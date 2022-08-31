const vscode = require('vscode');

function activate(context) {
	let editorConfig = vscode.workspace.getConfiguration('editor');

	let makeDefault = vscode.commands.registerCommand('code-zoom.default', () => {
		editorConfig.update('fontSize');
		editorConfig.update('lineHeight');
	});

	let makeSmall = vscode.commands.registerCommand('code-zoom.small', () => {
		let codeZoomConfig = vscode.workspace.getConfiguration('code-zoom');

		editorConfig.update('fontSize', codeZoomConfig.get('small.fontSize', 12));
		editorConfig.update('lineHeight', codeZoomConfig.get('small.lineHeight', 1.25));
	});

	let makeBig = vscode.commands.registerCommand('code-zoom.big', () => {
		let codeZoomConfig = vscode.workspace.getConfiguration('code-zoom');

		editorConfig.update('fontSize', codeZoomConfig.get('big.fontSize', 32));
		editorConfig.update('lineHeight', codeZoomConfig.get('big.lineHeight', 4));
	});

	context.subscriptions.push(makeDefault, makeSmall, makeBig);
}

function deactivate() {
	let config = vscode.workspace.getConfiguration('editor');

	config.update('fontSize');
	config.update('lineHeight');
}

module.exports = {
	activate,
	deactivate
}
