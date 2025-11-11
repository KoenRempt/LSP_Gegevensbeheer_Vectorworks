from lsprotocol.types import CompletionItem, MarkupContent, MarkupKind
import json
from typing import TypedDict
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent.parent
FUNCTIONS_JSON_PATH = ROOT_DIR / "src" / "common" / "on_completion" / "functions.json"


class Function(TypedDict):
    label: str
    detail: str
    documentation: str
    insert_text: str


class JSON(TypedDict):
    functions: list[Function]


def get_json_data():
    """Load JSON data from a file or define it inline"""
    # For demonstration, we'll define it inline
    with open(FUNCTIONS_JSON_PATH, "r", encoding="utf-8") as f:
        json_content: JSON = json.load(f)
    return json_content


def get_function_completions():
    """Handle general function completions"""
    json_data = get_json_data()
    completions = []

    for func in json_data["functions"]:
        item = CompletionItem(
            label=func["label"],
            detail=func["detail"],
            documentation=MarkupContent(MarkupKind.Markdown, value=func["documentation"]),
            insert_text=func["insert_text"],
        )
        completions.append(item)

    return completions
