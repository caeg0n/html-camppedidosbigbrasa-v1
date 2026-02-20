import os
import re

entities = {
    "&aacute;": "á",
    "&Aacute;": "Á",
    "&eacute;": "é",
    "&Eacute;": "É",
    "&iacute;": "í",
    "&Iacute;": "Í",
    "&oacute;": "ó",
    "&Oacute;": "Ó",
    "&uacute;": "ú",
    "&Uacute;": "Ú",
    "&atilde;": "ã",
    "&Atilde;": "Ã",
    "&otilde;": "õ",
    "&Otilde;": "Õ",
    "&acirc;": "â",
    "&Acirc;": "Â",
    "&ecirc;": "ê",
    "&Ecirc;": "Ê",
    "&icirc;": "î",
    "&Icirc;": "Î",
    "&ocirc;": "ô",
    "&Ocirc;": "Ô",
    "&ucirc;": "û",
    "&Ucirc;": "Û",
    "&ccedil;": "ç",
    "&Ccedil;": "Ç",
    "&amp;": "&"
}

def replace_entities(text):
    for entity, char in entities.items():
        text = text.replace(entity, char)
    return text

files = [
    r"c:\html\html-camppedidos-v1\html-camppedidosbigbrasa-v1\menu-data.js",
    r"c:\html\html-camppedidos-v1\html-camppedidosbigbrasa-v1\index.html",
    r"c:\html\html-camppedidos-v1\html-camppedidosbigbrasa-v1\compras\index.html"
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = replace_entities(content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No changes in {file}")

