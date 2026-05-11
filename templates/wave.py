def get_wave_svg(calendar, color="#00FFAA"):
    # --- Configuration ---
    cell_size, gap = 10, 3
    step = cell_size + gap
    pad_x, pad_y = 30, 40
    weeks = calendar[-52:]
    num_weeks = len(weeks)
    
    width = pad_x * 2 + num_weeks * step
    height = pad_y * 2 + 7 * step
    
    # Timing: 4s wave, 4s pause
    total_dur = 8.0
    wave_dur = 4.0
    
    dark_c = ["#161b22", "#0e4429", "#006d3a", "#26a641", "#39d353"]
    light_c = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
    
    grid_html = ""
    for x, week in enumerate(weeks):
        col_ratio = x / (num_weeks - 1) if num_weeks > 1 else 0
        delay = col_ratio * wave_dur
        
        for y, day in enumerate(week["contributionDays"]):
            count = day["contributionCount"]
            level = 0
            if count > 0:
                if count < 5: level = 1
                elif count < 10: level = 2
                elif count < 20: level = 3
                else: level = 4
            
            px, py = pad_x + x * step, pad_y + y * step
            grid_html += f'<rect x="{px}" y="{py}" width="{cell_size}" height="{cell_size}" rx="2" class="wv-cell wv-l-{level}" style="animation-delay: {delay:.3f}s;"/>\n'

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .wv-bg {{ fill: #0d1117; }}
    .wv-border {{ stroke: #30363d; }}
    .wv-cell {{ fill: #161b22; transform-origin: center; transform-box: fill-box; }}
    
    /* DARK THEME ANIMATIONS */
    .wv-l-0 {{ animation: wv-jump-0 {total_dur}s infinite cubic-bezier(0.4, 0, 0.2, 1); }}
    .wv-l-1 {{ animation: wv-jump-1 {total_dur}s infinite cubic-bezier(0.4, 0, 0.2, 1); }}
    .wv-l-2 {{ animation: wv-jump-2 {total_dur}s infinite cubic-bezier(0.4, 0, 0.2, 1); }}
    .wv-l-3 {{ animation: wv-jump-3 {total_dur}s infinite cubic-bezier(0.4, 0, 0.2, 1); }}
    .wv-l-4 {{ animation: wv-jump-4 {total_dur}s infinite cubic-bezier(0.4, 0, 0.2, 1); }}

    @keyframes wv-jump-0 {{
      0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: #161b22; }}
      12.5% {{ transform: translateY(-8px) scale(1.2); fill: {color}; filter: drop-shadow(0 0 5px {color}); }}
    }}
    @keyframes wv-jump-1 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {dark_c[1]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: #fff; filter: drop-shadow(0 0 8px {color}); }} }}
    @keyframes wv-jump-2 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {dark_c[2]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: #fff; filter: drop-shadow(0 0 8px {color}); }} }}
    @keyframes wv-jump-3 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {dark_c[3]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: #fff; filter: drop-shadow(0 0 8px {color}); }} }}
    @keyframes wv-jump-4 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {dark_c[4]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: #fff; filter: drop-shadow(0 0 8px {color}); }} }}

    @media (prefers-color-scheme: light) {{
      .wv-bg {{ fill: #ffffff; }}
      .wv-border {{ stroke: #d0d7de; }}
      .wv-cell {{ fill: #ebedf0; }}
      .wv-l-0 {{ animation-name: wv-jump-l0; }}
      .wv-l-1 {{ animation-name: wv-jump-l1; }}
      .wv-l-2 {{ animation-name: wv-jump-l2; }}
      .wv-l-3 {{ animation-name: wv-jump-l3; }}
      .wv-l-4 {{ animation-name: wv-jump-l4; }}
    }}
    
    @keyframes wv-jump-l0 {{
      0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: #ebedf0; }}
      12.5% {{ transform: translateY(-8px) scale(1.2); fill: {color}; filter: drop-shadow(0 0 5px {color}); }}
    }}
    @keyframes wv-jump-l1 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {light_c[1]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: {color}; filter: drop-shadow(0 0 8px {color}); }} }}
    @keyframes wv-jump-l2 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {light_c[2]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: {color}; filter: drop-shadow(0 0 8px {color}); }} }}
    @keyframes wv-jump-l3 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {light_c[3]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: {color}; filter: drop-shadow(0 0 8px {color}); }} }}
    @keyframes wv-jump-l4 {{ 0%, 25%, 100% {{ transform: translateY(0) scale(1); fill: {light_c[4]}; }} 12.5% {{ transform: translateY(-12px) scale(1.3); fill: {color}; filter: drop-shadow(0 0 8px {color}); }} }}
  </style>

  <rect width="{width}" height="{height}" rx="12" class="wv-bg wv-border" stroke-width="1.5"/>
  <g id="wv-grid">
    {grid_html}
  </g>
</svg>"""
