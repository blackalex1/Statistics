def get_activity_graph_svg(calendar, color="#00FFAA"):
    # --- Data Processing ---
    # Flatten the last ~35 days to ensure we have a full month trend
    all_days = []
    for week in calendar[-6:]:
        for day in week["contributionDays"]:
            all_days.append(day)
    
    # Take last 30 days for a focused view
    recent_days = all_days[-30:]
    num_points = len(recent_days)
    
    # --- Dimensions & Scaling ---
    width = 850
    height = 300
    pad_l, pad_r = 50, 40
    pad_t, pad_b = 70, 60
    
    graph_w = width - pad_l - pad_r
    graph_h = height - pad_t - pad_b
    
    counts = [d["contributionCount"] for d in recent_days]
    max_count = max(counts) if counts else 0
    # Determine Y-axis limit (rounded up for clean grid)
    if max_count <= 5: y_limit = 10
    elif max_count <= 10: y_limit = 15
    elif max_count <= 25: y_limit = 30
    else: y_limit = ((max_count // 10) + 1) * 10
    
    def get_x(i):
        return pad_l + (i * (graph_w / (num_points - 1)))
    
    def get_y(count):
        return pad_t + graph_h - (count * (graph_h / y_limit))

    # --- Points Calculation ---
    points = []
    for i, day in enumerate(recent_days):
        points.append((get_x(i), get_y(day["contributionCount"])))

    # --- Path Construction (Smooth Curves) ---
    # We'll use Cubic Bezier curves with control points halfway between nodes
    if not points: return ""
    
    line_path = f"M {points[0][0]},{points[0][1]}"
    for i in range(len(points) - 1):
        p0 = points[i]
        p1 = points[i+1]
        # Control points are placed horizontally to create a smooth wave
        cp1_x = p0[0] + (p1[0] - p0[0]) / 2
        cp2_x = p0[0] + (p1[0] - p0[0]) / 2
        line_path += f" C {cp1_x},{p0[1]} {cp2_x},{p1[1]} {p1[0]},{p1[1]}"

    # Area path (closed loop back to baseline)
    area_path = line_path + f" L {points[-1][0]},{pad_t + graph_h} L {points[0][0]},{pad_t + graph_h} Z"

    # --- Grid & Labels ---
    grid_html = ""
    # Horizontal grid lines (3 levels)
    for val in [0, y_limit // 2, y_limit]:
        y = get_y(val)
        grid_html += f'<line x1="{pad_l}" y1="{y}" x2="{width - pad_r}" y2="{y}" class="grid-line" />'
        grid_html += f'<text x="{pad_l - 12}" y="{y + 4}" class="axis-label" text-anchor="end">{val}</text>'

    # Vertical grid & Date labels
    for i in range(0, num_points, 5):
        x = get_x(i)
        grid_html += f'<line x1="{x}" y1="{pad_t}" x2="{x}" y2="{pad_t + graph_h}" class="grid-line" />'
        date_day = recent_days[i]["date"].split("-")[-1]
        grid_html += f'<text x="{x}" y="{height - 35}" class="axis-label" text-anchor="middle">{date_day}</text>'

    # --- Data Points (Dots) ---
    dots_html = ""
    for i, (px, py) in enumerate(points):
        delay = (i / num_points) * 0.8
        dots_html += f'<circle cx="{px}" cy="{py}" r="3.5" fill="white" class="dot" style="animation-delay: {delay}s;"/>'

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="areaGradient" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    :root {{ 
      --bg: #0d1117; 
      --accent: {color}; 
      --text: #8b949e;
      --title-text: {color};
    }}
    @media (prefers-color-scheme: light) {{
      :root {{ 
        --bg: #ffffff; 
        --accent: #0969da; 
        --text: #57606a;
        --title-text: #1f2328;
      }}
    }}

    .bg {{ fill: var(--bg); stroke: #30363d; stroke-width: 1; }}
    .grid-line {{ stroke: var(--text); stroke-opacity: 0.15; stroke-width: 1; stroke-dasharray: 3,3; }}
    .axis-label {{ fill: var(--text); font-family: 'Segoe UI', Tahoma, sans-serif; font-size: 11px; }}
    .title {{ fill: var(--title-text); font-family: 'Segoe UI', Tahoma, sans-serif; font-size: 18px; font-weight: bold; }}
    
    .trend-line {{ 
      stroke: var(--accent); 
      stroke-width: 3; 
      fill: none; 
      filter: url(#glow);
      stroke-dasharray: 2000;
      stroke-dashoffset: 2000;
      animation: drawLine 2s forwards ease-in-out;
    }}
    
    .trend-area {{ 
      fill: url(#areaGradient); 
      opacity: 0;
      animation: fadeIn 1.5s 0.5s forwards;
    }}

    .dot {{ 
      opacity: 0; 
      animation: fadeIn 0.3s forwards;
      stroke: var(--accent);
      stroke-width: 1;
    }}

    @keyframes drawLine {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
  </style>

  <rect width="{width}" height="{height}" rx="12" class="bg"/>
  
  <text x="30" y="40" class="title">Activity Trends</text>
  <text x="{width - 30}" y="40" class="axis-label" text-anchor="end">Last 30 Days</text>
  
  <g class="grid">
    {grid_html}
  </g>

  <path d="{area_path}" class="trend-area"/>
  <path d="{line_path}" class="trend-line"/>
  
  <g class="dots">
    {dots_html}
  </g>
</svg>"""
