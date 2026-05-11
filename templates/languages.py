def get_languages_svg(languages, color="#00FFAA"):
    bars = ""
    for i, (name, pct) in enumerate(languages[:5]):
        y_pos = 45 + (i * 32)
        grad_id = f"l-grad-{i}"
        sheen_id = f"l-sheen-{i}"
        clip_id = f"l-clip-{i}"
        
        bar_full_width = 240
        bar_filled_width = (pct / 100) * bar_full_width
        sheen_width = 100
        
        bars += f"""
        <g>
          <g class="l-item-anim" style="animation-delay: {i*0.1}s;">
            <defs>
              <linearGradient id="{grad_id}" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="var(--l-accent-light)"/>
                <stop offset="100%" stop-color="var(--l-accent)"/>
              </linearGradient>
              <linearGradient id="{sheen_id}" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="white" stop-opacity="0"/>
                <stop offset="50%" stop-color="white" stop-opacity="0.6"/>
                <stop offset="100%" stop-color="white" stop-opacity="0"/>
              </linearGradient>
              <clipPath id="{clip_id}">
                <rect x="140" y="{y_pos-10}" width="{bar_filled_width}" height="8" rx="4"/>
              </clipPath>
            </defs>

            <text x="35" y="{y_pos}" class="l-name">{name}</text>
            <text x="415" y="{y_pos}" class="l-pct" text-anchor="end">{pct}%</text>
            
            <rect x="140" y="{y_pos-10}" width="{bar_full_width}" height="8" rx="4" class="l-bar-bg"/>
            <rect x="140" y="{y_pos-10}" width="0" height="8" rx="4" fill="url(#{grad_id})" class="l-bar-fill">
              <animate attributeName="width" from="0" to="{bar_filled_width}" dur="1s" begin="{i*0.1}s" calcMode="spline" keyTimes="0; 1" keySplines="0.4 0 0.2 1" fill="freeze"/>
            </rect>
            
            <g clip-path="url(#{clip_id})">
              <rect x="140" y="{y_pos-10}" width="{sheen_width}" height="8" rx="4" fill="url(#{sheen_id})" opacity="0">
                 <animate attributeName="x" from="{140 - sheen_width}" to="{140 + bar_filled_width}" dur="2s" begin="{2 + i*0.2}s" repeatCount="indefinite" />
                 <animate attributeName="opacity" values="0;1;0" dur="2s" begin="{2 + i*0.2}s" repeatCount="indefinite" />
              </rect>
            </g>
          </g>
        </g>
        """
        
    return f"""<svg width="450" height="200" viewBox="0 0 450 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    :root {{ 
      --l-bg: #0d1117; 
      --l-accent: {color}; 
      --l-accent-light: {color}99; 
      --l-text: #c9d1d9;
      --l-grid-op: 0.05;
      --l-shadow: drop-shadow(0 0 3px {color});
    }}
    @media (prefers-color-scheme: light) {{
      :root {{ 
        --l-bg: #ffffff; 
        --l-accent: #1a7f37; 
        --l-accent-light: #2da44e; 
        --l-text: #1f2328;
        --l-grid-op: 0.1;
        --l-shadow: none;
      }}
    }}

    .l-card-bg {{ fill: var(--l-bg); stroke: #30363d; stroke-width: 2; }}
    @media (prefers-color-scheme: light) {{ .l-card-bg {{ stroke: #d0d7de; }} }}

    .l-name {{ font: bold 13px 'Segoe UI', Ubuntu, sans-serif; fill: var(--l-text); }}
    .l-pct {{ font: bold 12px 'JetBrains Mono', 'Courier New', monospace; fill: var(--l-accent); }}
    .l-bar-bg {{ fill: #161b22; opacity: 0.8; }}
    @media (prefers-color-scheme: light) {{ .l-bar-bg {{ fill: #ebedf0; opacity: 1; }} }}

    .l-bar-fill {{ filter: var(--l-shadow); }}
    .l-grid {{ stroke: var(--l-accent); opacity: var(--l-grid-op); stroke-width: 1; }}

    .l-item-anim {{ opacity: 0; animation: l-fade-in 0.5s forwards; }}
    @keyframes l-fade-in {{ from {{ opacity: 0; transform: translateX(-10px); }} to {{ opacity: 1; transform: translateX(0); }} }}
  </style>

  <rect width="450" height="200" rx="15" class="l-card-bg"/>
  
  <g class="l-grid">
    <path d="M 0 50 L 450 50 M 0 100 L 450 100 M 0 150 L 450 150" />
    <path d="M 50 0 L 50 200 M 400 0 L 400 200" />
  </g>

  {bars}
</svg>"""
