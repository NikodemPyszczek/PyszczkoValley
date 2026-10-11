
from pathlib import Path

web_dir = Path("web-build")
index_path = web_dir / "index.html"
game_path = web_dir / "game.html"

if not index_path.exists():
    raise SystemExit("Nie znaleziono web-build/index.html")

if game_path.exists():
    raise SystemExit("Plik game.html już istnieje")

# Zachowaj oryginalną stronę GB Studio jako stronę gry.
index_path.rename(game_path)

# Utwórz nową stronę główną z osadzoną grą.
html = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pyszczko Valley</title>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: #17261e;
      color: #e9f5df;
      font-family: monospace;
    }

    .page {
      min-height: 100vh;
      padding: 24px 16px 48px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 24px;
    }

    h1 {
      margin: 0;
      font-size: 26px;
      text-align: center;
    }

    .game-frame {
      display: block;
      width: min(100%, 480px);
      aspect-ratio: 480 / 432;
      border: 3px solid #8eae81;
      border-radius: 8px;
      background: #000;
    }

    .controls {
      width: min(100%, 480px);
      padding: 20px;
      background: #263d34;
      border: 2px solid #8eae81;
      border-radius: 8px;
      text-align: center;
    }

    .keys {
      margin-top: 16px;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 14px;
      line-height: 2.5;
    }

    kbd {
      padding: 5px 8px;
      background: #e9f5df;
      color: #263d34;
      border-radius: 4px;
      font-weight: bold;
    }

    @media (hover: none) and (pointer: coarse) {
      .page {
        padding: 0;
        display: block;
      }

      h1, .controls {
        display: none;
      }

      .game-frame {
        position: fixed;
        inset: 0;
        width: 100%;
        height: 100dvh;
        aspect-ratio: auto;
        border: none;
        border-radius: 0;
      }
    }
  </style>
</head>
<body>
  <main class="page">
    <h1>Pyszczko Valley</h1>

    <iframe
      class="game-frame"
      src="./game.html"
      title="Pyszczko Valley - gra"
      allow="fullscreen"
      allowfullscreen>
    </iframe>

    <section class="controls" aria-label="Sterowanie">
      <strong>STEROWANIE</strong>
      <div class="keys">
        <span><kbd>↑ ↓ ← →</kbd> Ruch</span>
        <span><kbd>Z</kbd> Akcja</span>
        <span><kbd>X</kbd> Cofnij</span>
        <span><kbd>Enter</kbd> Start</span>
      </div>
    </section>
  </main>
</body>
</html>
"""

index_path.write_text(html, encoding="utf-8")
print("Utworzono stronę z osadzoną grą i legendą sterowania.")

