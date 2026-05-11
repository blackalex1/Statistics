def get_matrix_svg(calendar, color="#00FFAA"):
    cell_size, gap = 10, 3
    step = cell_size + gap
    pad_x, pad_y = 20, 25
    weeks = calendar[-52:]
    num_weeks = len(weeks)
    width = pad_x * 2 + num_weeks * step
    height = pad_y + 7 * step + 15
    rain_dur = 5.0
    total_dur = 11.0
    
    import random
    random.seed(42)
    
    grid_html = ""
    for x, week in enumerate(weeks):
        col_delay = random.uniform(0, rain_dur - 1.0)
        for y, day in enumerate(week["contributionDays"]):
            count = day["contributionCount"]
            level = 0
            if count > 0:
                if count < 5: level = 1
                elif count < 10: level = 2
                elif count < 20: level = 3
                else: level = 4
            px, py = pad_x + x * step, pad_y + y * step
            hit_time = col_delay + (y / 7) * 0.8
            neg_delay = hit_time - 4.4 
            cell_class = f"cell active l-{level}" if level > 0 else "cell empty"
            grid_html += f"""
            <rect x="{px}" y="{py}" width="{cell_size}" height="{cell_size}" rx="2" 
                  fill="#161b22" class="{cell_class}" 
                  style="animation-delay: {neg_delay:.3f}s;"/>
            """

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    :root {{
      --bg: #0d1117;
      --border: #30363d;
      --accent: {color};
      --c0: #161b22;
      --c1: #0e4429; --c2: #006d3a; --c3: #26a641; --c4: #39d353;
      --f0: #2ea043; --f1: #00ff77; --f2: #44ffaa; --f3: #aaffdd; --f4: #ffffff;
      --cell-op: 0.15;
    }}
    @media (prefers-color-scheme: light) {{
      :root {{
        --bg: #ffffff;
        --border: #d0d7de;
        --c0: #ebedf0;
        --c1: #9be9a8; --c2: #40c463; --c3: #30a14e; --c4: #216e39;
        --f0: #40c463; --f1: #30a14e; --f2: #216e39; --f3: #1a4a2b; --f4: #12331c;
        --cell-op: 0.5;
      }}
    }}
    .bg {{ fill: var(--bg); }}
    @keyframes matrix-cycle {{
      0%, 39.9% {{ fill: var(--c0); opacity: var(--cell-op); filter: none; }}
      40% {{ fill: var(--flash); opacity: 1; filter: brightness(1.4) drop-shadow(0 0 6px var(--flash)); }}
      45%, 85% {{ fill: var(--target); opacity: 1; filter: none; }}
      95%, 100% {{ fill: var(--c0); opacity: var(--cell-op); }}
    }}
    .cell {{ fill: var(--c0); opacity: var(--cell-op); }}
    .active {{ animation: matrix-cycle {total_dur}s infinite linear; }}
    .empty {{ --target: var(--c0); --flash: var(--f0); animation: matrix-cycle {total_dur}s infinite linear; }}
    .l-1 {{ --target: var(--c1); --flash: var(--f1); }}
    .l-2 {{ --target: var(--c2); --flash: var(--f2); }}
    .l-3 {{ --target: var(--c3); --flash: var(--f3); }}
    .l-4 {{ --target: var(--c4); --flash: var(--f4); }}
  </style>
  <rect width="{width}" height="{height}" rx="12" class="bg" stroke="var(--border)" stroke-width="1.5"/>
  <g> {grid_html} </g>
</svg>"""
