import re, sys

def esc_html(s):
    return ''.join(c if ord(c) < 128 else f'&#{ord(c)};' for c in s)

def esc_js(s):
    return ''.join(c if ord(c) < 128 else f'\\u{ord(c):04x}' for c in s)

for path in sys.argv[1:]:
    text = open(path, encoding='utf-8').read()
    # ensure charset meta is first
    if '<meta charset' not in text.split('\n', 1)[0].lower():
        text = '<meta charset="utf-8">\n' + text
    # split out <script>...</script> so JS uses \u and HTML uses &#;
    parts = re.split(r'(<script[^>]*>.*?</script>)', text, flags=re.S | re.I)
    out = []
    for p in parts:
        m = re.match(r'(<script[^>]*>)(.*?)(</script>)', p, flags=re.S | re.I)
        if m:
            out.append(m.group(1) + esc_js(m.group(2)) + m.group(3))
        else:
            out.append(esc_html(p))
    open(path, 'w', encoding='utf-8').write(''.join(out))
    # report residual non-ascii (should be 0)
    residual = sum(1 for c in open(path, encoding='utf-8').read() if ord(c) > 127)
    print(f"{path}: residual non-ASCII bytes = {residual}")
