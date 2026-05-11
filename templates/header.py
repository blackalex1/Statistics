import random
import xml.sax.saxutils as saxutils

def get_header_svg(username, role, color="#00FFAA"):
    # Matrix rain configuration
    chars = ["0", "1", "⚡", "█", "👾", "{", "}", "[", "]", "<", ">", "/", "\\", "|", "-", "_", "DIR", "ROOT", "EXE"]
    matrix_html = ""
    for i in range(0, 800, 30):
        raw_chars = "".join(random.choice(chars) for _ in range(12))
        col_chars = saxutils.escape(raw_chars)
        delay = random.uniform(0, 5)
        duration = random.uniform(4, 10)
        matrix_html += f"""
        <text x="{i}" y="-50" class="h-matrix-text" style="animation-delay: {delay}s; animation-duration: {duration}s; font-size: {random.randint(8, 14)}px;">
            {col_chars}
        </text>
        """

    return f"""<svg width="800" height="200" viewBox="0 0 800 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    :root {{ 
      --h-bg: #0d1117; 
      --h-text: #ffffff; 
      --h-accent: {color}; 
      --h-matrix-opacity: 0.25;
    }}
    @media (prefers-color-scheme: light) {{ 
      :root {{ 
        --h-bg: #ffffff; 
        --h-text: #1f2328; 
        --h-accent: #1a7f37;
        --h-matrix-opacity: 0.4;
      }} 
      .h-title {{ filter: none !important; }}
    }}

    .h-bg {{ fill: var(--h-bg); }}

    .h-title {{ 
      font: bold 52px 'Segoe UI', Ubuntu, sans-serif; 
      fill: var(--h-accent); 
      text-transform: uppercase; 
      letter-spacing: 8px;
      animation: h-glitch 5s infinite;
      transform-origin: center;
    }}
    
    .h-subtitle {{ 
      font: bold 16px 'Courier New', monospace; 
      fill: var(--h-text); 
      letter-spacing: 3px; 
      text-transform: uppercase;
      opacity: 0.8;
    }}

    .h-matrix-text {{ 
      font: bold 12px monospace;
      fill: var(--h-accent); 
      opacity: 0; 
      writing-mode: vertical-rl; 
      animation: h-fall linear infinite; 
    }}

    /* REFINED GLITCH: Softened collapse, intensified color split */
    @keyframes h-glitch {{
      0%, 80%, 100% {{ transform: none; opacity: 1; text-shadow: 0 0 8px var(--h-accent); }}
      81% {{ transform: skew(-5deg) translate(-5px, 2px); text-shadow: 3px 0 #ff00c1, -3px 0 #00fff9; opacity: 0.8; }}
      82% {{ transform: skew(5deg) translate(5px, -2px); text-shadow: -3px 0 #ff00c1, 3px 0 #00fff9; opacity: 0.9; }}
      83% {{ transform: none; text-shadow: 0 0 8px var(--h-accent); }}
      84% {{ transform: scaleY(0.7) skewX(10deg); opacity: 0.7; text-shadow: 4px 0 #ff00c1, -4px 0 #00fff9; }}
      85% {{ transform: none; opacity: 1; }}
      92% {{ transform: translate(-4px, -2px); text-shadow: 5px 0 red, -5px 0 blue; }}
      94% {{ transform: translate(4px, 2px); text-shadow: -5px 0 red, 5px 0 blue; }}
      96% {{ transform: none; text-shadow: 0 0 8px var(--h-accent); }}
    }}

    @keyframes h-fall {{ 
      0% {{ transform: translateY(-100px); opacity: 0; }} 
      10% {{ opacity: var(--h-matrix-opacity); }} 
      90% {{ opacity: var(--h-matrix-opacity); }} 
      100% {{ transform: translateY(300px); opacity: 0; }} 
    }}

    .h-scanline {{
      width: 800px;
      height: 2px;
      fill: var(--h-accent);
      opacity: 0.08;
      animation: h-scan 3s infinite linear;
    }}
    @keyframes h-scan {{
      0% {{ transform: translateY(0); }}
      100% {{ transform: translateY(200px); }}
    }}

    .h-corner {{ stroke: var(--h-accent); stroke-width: 2.5; fill: none; opacity: 0.6; stroke-linecap: square; }}
  </style>

  <rect width="800" height="200" rx="15" class="h-bg"/>
  
  <g opacity="1">{matrix_html}</g>
  <rect class="h-scanline" />
  
  <defs>
    <linearGradient id="h-mask-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="var(--h-bg)" stop-opacity="1"/>
      <stop offset="20%" stop-color="var(--h-bg)" stop-opacity="0"/>
      <stop offset="80%" stop-color="var(--h-bg)" stop-opacity="0"/>
      <stop offset="100%" stop-color="var(--h-bg)" stop-opacity="1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#h-mask-grad)" pointer-events="none"/>

  <!-- Main Content -->
  <text x="400" y="90" text-anchor="middle" dominant-baseline="middle" class="h-title">{username}</text>
  <text x="400" y="140" text-anchor="middle" class="h-subtitle">{role}</text>

  <!-- Corner Accents -->
  <path d="M 30 10 L 10 10 L 10 30" class="h-corner" />
  <path d="M 770 10 L 790 10 L 790 30" class="h-corner" />
  <path d="M 30 190 L 10 190 L 10 170" class="h-corner" />
  <path d="M 770 190 L 790 190 L 790 170" class="h-corner" />
</svg>"""
