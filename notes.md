# Change log

## Build Instructions

```bash
npm install -g vsce

cd myExtension
vsce package
# myExtension.vsix generated
# vsce publish
# <publisherID>.myExtension published to VS Code Marketplace
```


## Strip H2 from card header

/src/markdown/parser/cardParser.ts (line 148)

``` ts
let string = lines.join("\n")
    // $$\{1,2\} \%100$$ => $$\\{1,2\\} \\%100$$
    .replace(/(?<!\\)\$\$.+?(?<!\\)\$\$/gs, fixLatex)
    // $\{1,2\} \%100$ => $\\{1,2\\} \\%100$
    .replace(/(?<![\\$])\$(?!\$).+?(?<!\\)\$/gs, fixLatex);
string = lines.join("\n").replace("## ", ""); // ! changes

```

## Added deckname to default card template

/src/manageTemplate.ts (line 7)

```ts
const front = `<link rel="stylesheet" href="_vscodeAnkiPlugin.css" />{{Front}}

<br><br>
<div style='font-family: "Arial"; font-size: 16px;'>
<span id="deck">{{Deck}}</span><script>
document.getElementById("deck").innerHTML="{{Deck}}".split("::").pop();
</script>
</div>
`;
```

## Editing version number and author

/src/package.json (line 6)

```js
"publisher": "wrinkled",
```

/src/extensions.ts (line 46)

```js
const ankiExt = extensions.getExtension("wrinkled.anki"); //! This needed to be changed
```