#!/usr/bin/env python3

import copy
import json
from functools import lru_cache
from pathlib import Path


DEFAULT_CONFIG = {
    "paths": {
        "obsidian_vault": "~/ObsidianVault",
        "paper_notes_folder": "论文笔记",
        "daily_papers_folder": "DailyPapers",
        "concepts_folder": "_概念",
        "guided_reading_folder": "共读精读",
        "zotero_db": "~/Zotero/zotero.sqlite",
        "zotero_storage": "~/Zotero/storage",
    },
    "daily_papers": {
        "keywords": [
            "trajectory inference",
            "single-cell",
            "single cell",
            "flow matching",
            "neural ode",
            "schrödinger bridge",
            "schrodinger bridge",
            "energy-based model",
            "score matching",
            "action matching",
            "potential energy landscape",
            "cell reprogramming",
            "cell development",
        ],
        "negative_keywords": [
            "large language model",
            "llm",
            "embodied ai",
            "robot",
            "manipulation",
            "autonomous driving",
            "nlp",
            "natural language processing",
            "prompt engineering",
            "text-to-image",
            "audio generation",
            "coding agent",
            "code generation",
            "weather forecast",
            "trading",
            "financial",
            "software engineering",
            "object detection",
            "image segmentation",
        ],
        "domain_boost_keywords": [
            "scrna-seq",
            "transcriptomics",
            "dynamic system",
            "optimal transport",
            "perturbation",
            "b-spline",
            "time-varying",
            "distributional",
            "moment transfer",
        ],
        "arxiv_categories": ["q-bio.QM", "q-bio.CB", "cs.LG", "stat.ML", "cond-mat.stat-mech"],
        "pubmed_journals": [
            "Cell",
            "Cell Systems",
            "Cell Genomics",
            "Cell Reports",
            "Developmental Cell",
            "Nature",
            "Nature Biotechnology",
            "Nature Methods",
            "Nature Genetics",
            "Nature Communications",
            "Science",
            "Science Advances",
        ],
        "min_score": 2,
        "top_n": 30,
    },
    "automation": {
        "auto_refresh_indexes": True,
        "git_commit": False,
        "git_push": False,
    },
}


def _deep_merge(base: dict, override: dict) -> dict:
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value
    return base


@lru_cache(maxsize=1)
def load_user_config() -> dict:
    config = copy.deepcopy(DEFAULT_CONFIG)
    config_dir = Path(__file__).resolve().parent

    for filename in ("user-config.json", "user-config.local.json"):
        config_path = config_dir / filename
        if not config_path.exists():
            continue
        with config_path.open("r", encoding="utf-8") as f:
            loaded = json.load(f)
        if isinstance(loaded, dict):
            _deep_merge(config, loaded)

    return config


def _expand(path_value: str) -> Path:
    return Path(path_value).expanduser()


def paths_config() -> dict:
    return load_user_config()["paths"]


def daily_papers_config() -> dict:
    return load_user_config()["daily_papers"]


def automation_config() -> dict:
    config = load_user_config()["automation"]
    if config.get("git_push") and not config.get("git_commit"):
        config = copy.deepcopy(config)
        config["git_push"] = False
    return config


def obsidian_vault_path() -> Path:
    return _expand(paths_config()["obsidian_vault"])


def paper_notes_dir() -> Path:
    return obsidian_vault_path() / paths_config()["paper_notes_folder"]


def daily_papers_dir() -> Path:
    return obsidian_vault_path() / paths_config()["daily_papers_folder"]


def concepts_dir() -> Path:
    return paper_notes_dir() / paths_config()["concepts_folder"]


def zotero_db_path() -> Path:
    return _expand(paths_config()["zotero_db"])


def zotero_storage_dir() -> Path:
    return _expand(paths_config()["zotero_storage"])


def auto_refresh_indexes_enabled() -> bool:
    return bool(automation_config()["auto_refresh_indexes"])


def git_commit_enabled() -> bool:
    return bool(automation_config()["git_commit"])


def git_push_enabled() -> bool:
    return bool(automation_config()["git_push"])
