def get_scanner_svg(calendar, color="#00FFAA"):
    # --- Configuration ---
    cell_size, gap = 10, 3
    step = cell_size + gap
    pad_x, pad_y = 20, 25
    weeks = calendar[-52:]
    num_weeks = len(weeks)
    
    width = pad_x * 2 + num_weeks * step
    height = pad_y + 7 * step + 15
    grid_width = (num_weeks - 1) * step
    grid_height = 7 * step - gap
    
    # Timing
    total_dur = 12.0
    scan_dur = 4.0
    
    dark_c = ["#161b22", "#0e4429", "#006d3a", "#26a641", "#39d353"]
    light_c = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
    
    grid_html = ""
    for x, week in enumerate(weeks):
        col_ratio = x / (num_weeks - 1) if num_weeks > 1 else 0
        delay = col_ratio * scan_dur
        
        for y, day in enumerate(week["contributionDays"]):
            count = day["contributionCount"]
            level = 0
            if count > 0:
                if count < 5: level = 1
                elif count < 10: level = 2
                elif count < 20: level = 3
                else: level = 4
            
            px, py = pad_x + x * step, pad_y + y * step
            grid_html += f'<rect x="{px}" y="{py}" width="{cell_size}" height="{cell_size}" rx="2" class="sc-cell sc-l-{level}" style="animation-delay: {delay:.3f}s;"/>\n'

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sc-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{color}" stop-opacity="0" />
      <stop offset="100%" stop-color="{color}" stop-opacity="0.6" />
    </linearGradient>
  </defs>
  <style>
    .sc-bg {{ fill: #0d1117; }}
    .sc-border {{ stroke: #30363d; }}
    .sc-cell {{ fill: #161b22; opacity: 0.15; }}
    
    /* REVEAL KEYFRAMES: Gradient Cooling Trail */
    .sc-l-0 {{ animation: sc-rev-0 {total_dur}s infinite; }}
    .sc-l-1 {{ animation: sc-rev-1 {total_dur}s infinite; }}
    .sc-l-2 {{ animation: sc-rev-2 {total_dur}s infinite; }}
    .sc-l-3 {{ animation: sc-rev-3 {total_dur}s infinite; }}
    .sc-l-4 {{ animation: sc-rev-4 {total_dur}s infinite; }}

    @keyframes sc-rev-0 {{
      0% {{ fill: #fff; opacity: 1; filter: drop-shadow(0 0 6px {color}); }}
      1% {{ fill: {color}; opacity: 0.8; filter: drop-shadow(0 0 4px {color}); }}
      3% {{ fill: {color}; opacity: 0.4; filter: drop-shadow(0 0 2px {color}); }}
      5%, 100% {{ fill: #161b22; opacity: 0.15; filter: none; }}
    }}
    
    /* Multistage gradient cooling for contribution levels */
    @keyframes sc-rev-1 {{ 
      0% {{ fill: #fff; opacity: 1; filter: brightness(2) drop-shadow(0 0 10px {color}); }} 
      2% {{ fill: #fff; opacity: 1; filter: brightness(1.5) drop-shadow(0 0 8px {color}); }}
      4% {{ fill: {color}; opacity: 1; filter: drop-shadow(0 0 6px {color}); }}
      6% {{ fill: {dark_c[1]}; opacity: 1; filter: drop-shadow(0 0 4px {dark_c[1]}); }}
      10%, 75% {{ fill: {dark_c[1]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: #161b22; opacity: 0.15; }} 
    }}
    @keyframes sc-rev-2 {{ 
      0% {{ fill: #fff; opacity: 1; filter: brightness(2) drop-shadow(0 0 10px {color}); }} 
      2% {{ fill: #fff; opacity: 1; filter: brightness(1.5) drop-shadow(0 0 8px {color}); }}
      4% {{ fill: {color}; opacity: 1; filter: drop-shadow(0 0 6px {color}); }}
      6% {{ fill: {dark_c[2]}; opacity: 1; filter: drop-shadow(0 0 4px {dark_c[2]}); }}
      10%, 75% {{ fill: {dark_c[2]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: #161b22; opacity: 0.15; }} 
    }}
    @keyframes sc-rev-3 {{ 
      0% {{ fill: #fff; opacity: 1; filter: brightness(2) drop-shadow(0 0 10px {color}); }} 
      2% {{ fill: #fff; opacity: 1; filter: brightness(1.5) drop-shadow(0 0 8px {color}); }}
      4% {{ fill: {color}; opacity: 1; filter: drop-shadow(0 0 6px {color}); }}
      6% {{ fill: {dark_c[3]}; opacity: 1; filter: drop-shadow(0 0 4px {dark_c[3]}); }}
      10%, 75% {{ fill: {dark_c[3]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: #161b22; opacity: 0.15; }} 
    }}
    @keyframes sc-rev-4 {{ 
      0% {{ fill: #fff; opacity: 1; filter: brightness(2) drop-shadow(0 0 10px {color}); }} 
      2% {{ fill: #fff; opacity: 1; filter: brightness(1.5) drop-shadow(0 0 8px {color}); }}
      4% {{ fill: {color}; opacity: 1; filter: drop-shadow(0 0 6px {color}); }}
      6% {{ fill: {dark_c[4]}; opacity: 1; filter: drop-shadow(0 0 4px {dark_c[4]}); }}
      10%, 75% {{ fill: {dark_c[4]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: #161b22; opacity: 0.15; }} 
    }}

    @media (prefers-color-scheme: light) {{
      .sc-bg {{ fill: #ffffff; }}
      .sc-border {{ stroke: #d0d7de; }}
      .sc-cell {{ fill: {light_c[0]}; opacity: 1; }}
      .sc-l-0 {{ animation: sc-rev-l0 {total_dur}s infinite; }}
      .sc-l-1 {{ animation: sc-rev-l1 {total_dur}s infinite; }}
      .sc-l-2 {{ animation: sc-rev-l2 {total_dur}s infinite; }}
      .sc-l-3 {{ animation: sc-rev-l3 {total_dur}s infinite; }}
      .sc-l-4 {{ animation: sc-rev-l4 {total_dur}s infinite; }}
    }}
    
    @keyframes sc-rev-l0 {{ 
      0% {{ fill: #fff; opacity: 1; filter: drop-shadow(0 0 8px {color}); }} 
      2% {{ fill: {color}; opacity: 0.8; filter: drop-shadow(0 0 4px {color}); }} 
      5%, 100% {{ fill: {light_c[0]}; opacity: 1; filter: none; }} 
    }}
    @keyframes sc-rev-l1 {{ 
      0% {{ fill: #fff; opacity: 1; filter: drop-shadow(0 0 10px {color}); }} 
      3% {{ fill: {color}; opacity: 0.8; filter: drop-shadow(0 0 6px {color}); }} 
      8%, 75% {{ fill: {light_c[1]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: {light_c[0]}; opacity: 1; }} 
    }}
    @keyframes sc-rev-l2 {{ 
      0% {{ fill: #fff; opacity: 1; filter: drop-shadow(0 0 10px {color}); }} 
      3% {{ fill: {color}; opacity: 0.8; filter: drop-shadow(0 0 6px {color}); }} 
      8%, 75% {{ fill: {light_c[2]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: {light_c[0]}; opacity: 1; }} 
    }}
    @keyframes sc-rev-l3 {{ 
      0% {{ fill: #fff; opacity: 1; filter: drop-shadow(0 0 10px {color}); }} 
      3% {{ fill: {color}; opacity: 0.8; filter: drop-shadow(0 0 6px {color}); }} 
      8%, 75% {{ fill: {light_c[3]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: {light_c[0]}; opacity: 1; }} 
    }}
    @keyframes sc-rev-l4 {{ 
      0% {{ fill: #fff; opacity: 1; filter: drop-shadow(0 0 10px {color}); }} 
      3% {{ fill: {color}; opacity: 0.8; filter: drop-shadow(0 0 6px {color}); }} 
      8%, 75% {{ fill: {light_c[4]}; opacity: 1; filter: none; }} 
      85%, 100% {{ fill: {light_c[0]}; opacity: 1; }} 
    }}

    /* BEAM */
    @keyframes sc-beam-move {{
      0% {{ transform: translateX(0); opacity: 0; }}
      1% {{ opacity: 1; }}
      32% {{ opacity: 1; }}
      33.3% {{ transform: translateX({grid_width}px); opacity: 0; }}
      100% {{ transform: translateX({grid_width}px); opacity: 0; }}
    }}
    .sc-beam {{ animation: sc-beam-move {total_dur}s infinite linear; }}
  </style>

  <rect width="{width}" height="{height}" rx="12" class="sc-bg sc-border" stroke-width="1.5"/>
  
  <g id="sc-grid">
    {grid_html}
  </g>

  <g transform="translate({pad_x}, {pad_y})">
    <g class="sc-beam">
      <rect fill="url(#sc-grad)" x="-30" y="0" width="30" height="{grid_height}" />
      <rect fill="#fff" x="-1" y="0" width="2" height="{grid_height}" rx="1" />
      <circle fill="{color}" cx="0" cy="0" r="3" />
      <circle fill="{color}" cx="0" cy="{grid_height}" r="3" />
    </g>
  </g>
</svg>"""
