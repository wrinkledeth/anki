# Anki for Vscode

This is my personal fork of [Anki for vscode](https://github.com/jasonwilliams/anki)

There are two changes:

- H2 stripped from card header
- Deck name added to default card templat

[Original README.md](https://github.com/wrinkledeth/anki/blob/main/README_ORIGINAL.md)

[Detailed notes on changes](https://github.com/wrinkledeth/anki/blob/main/notes.md)

[Anki to Markdown Helper Script](https://github.com/wrinkledeth/anki/tree/main/scripts)

## Build Instructions

```bash
npm install -g vsce

cd myExtension
vsce package
# myExtension.vsix generated
```

Install Extension to Vscode from CLI

```bash
code --install-extension anki-1.2.8.vsix
```
