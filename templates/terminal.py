def get_terminal_svg(data, color="#00FFAA"):
    # data format: {"role": "...", "focus": "...", "system": "...", "mindset": "..."}
    width = 600
    height = 200
    
    # CSS Variables and Styles
    # We include light mode support as well
    svg_style = f"""
    <style>
        :root {{
            --term-bg: #0d1117;
            --term-accent: {color};
            --term-text: #ffffff;
            --term-secondary: #8b949e;
            --term-border: #30363d;
        }}
        @media (prefers-color-scheme: light) {{
            :root {{
                --term-bg: #f6f8fa;
                --term-accent: #1a7f37;
                --term-text: #1f2328;
                --term-secondary: #57606a;
                --term-border: #d0d7de;
            }}
        }}

        .terminal-window {{
            fill: var(--term-bg);
            stroke: var(--term-border);
            stroke-width: 1.5;
        }}
        
        .title-bar {{
            fill: var(--term-border);
            opacity: 0.5;
        }}

        .dot {{ r: 3; }}
        .dot-red {{ fill: #ff5f56; }}
        .dot-yellow {{ fill: #ffbd2e; }}
        .dot-green {{ fill: #27c93f; }}

        .label {{
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 14px;
            font-weight: bold;
            fill: var(--term-text);
        }}

        .value {{
            font-family: 'Fira Code', 'Courier New', monospace;
            font-size: 14px;
            fill: var(--term-accent);
        }}

        .cursor {{
            fill: var(--term-accent);
            animation: blink 1s infinite step-end;
        }}

        @keyframes blink {{
            from, to {{ opacity: 1; }}
            50% {{ opacity: 0; }}
        }}

        .glow {{
            filter: drop-shadow(0 0 3px var(--term-accent));
        }}

        .line-appear {{
            opacity: 0;
            animation: fadeIn 0.5s forwards;
        }}
        
        @keyframes fadeIn {{
            to {{ opacity: 1; }}
        }}
    </style>
    """

    content_html = ""
    y_start = 65
    line_height = 28
    
    lines = [
        ("$ role", data.get("role", "")),
        ("$ focus", data.get("focus", "")),
        ("$ system", data.get("system", "")),
        ("$ mindset", data.get("mindset", ""))
    ]

    for i, (label, value) in enumerate(lines):
        y = y_start + (i * line_height)
        delay = i * 0.2
        content_html += f"""
        <g class="line-appear" style="animation-delay: {delay}s;">
            <text x="35" y="{y}" class="label">{label}</text>
            <text x="130" y="{y}" class="value glow">{value}</text>
        </g>
        """
    
    # Add a blinking cursor after the last line
    cursor_x = 130 + (len(lines[-1][1]) * 8.5) # Approximate character width
    cursor_y = y_start + (len(lines) - 1) * line_height - 12
    
    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
    {svg_style}
    
    <rect width="{width}" height="{height}" rx="10" class="terminal-window"/>
    <path d="M0 10 C0 4.47715 4.47715 0 10 0 H590 C595.523 0 600 4.47715 600 10 V30 H0 V10 Z" class="title-bar"/>
    
    <circle cx="20" cy="15" class="dot dot-red"/>
    <circle cx="35" cy="15" class="dot dot-yellow"/>
    <circle cx="50" cy="15" class="dot dot-green"/>
    <text x="300" y="20" text-anchor="middle" style="font-family: monospace; font-size: 10px; fill: var(--term-secondary);">system_info — bash</text>

    {content_html}
    
    <rect x="{cursor_x}" y="{cursor_y}" width="8" height="15" class="cursor" style="animation-delay: {len(lines) * 0.2}s;"/>
</svg>"""
