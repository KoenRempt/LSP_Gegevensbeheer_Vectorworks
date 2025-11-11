from pygls.lsp.server import LanguageServer
from lsprotocol import types

from common import on_completion

server = LanguageServer("gegevensbeheer-server", "v0.1")


@server.feature(
    types.TEXT_DOCUMENT_COMPLETION,
    types.CompletionOptions(trigger_characters=["."]),
)
def on_completions(params: types.CompletionParams):
    document = server.workspace.get_text_document(params.text_document.uri)
    current_line = document.lines[params.position.line].strip()

    all_completions = []

    # Check for hello. pattern completions
    hello_completions = on_completion.get_hello_completions(current_line)
    all_completions.extend(hello_completions)

    # If no hello completions, provide function completions
    if not hello_completions:
        function_completions = on_completion.get_function_completions()
        all_completions.extend(function_completions)

    return all_completions


if __name__ == "__main__":
    server.start_io()
