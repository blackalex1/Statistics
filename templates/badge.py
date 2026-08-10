def get_contact_badge_svg(username="blackalex1", color="#00FFAA"):
    width = 420
    height = 54
    
    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="tg-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0.02"/>
    </linearGradient>
  </defs>

  <style>
    :root {{
      --b-bg: #0d1117;
      --b-accent: {color};
      --b-text: #ffffff;
      --b-border: #30363d;
      --b-muted: #8b949e;
    }}
    @media (prefers-color-scheme: light) {{
      :root {{
        --b-bg: #ffffff;
        --b-accent: #0969da;
        --b-text: #1f2328;
        --b-border: #d0d7de;
        --b-muted: #636c76;
      }}
    }}

    .badge-card {{
      fill: var(--b-bg);
      stroke: var(--b-border);
      stroke-width: 1.5;
    }}

    .badge-hud {{
      stroke: var(--b-accent);
      stroke-width: 1.5;
      fill: none;
      opacity: 0.8;
    }}

    .tg-title {{
      font: bold 12px 'JetBrains Mono', 'Segoe UI', monospace;
      fill: var(--b-text);
      letter-spacing: 1.5px;
    }}

    .tg-handle {{
      font: bold 11px 'JetBrains Mono', monospace;
      fill: var(--b-accent);
      letter-spacing: 1px;
    }}

    .tg-meta {{
      font: bold 9px 'JetBrains Mono', monospace;
      fill: var(--b-muted);
      letter-spacing: 1px;
    }}

    .tg-icon {{
      fill: var(--b-accent);
    }}

    @keyframes live-pulse {{
      0%, 100% {{ opacity: 0.4; transform: scale(1); }}
      50% {{ opacity: 1; transform: scale(1.2); }}
    }}

    .status-dot {{
      fill: var(--b-accent);
      animation: live-pulse 2s infinite ease-in-out;
      transform-origin: {width - 32}px 27px;
    }}
  </style>

  <rect width="{width}" height="{height}" rx="8" class="badge-card"/>
  <rect width="{width}" height="{height}" rx="8" fill="url(#tg-grad)"/>

  <!-- Tactical Corner Brackets -->
  <path d="M 0 10 L 0 0 L 10 0" class="badge-hud"/>
  <path d="M {width} 10 L {width} 0 L {width-10} 0" class="badge-hud"/>
  <path d="M 0 {height-10} L 0 {height} L 10 {height}" class="badge-hud"/>
  <path d="M {width} {height-10} L {width} {height} L {width-10} {height}" class="badge-hud"/>

  <!-- Telegram Glyph (Vector accurate) -->
  <g transform="translate(18, 15)">
    <path d="M21.5 2.1L1.8 9.7C0.5 10.2 0.5 11 1.6 11.3L6.6 12.9L18.2 5.6C18.7 5.3 19.2 5.5 18.8 5.8L9.4 14.3L9 19.5C9.5 19.5 9.7 19.3 10 19L12.4 16.7L17.4 20.4C18.3 20.9 19 20.6 19.2 19.5L22.5 4C22.8 2.8 22 2.2 21.5 2.1Z" class="tg-icon"/>
  </g>

  <!-- Content -->
  <text x="56" y="24" class="tg-title">TELEGRAM // DIRECT LINK</text>
  <text x="56" y="40" class="tg-handle">@{username}</text>

  <!-- Live Status Beacon -->
  <circle cx="{width - 32}" cy="27" r="4.5" class="status-dot"/>
  <text x="{width - 45}" y="30" text-anchor="end" class="tg-meta">[ONLINE]</text>
</svg>"""
