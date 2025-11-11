import * as path from "path";
import * as vscode from "vscode";
import { LanguageClient, LanguageClientOptions, ServerOptions, TransportKind } from "vscode-languageclient/node";

let client: LanguageClient;

export function activate(context: vscode.ExtensionContext) {
    // Path to your Python interpreter inside the virtual environment
    const pythonExecutable = process.platform === "win32"
        ? path.join(context.asAbsolutePath("server/.venv/Scripts/python.exe"))
        : path.join(context.asAbsolutePath("server/.venv/bin/python"));

    // Path to the Python server
    const serverScript = context.asAbsolutePath("server/src/server.py");

    // Define how to run the server
    const serverOptions: ServerOptions = {
        command: pythonExecutable,
        args: [serverScript],
        transport: TransportKind.stdio
    };

    // Options for the VSCode client
    const clientOptions: LanguageClientOptions = {
        documentSelector: [{ scheme: "file", language: "gegevensbeheer" }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher("**/.clientrc")
        }
    };

    // Create the language client
    client = new LanguageClient(
        "gegevensbeheerLanguageServer",
        "Gegevensbeheer Language Server",
        serverOptions,
        clientOptions
    );

    // Start the client
    client.start();
}

export function deactivate(): Thenable<void> | undefined {
    if (!client) {
        return undefined;
    }
    return client.stop();
}
