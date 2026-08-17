#!/usr/bin/env python3
"""Generate preview.html from README.md with a Dark/Light theme switcher."""

from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUTPUT = ROOT / "preview.html"

TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Abrar Morshed — GitHub profile preview</title>
  <link id="md-theme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-dark.min.css" />
  <style>
    :root {{
      --bg: #0d1117;
      --border: #30363d;
      --text: #e6edf3;
      --muted: #8b949e;
      --link: #4493f8;
      --accent: #6366f1;
    }}
    html[data-theme="light"] {{
      --bg: #ffffff;
      --border: #d0d7de;
      --text: #1f2328;
      --muted: #656d76;
      --link: #0969da;
      --accent: #4f46e5;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }}
    .topbar {{
      height: 64px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      position: sticky;
      top: 0;
      background: color-mix(in srgb, var(--bg) 92%, transparent);
      backdrop-filter: blur(12px);
      z-index: 10;
      gap: 16px;
    }}
    .brand {{ display: flex; gap: 10px; align-items: center; font-weight: 600; min-width: 0; }}
    .brand svg {{ width: 32px; height: 32px; fill: var(--text); flex-shrink: 0; }}
    .controls {{ display: flex; align-items: center; gap: 12px; flex-shrink: 0; }}
    .hint {{ color: var(--muted); font-size: 13px; }}
    .theme-switch {{
      display: inline-flex;
      border: 1px solid var(--border);
      border-radius: 8px;
      overflow: hidden;
      background: var(--bg);
    }}
    .theme-switch button {{
      border: 0;
      background: transparent;
      color: var(--muted);
      padding: 6px 14px;
      cursor: pointer;
      font: inherit;
      font-size: 13px;
      font-weight: 600;
    }}
    .theme-switch button.active {{
      background: var(--accent);
      color: #fff;
    }}
    .layout {{
      max-width: 1280px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 296px 1fr;
      gap: 24px;
      padding: 24px;
    }}
    @media (max-width: 900px) {{
      .layout {{ grid-template-columns: 1fr; }}
      .hint {{ display: none; }}
    }}
    .avatar {{
      width: 296px;
      max-width: 100%;
      aspect-ratio: 1;
      border-radius: 50%;
      border: 1px solid var(--border);
    }}
    .name {{ font-size: 24px; font-weight: 700; margin: 16px 0 0; }}
    .login {{ font-size: 20px; font-weight: 300; color: var(--muted); margin: 0 0 12px; }}
    .bio {{ margin-bottom: 16px; line-height: 1.5; }}
    .meta {{ color: var(--muted); font-size: 14px; display: grid; gap: 8px; }}
    .meta a {{ color: var(--link); text-decoration: none; }}
    .readme {{
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 32px;
      background: var(--bg);
      min-width: 0;
    }}
    .markdown-body {{ background: transparent !important; }}
    .markdown-body a {{ color: var(--link); }}
    .markdown-body table {{ display: table; width: 100%; }}
    .markdown-body img {{ background: transparent; }}
    html[data-theme="light"] .markdown-body {{ color-scheme: light; color: #1f2328; }}

    /* Preview-only: show one theme variant at a time */
    html[data-theme="dark"] img[src*="gh-light-mode-only"] {{ display: none !important; }}
    html[data-theme="light"] img[src*="gh-dark-mode-only"] {{ display: none !important; }}
  </style>
</head>
<body>
  <div class="topbar">
    <div class="brand">
      <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/></svg>
      <span>AbrarSoul — profile preview</span>
    </div>
    <div class="controls">
      <span class="hint">Use the switcher to preview each theme</span>
      <div class="theme-switch" role="group" aria-label="Theme">
        <button type="button" data-theme="dark" class="active">Dark</button>
        <button type="button" data-theme="light">Light</button>
      </div>
    </div>
  </div>
  <div class="layout">
    <aside>
      <img class="avatar" src="https://avatars.githubusercontent.com/u/73701376?v=4" alt="Abrar Morshed" />
      <h1 class="name">Abrar Morshed</h1>
      <p class="login">AbrarSoul</p>
      <p class="bio">Programmer | Researcher | M.Sc. in Computing Science</p>
      <div class="meta">
        <div>GPT-Lab (Tampere University)</div>
        <div>Tampere, Finland</div>
        <div><a href="https://abrarsoul.github.io/">abrarsoul.github.io</a></div>
        <div><a href="mailto:abrar.morshed@tuni.fi">abrar.morshed@tuni.fi</a></div>
      </div>
    </aside>
    <article class="readme markdown-body">
{body}
    </article>
  </div>
  <script>
    const html = document.documentElement;
    const mdTheme = document.getElementById("md-theme");
    const buttons = [...document.querySelectorAll(".theme-switch button")];

    const setTheme = (theme) => {{
      html.dataset.theme = theme;
      localStorage.setItem("preview-theme", theme);
      mdTheme.href = theme === "dark"
        ? "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-dark.min.css"
        : "https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown-light.min.css";
      buttons.forEach((btn) => btn.classList.toggle("active", btn.dataset.theme === theme));
    }};

    buttons.forEach((btn) => btn.addEventListener("click", () => setTheme(btn.dataset.theme)));
    setTheme(localStorage.getItem("preview-theme") || "dark");
  </script>
</body>
</html>
"""


def main() -> None:
    md = README.read_text(encoding="utf-8")
    body = markdown.markdown(md, extensions=["extra", "sane_lists", "nl2br"])
    OUTPUT.write_text(TEMPLATE.format(body=body), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
