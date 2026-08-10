import random
import xml.sax.saxutils as saxutils

def get_header_svg(username, role, color="#00FFAA"):
    width = 800
    height = 200
    
    chars = ["0", "1", "⚡", "█", "👾", "{", "}", "[", "]", "<", ">", "/", "\\", "|", "-", "_", "DIR", "ROOT", "EXE", "0x", "SYS"]
    matrix_html = ""
    # Flank columns (16..200) & (600..784) to keep center clean
    flank_x_positions = list(range(16, 210, 24)) + list(range(600, 784, 24))
    
    for i in flank_x_positions:
        raw_chars = "".join(random.choice(chars) for _ in range(9))
        col_chars = saxutils.escape(raw_chars)
        delay = round(random.uniform(0, 3.5), 2)
        duration = round(random.uniform(4.5, 7.0), 2)
        font_sz = random.randint(10, 12)
        matrix_html += f"""
        <text x="{i}" y="-30" class="h-matrix-text" style="animation-delay: {delay}s; animation-duration: {duration}s; font-size: {font_sz}px;">
            {col_chars}
        </text>
        """

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="h-clip-standalone">
      <rect width="{width}" height="{height}" rx="12"/>
    </clipPath>
    <radialGradient id="h-text-shield-standalone" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="var(--h-bg)" stop-opacity="0.9"/>
      <stop offset="65%" stop-color="var(--h-bg)" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="var(--h-bg)" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="h-mask-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="var(--h-bg)" stop-opacity="1"/>
      <stop offset="18%" stop-color="var(--h-bg)" stop-opacity="0"/>
      <stop offset="82%" stop-color="var(--h-bg)" stop-opacity="0"/>
      <stop offset="100%" stop-color="var(--h-bg)" stop-opacity="1"/>
    </linearGradient>
  </defs>

  <style>
    :root {{ 
      --h-bg: #0d1117; 
      --h-text: #ffffff; 
      --h-accent: {color}; 
      --h-border: #30363d;
      --h-muted: #8b949e;
      --h-matrix-opacity: 0.22;
    }}
    @media (prefers-color-scheme: light) {{ 
      :root {{ 
        --h-bg: #ffffff; 
        --h-text: #1f2328; 
        --h-accent: #1a7f37;
        --h-border: #d0d7de;
        --h-muted: #57606a;
        --h-matrix-opacity: 0.35;
      }} 
    }}

    .h-bg {{ fill: var(--h-bg); stroke: var(--h-border); stroke-width: 1.5; }}

    .h-title {{ 
      font: bold 52px 'JetBrains Mono', 'Segoe UI', monospace; 
      fill: var(--h-accent); 
      text-transform: uppercase; 
      letter-spacing: 8px;
      animation: h-glitch 6s infinite ease-in-out;
      transform-origin: center;
    }}
    
    .h-subtitle {{ 
      font: bold 14px 'JetBrains Mono', 'Courier New', monospace; 
      fill: var(--h-text); 
      letter-spacing: 3px; 
      text-transform: uppercase;
      opacity: 0.9;
    }}

    .h-tagline {{
      font: bold 10px 'JetBrains Mono', monospace;
      fill: var(--h-muted);
      letter-spacing: 2px;
      opacity: 0.75;
    }}

    .h-matrix-text {{ 
      font: bold 12px monospace;
      fill: var(--h-accent); 
      opacity: 0; 
      writing-mode: vertical-rl; 
      animation: h-fall linear infinite; 
    }}

    @keyframes h-glitch {{
      0%, 88%, 100% {{ transform: none; opacity: 1; }}
      89% {{ transform: skew(-3deg) translate(-2px, 1px); opacity: 0.85; }}
      90% {{ transform: skew(3deg) translate(2px, -1px); opacity: 0.9; }}
      91% {{ transform: none; opacity: 1; }}
      95% {{ transform: translate(-2px, -1px); }}
      96% {{ transform: translate(2px, 1px); }}
      97% {{ transform: none; }}
    }}

    @keyframes h-fall {{ 
      0% {{ transform: translateY(-40px); opacity: 0; }} 
      15% {{ opacity: var(--h-matrix-opacity); }} 
      80% {{ opacity: var(--h-matrix-opacity); }} 
      100% {{ transform: translateY(200px); opacity: 0; }} 
    }}

    .h-scanline {{
      width: {width}px;
      height: 2px;
      fill: var(--h-accent);
      opacity: 0.08;
      animation: h-scan 4s infinite linear;
    }}
    @keyframes h-scan {{
      0% {{ transform: translateY(0); }}
      100% {{ transform: translateY(200px); }}
    }}

    .h-corner {{ stroke: var(--h-accent); stroke-width: 2; fill: none; opacity: 0.8; stroke-linecap: square; }}
    .h-reticle {{ stroke: var(--h-muted); stroke-width: 1; opacity: 0.4; }}
  </style>

  <rect width="{width}" height="{height}" rx="12" class="h-bg"/>
  
  <g clip-path="url(#h-clip-standalone)">
    <g opacity="1">{matrix_html}</g>
    <rect class="h-scanline" />
  </g>
  
  <rect width="{width}" height="{height}" fill="url(#h-mask-grad)" pointer-events="none"/>
  <ellipse cx="{width/2}" cy="115" rx="280" ry="65" fill="url(#h-text-shield-standalone)" pointer-events="none"/>

  <!-- Main Content -->
  <text x="{width/2}" y="95" text-anchor="middle" dominant-baseline="middle" class="h-title">{username}</text>
  <text x="{width/2}" y="142" text-anchor="middle" class="h-subtitle">{role}</text>
  <text x="{width/2}" y="168" text-anchor="middle" class="h-tagline">[ ARCH: x86_64 // ARM64 // WIN_NT // LINUX_KERNEL ]</text>

  <!-- Precision Corner Accents -->
  <path d="M 28 12 L 12 12 L 12 28" class="h-corner" />
  <path d="M {width-28} 12 L {width-12} 12 L {width-12} 28" class="h-corner" />
  <path d="M 28 {height-12} L 12 {height-12} L 12 {height-28}" class="h-corner" />
  <path d="M {width-28} {height-12} L {width-12} {height-12} L {width-12} {height-28}" class="h-corner" />
  
  <!-- Center Crosshairs -->
  <path d="M {width/2 - 5} 100 L {width/2 + 5} 100 M {width/2} 95 L {width/2} 105" class="h-reticle" opacity="0.2"/>
</svg>"""
