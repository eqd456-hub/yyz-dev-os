#!/usr/bin/env python3
"""Deterministically validate the portable YYZ Dev OS package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from validate_behavior_cases import validate_suite


ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()

REQUIRED_FILES = [
    "SKILL.md",
    "VERSION",
    "CHANGELOG.md",
    "README.md",
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
        if not path.is_file() or ".git" in path.parts:
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
