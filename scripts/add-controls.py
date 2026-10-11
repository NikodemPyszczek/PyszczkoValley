from pathlib import Path

html_path = Path("web-build/index.html")

if not html_path.exists():
    raise SystemExit("Nie znaleziono web-build/index.html")

html = html_path.read_text(encoding="utf-8")

controls = """
<style>
  #pyszczko-controls {
    margin: 18px auto 24px;
    padding: 14px 20px;
    width: fit-content;
    max-width: calc(100% - 40px);
    text-align: center;
    font-family: monospace;
    color: #e9f5df;
    background: #263d34;
    border: 2px solid #8eae81;
    border-radius: 8px;
    box-sizing: border-box;
  }

  #pyszczko-controls .keys {
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 14px;
  }

  #pyszczko-controls kbd {
    padding: 3px 7px;
    background: #e9f5df;
    color: #263d34;
    border-radius: 4px;
    font-weight: bold;
  }

  @media (hover: none) and (pointer: coarse) {
    #pyszczko-controls {
      display: none;
    }
  }
</style>

<div id="pyszczko-controls">
  <strong>STEROWANIE</strong>
  <div class="keys">
    <span><kbd>↑ ↓ ← →</kbd> Ruch</span>
    <span><kbd>Z</kbd> Akcja</span>
    <span><kbd>X</kbd> Cofnij</span>
    <span><kbd>Enter</kbd> Start</span>
  </div>
</div>
"""

if 'id="pyszczko-controls"' in html:
    raise SystemExit("Legenda sterowania już istnieje")

if "</body>" not in html:
    raise SystemExit("Nie znaleziono znacznika </body>")

html = html.replace("</body>", controls + "\n</body>", 1)

html_path.write_text(html, encoding="utf-8")

print("Dodano legendę sterowania do strony gry.")
