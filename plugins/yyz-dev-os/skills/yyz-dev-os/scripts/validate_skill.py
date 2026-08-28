#!/usr/bin/env python3
"""Deterministically validate the portable YYZ Dev OS package."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

from validate_behavior_cases import validate_suite


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
IS_PLUGIN_SNAPSHOT = (
    ROOT.parent.name == "skills"
    and ROOT.parent.parent.name == "yyz-dev-os"
    and (ROOT.parent.parent / ".codex-plugin/plugin.json").is_file()
)
PLUGIN_SNAPSHOT_ROOT = ROOT / "plugins" / "yyz-dev-os" / "skills" / "yyz-dev-os"

REQUIRED_FILES = [
    "SKILL.md",
    "VERSION",
    "CHANGELOG.md",
    "README.md",
    "LICENSE",
    ".gitignore",
    ".gitattributes",
    "agents/openai.yaml",
    "references/rules/operating-principles.md",
    "references/rules/source-of-truth.md",
    "references/rules/ai-role-policy.md",
    "references/rules/routing-policy.md",
    "references/rules/verification-policy.md",
    "references/rules/git-policy.md",
    "references/rules/memory-policy.md",
    "references/rules/recovery-policy.md",
    "references/rules/approval-risk-policy.md",
    "references/rules/storage-policy.md",
    "references/rules/reporting-policy.md",
    "references/rules/self-audit-policy.md",
    "references/protocols/project-bootstrap.md",
    "references/protocols/project-recovery.md",
    "references/protocols/code-health-audit.md",
    "references/protocols/website-development.md",
    "references/protocols/implementation.md",
    "references/protocols/independent-review.md",
    "references/protocols/repair-loop.md",
    "references/protocols/project-handoff.md",
    "assets/templates/recovery-entry.template.json",
    "assets/templates/current-state.template.json",
    "assets/templates/roadmap.template.json",
    "assets/templates/decisions.template.json",
    "assets/templates/known-issues.template.json",
    "assets/templates/operating-rules.template.json",
    "assets/templates/project-bootstrap.md",
    "assets/schemas/recovery-entry.schema.json",
    "tests/behavior-cases.json",
    "tests/test_validate_behavior_cases.py",
    "scripts/validate_behavior_cases.py",
    "scripts/validate_skill.py",
]
if not IS_PLUGIN_SNAPSHOT:
    REQUIRED_FILES.extend(
        [
            ".agents/plugins/marketplace.json",
            "docs/index.md",
            "docs/_config.yml",
            "docs/privacy.md",
            "docs/terms.md",
            "docs/support.md",
            "plugins/yyz-dev-os/.codex-plugin/plugin.json",
            "scripts/build_plugin_package.py",
            "submission/openai-public-listing.md",
            "submission/openai-public-listing.json",
            "submission/openai-review-cases.json",
        ]
    )

SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
WINDOWS_ABSOLUTE = re.compile(r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]")
UNIX_MACHINE_PATH = re.compile(r"/(?:Users|home)/[^\s`\"']+")
LIVE_PROJECT_MARKERS = [
    re.compile(r"\b[0-9a-fA-F]{40}\b"),
    re.compile(r"\bDEV-[0-9]"),
    re.compile(r"YYZ AI Dev Orchestrator", re.IGNORECASE),
]
SECRET_VALUE_PATTERNS = [
    re.compile("s" + r"k-[A-Za-z0-9_-]{20,}"),
    re.compile("gh" + r"[pousr]_[A-Za-z0-9]{20,}"),
    re.compile("AK" + r"IA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]
FORBIDDEN_JSON_KEYS = {
    "apikey",
    "api_key",
    "token",
    "access_token",
    "refresh_token",
    "secret",
    "password",
    "private_key",
}


def load_json(path: Path, failures: list[str]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        failures.append(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")
        return None


def walk_json(value: Any, path: str, failures: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key.lower() in FORBIDDEN_JSON_KEYS:
                failures.append(f"Secret-like JSON key: {path}.{key}")
            walk_json(child, f"{path}.{key}", failures)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk_json(child, f"{path}[{index}]", failures)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or ".git" in path.parts
            or PLUGIN_SNAPSHOT_ROOT in path.parents
        ):
            continue
        if path.name == "VERSION" or path.suffix.lower() in {
            ".md",
            ".json",
            ".yaml",
            ".yml",
            ".py",
            ".txt",
        }:
            files.append(path)
    return files


def validate_frontmatter(failures: list[str]) -> str:
    path = ROOT / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) >= 500:
        failures.append(f"SKILL.md must stay below 500 lines; found {len(lines)}")
    if len(lines) < 5 or lines[0] != "---":
        failures.append("SKILL.md is missing YAML frontmatter")
        return text
    try:
        end = lines.index("---", 1)
    except ValueError:
        failures.append("SKILL.md frontmatter is not closed")
        return text
    keys = []
    for line in lines[1:end]:
        if line and not line.startswith((" ", "\t")) and ":" in line:
            keys.append(line.split(":", 1)[0])
    if keys != ["name", "description"]:
        failures.append(f"SKILL.md frontmatter keys must be name, description; found {keys}")
    if "name: yyz-dev-os" not in "\n".join(lines[1:end]):
        failures.append("SKILL.md name must be yyz-dev-os")
    return text


def validate_recovery_contract(failures: list[str]) -> None:
    path = ROOT / "assets/templates/recovery-entry.template.json"
    data = load_json(path, failures)
    if not isinstance(data, dict):
        return
    required = {
        "schemaVersion",
        "projectId",
        "projectName",
        "repository",
        "globalSkill",
        "globalSkillVersion",
        "projectBrainRoot",
        "bindings",
        "recoveryOrder",
        "authorityOrder",
        "rules",
    }
    missing = sorted(required - data.keys())
    if missing:
        failures.append(f"Recovery template missing fields: {', '.join(missing)}")
    if data.get("globalSkill") != "yyz-dev-os":
        failures.append("Recovery template has the wrong globalSkill identity")
    if data.get("globalSkillVersion") != (ROOT / "VERSION").read_text(encoding="utf-8").strip():
        failures.append("Recovery template version does not match VERSION")
    recovery_order = data.get("recoveryOrder")
    if not isinstance(recovery_order, list) or recovery_order[:2] != ["global-skill", "git"]:
        failures.append("Recovery template must load global-skill before observing Git")
    rules = data.get("rules")
    if not isinstance(rules, dict) or rules.get("doNotUseChatMemoryAsProjectTruth") is not True:
        failures.append("Recovery template must prohibit chat memory as project truth")
    bindings = data.get("bindings")
    binding_keys = {
        "architecture",
        "trustedCheckpoint",
        "evidenceIndex",
        "globalCapabilityLedger",
        "projectCapabilityLedger",
    }
    if not isinstance(bindings, dict) or set(bindings) != binding_keys:
        failures.append("Recovery template must declare all architecture, checkpoint, evidence, and ledger bindings")


def validate_project_bootstrap_version(version: str, failures: list[str]) -> None:
    path = ROOT / "assets/templates/project-bootstrap.md"
    text = path.read_text(encoding="utf-8")
    matches = re.findall(
        r"^- Loaded compatible Skill version:\s+`([^`]+)`\s*$",
        text,
        flags=re.MULTILINE,
    )
    if len(matches) != 1:
        failures.append("Project bootstrap template must declare exactly one Loaded compatible Skill version")
    elif matches[0] != version:
        failures.append("Project bootstrap template version does not match VERSION")


def validate_public_listing_candidate(version: str, failures: list[str]) -> None:
    listing_path = ROOT / "submission/openai-public-listing.json"
    listing = load_json(listing_path, failures)
    if not isinstance(listing, dict):
        return
    expected = {
        "schemaVersion": 1,
        "status": "READY_FOR_PORTAL_SUBMISSION",
        "distribution": "PRIVATE_TEAM_ONLY_UNTIL_APPROVED",
        "pluginType": "SKILLS_ONLY",
        "category": "Productivity",
        "publisherIdentity": "杨元钊",
        "developerDisplayName": "YYZ",
    }
    for key, value in expected.items():
        if listing.get(key) != value:
            failures.append(f"Public listing candidate has invalid {key}")
    public_urls = listing.get("publicURLs")
    expected_urls = {
        "website": "https://eqd456-hub.github.io/yyz-dev-os/",
        "support": "https://github.com/eqd456-hub/yyz-dev-os/issues",
        "privacy": "https://eqd456-hub.github.io/yyz-dev-os/privacy.html",
        "terms": "https://eqd456-hub.github.io/yyz-dev-os/terms.html",
    }
    if public_urls != expected_urls:
        failures.append("Public listing candidate must declare the approved public URLs")
    assets = listing.get("assets")
    expected_asset_path = "./plugins/yyz-dev-os/assets/yyz-dev-os-logo.png"
    if not isinstance(assets, dict) or assets != {
        "logo": expected_asset_path,
        "composerIcon": expected_asset_path,
    }:
        failures.append("Public listing candidate must declare the packaged logo and composer icon")
    elif not IS_PLUGIN_SNAPSHOT:
        plugin_root = (ROOT / "plugins/yyz-dev-os").resolve()
        asset_path = (ROOT / expected_asset_path.removeprefix("./")).resolve()
        if not asset_path.is_relative_to(plugin_root):
            failures.append("Public listing asset must stay inside the plugin root")
        elif asset_path.suffix.lower() != ".png" or not asset_path.is_file():
            failures.append("Public listing asset must be an existing PNG file")
        else:
            asset_bytes = asset_path.read_bytes()
            if asset_bytes[:8] != b"\x89PNG\r\n\x1a\n":
                failures.append("Public listing asset must have a PNG signature")
            elif len(asset_bytes) < 26 or asset_bytes[25] not in {4, 6}:
                failures.append("Public listing asset must use a PNG alpha channel")
    release_notes = listing.get("releaseNotes")
    if not isinstance(release_notes, str) or version not in release_notes:
        failures.append("Public listing candidate release notes must name the current VERSION")

    cases_path = ROOT / "submission/openai-review-cases.json"
    cases = load_json(cases_path, failures)
    if not isinstance(cases, dict) or cases.get("schemaVersion") != 1:
        failures.append("Public review cases must have schemaVersion 1")
        return
    for key, expected_count in (("positiveCases", 5), ("negativeCases", 3)):
        values = cases.get(key)
        if not isinstance(values, list) or len(values) != expected_count:
            failures.append(f"Public review cases must contain {expected_count} {key}")
            continue
        seen_ids: set[str] = set()
        for case in values:
            if not isinstance(case, dict):
                failures.append(f"Public {key} entries must be objects")
                continue
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id.strip() or case_id in seen_ids:
                failures.append(f"Public {key} entries require unique non-empty ids")
            seen_ids.add(case_id) if isinstance(case_id, str) else None
            for field in ("prompt", "expectedOutcome"):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    failures.append(f"Public {key} entry {case_id!r} requires {field}")


def validate_plugin_packaging(version: str, failures: list[str]) -> None:
    marketplace_path = ROOT / ".agents/plugins/marketplace.json"
    marketplace = load_json(marketplace_path, failures)
    if not isinstance(marketplace, dict):
        return
    if marketplace.get("name") != "yyz-team":
        failures.append("Marketplace name must be yyz-team")
    interface = marketplace.get("interface")
    if not isinstance(interface, dict) or interface.get("displayName") != "YYZ Team":
        failures.append("Marketplace displayName must be YYZ Team")
    plugins = marketplace.get("plugins")
    expected_entry = {
        "name": "yyz-dev-os",
        "source": {"source": "local", "path": "./plugins/yyz-dev-os"},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }
    if not isinstance(plugins, list) or plugins != [expected_entry]:
        failures.append("Marketplace must contain the expected yyz-dev-os team plugin entry")

    manifest_path = ROOT / "plugins/yyz-dev-os/.codex-plugin/plugin.json"
    manifest = load_json(manifest_path, failures)
    if not isinstance(manifest, dict):
        return
    if manifest.get("name") != "yyz-dev-os":
        failures.append("Plugin manifest name must be yyz-dev-os")
    if manifest.get("version") != version:
        failures.append("Plugin manifest version does not match VERSION")
    if manifest.get("skills") != "./skills/":
        failures.append("Plugin manifest skills path must be ./skills/")
    if manifest.get("homepage") != "https://eqd456-hub.github.io/yyz-dev-os/":
        failures.append("Plugin manifest homepage must match the public website")
    if manifest.get("license") != "MIT":
        failures.append("Plugin manifest license must be MIT")
    if any(key in manifest for key in ("mcpServers", "apps", "hooks")):
        failures.append("Skill-only plugin manifest must not declare MCP, apps, or hooks")
    manifest_interface = manifest.get("interface")
    expected_plugin_asset = "./assets/yyz-dev-os-logo.png"
    manifest_author = manifest.get("author")
    if not isinstance(manifest_author, dict) or manifest_author.get("name") != "杨元钊":
        failures.append("Plugin manifest must use the selected individual publisher name")
    if not isinstance(manifest_interface, dict) or any(
        (
            manifest_interface.get("developerName") != "YYZ",
            manifest_interface.get("brandColor") != "#E10600",
            manifest_interface.get("logo") != expected_plugin_asset,
            manifest_interface.get("composerIcon") != expected_plugin_asset,
            manifest_interface.get("websiteURL")
            != "https://eqd456-hub.github.io/yyz-dev-os/",
            manifest_interface.get("privacyPolicyURL")
            != "https://eqd456-hub.github.io/yyz-dev-os/privacy.html",
            manifest_interface.get("termsOfServiceURL")
            != "https://eqd456-hub.github.io/yyz-dev-os/terms.html",
        )
    ):
        failures.append("Plugin manifest must declare the packaged brand color, logo, and composer icon")

    build_script = ROOT / "scripts/build_plugin_package.py"
    result = subprocess.run(
        [sys.executable, str(build_script), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stdout + result.stderr).strip().replace("\n", " | ")
        failures.append(f"Plugin snapshot is not synchronized: {detail}")


def main() -> int:
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            failures.append(f"Missing required file: {relative}")

    if failures:
        print("YYZ Dev OS validation FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not SEMVER.fullmatch(version):
        failures.append(f"VERSION is not valid Semantic Versioning: {version!r}")
    if f"[{version}]" not in (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"):
        failures.append("CHANGELOG.md does not contain the current VERSION")

    skill_text = validate_frontmatter(failures)
    recovery_text = (ROOT / "references/protocols/project-recovery.md").read_text(encoding="utf-8")
    memory_text = (ROOT / "references/rules/memory-policy.md").read_text(encoding="utf-8")
    if "Never use chat memory as project truth" not in recovery_text:
        failures.append("Project Recovery must explicitly reject chat memory as truth")
    if "Global Development Skill" not in memory_text or "Project Brain" not in memory_text:
        failures.append("Global and project memory scopes are not explicitly separated")
    if "project's current commit" not in skill_text:
        failures.append("SKILL.md does not explicitly prohibit live project state")

    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            failures.append(f"Unreadable UTF-8 file: {path.relative_to(ROOT)}: {exc}")
            continue
        relative = path.relative_to(ROOT)
        if path != SELF:
            if WINDOWS_ABSOLUTE.search(text) or UNIX_MACHINE_PATH.search(text):
                failures.append(f"Machine-specific absolute path in {relative}")
            for pattern in LIVE_PROJECT_MARKERS:
                if pattern.search(text):
                    failures.append(f"Project-specific live-state marker in {relative}")
            for pattern in SECRET_VALUE_PATTERNS:
                if pattern.search(text):
                    failures.append(f"Secret-like value in {relative}")

    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        data = load_json(path, failures)
        if data is not None:
            walk_json(data, str(path.relative_to(ROOT)), failures)

    schema_path = ROOT / "assets/schemas/recovery-entry.schema.json"
    schema = load_json(schema_path, failures)
    if isinstance(schema, dict) and schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        failures.append("Recovery schema must declare JSON Schema draft 2020-12")
    validate_recovery_contract(failures)
    validate_project_bootstrap_version(version, failures)
    if not IS_PLUGIN_SNAPSHOT:
        validate_public_listing_candidate(version, failures)
        validate_plugin_packaging(version, failures)

    behavior_failures, behavior_counts = validate_suite()
    failures.extend(behavior_failures)

    yaml_text = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    if "$yyz-dev-os" not in yaml_text:
        failures.append("agents/openai.yaml default_prompt must mention $yyz-dev-os")

    if failures:
        print("YYZ Dev OS validation FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("YYZ Dev OS validation PASSED")
    print(f"- version: {version}")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print("- JSON templates and schema: parseable")
    print("- recovery truth rule: enforced")
    print("- global/project scope: separated")
    print(f"- behavior routing contracts: {sum(behavior_counts.values())} cases")
    print("- machine paths, live project markers, and secret-like values: none found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
