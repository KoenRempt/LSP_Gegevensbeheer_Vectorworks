from lsprotocol.types import CompletionItem


def get_hello_completions(current_line: str):
    """Handle completions for 'hello.' pattern"""
    if not current_line.endswith("hello."):
        return []

    return [
        CompletionItem(label="world"),
        CompletionItem(label="friend"),
        CompletionItem(label="Inias"),
        CompletionItem(label="papa"),
    ]
