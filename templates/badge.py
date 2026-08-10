def get_contact_badge_svg(username="blackalex1", color="#00FFAA"):
    width = 850
    height = 46
    
    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="tg-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0.02"/>
    </linearGradient>
  </defs>

  <style>
    :root {{
      --b-bg: #161b22;
      --b-accent: {color};
      --b-text: #ffffff;
      --b-border: #30363d;
      --b-muted: #8b949e;
    }}
    @media (prefers-color-scheme: light) {{
      :root {{
        --b-bg: #f6f8fa;
        --b-accent: #1a7f37;
        --b-text: #1f2328;
        --b-border: #d0d7de;
        --b-muted: #636c76;
      }}
    }}

    .badge-card {{
      fill: var(--b-bg);
      stroke: var(--b-border);
      stroke-width: 1.2;
    }}

    .badge-hud {{
      stroke: var(--b-accent);
      stroke-width: 1.5;
      fill: none;
      opacity: 0.85;
    }}

    .tg-title {{
      font: bold 12px 'JetBrains Mono', monospace;
      fill: var(--b-text);
      letter-spacing: 1.5px;
    }}

    .tg-meta {{
      font: bold 10px 'JetBrains Mono', monospace;
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
      transform-origin: {width - 32}px 23px;
    }}
  </style>

  <rect width="{width}" height="{height}" rx="6" class="badge-card"/>
  <rect width="{width}" height="{height}" rx="6" fill="url(#tg-grad)"/>

  <!-- Tactical Corner Brackets -->
  <path d="M 0 8 L 0 0 L 8 0" class="badge-hud"/>
  <path d="M {width} 8 L {width} 0 L {width-8} 0" class="badge-hud"/>
  <path d="M 0 {height-8} L 0 {height} L 8 {height}" class="badge-hud"/>
  <path d="M {width} {height-8} L {width} {height} L {width-8} {height}" class="badge-hud"/>

  <!-- Telegram Glyph -->
  <g transform="translate(18, 13)">
    <path d="M19.5 1.8L1.6 8.7C0.5 9.1 0.5 9.8 1.4 10.1L6 11.5L16.4 5C16.8 4.7 17.2 4.9 16.9 5.2L8.5 12.8L8.1 17.5C8.5 17.5 8.7 17.3 9 17L11.2 14.9L15.7 18.2C16.5 18.6 17.1 18.3 17.3 17.4L20.3 3.5C20.6 2.4 19.9 1.9 19.5 1.8Z" class="tg-icon"/>
  </g>

  <!-- Content -->
  <text x="48" y="28" class="tg-title">COMMUNICATION_LINK // TELEGRAM: <tspan fill="var(--b-accent)">@{username}</tspan></text>

  <!-- Live Status Beacon -->
  <circle cx="{width - 32}" cy="23" r="4.5" class="status-dot"/>
  <text x="{width - 45}" y="27" text-anchor="end" class="tg-meta">[ONLINE // DIRECT_DISPATCH]</text>
</svg>"""
