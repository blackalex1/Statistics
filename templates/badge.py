def get_contact_badge_svg(username="blackalex1", color="#00FFAA"):
    width = 250
    height = 50
    
    svg_style = f"""
    <style>
        :root {{
            --b-bg: #0d1117;
            --b-accent: {color};
            --b-text: #ffffff;
            --b-border: #30363d;
        }}
        @media (prefers-color-scheme: light) {{
            :root {{
                --b-bg: #ffffff;
                --b-accent: #0969da;
                --b-text: #1f2328;
                --b-border: #d0d7de;
            }}
        }}

        .badge-rect {{
            fill: var(--b-bg);
            stroke: var(--b-accent);
            stroke-width: 1.5;
            transition: all 0.3s;
        }}

        .badge-text {{
            font: bold 14px monospace;
            fill: var(--b-text);
            letter-spacing: 2px;
            text-transform: uppercase;
        }}

        .badge-sub {{
            font: bold 10px monospace;
            fill: var(--b-accent);
            letter-spacing: 1px;
            opacity: 0.8;
        }}

        .glow {{
            filter: drop-shadow(0 0 4px var(--b-accent));
        }}

        .tg-icon {{
            fill: var(--b-accent);
        }}

        .corner {{
            fill: var(--b-accent);
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 0.8; transform: scale(1); }}
            50% {{ opacity: 1; transform: scale(1.05); }}
        }}

        .online-dot {{
            fill: {color};
            animation: pulse 2s infinite ease-in-out;
        }}
    </style>
    """

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
    {svg_style}
    
    <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="6" class="badge-rect"/>
    
    <!-- Telegram Icon (Simplified) -->
    <path d="M25 25 L40 18 L37 32 L31 29 L28 32 L25 25 Z" class="tg-icon glow"/>
    <path d="M40 18 L31 29 L25 25" fill="none" stroke="var(--b-bg)" stroke-width="1"/>

    <text x="60" y="24" class="badge-text">TELEGRAM</text>
    <text x="60" y="38" class="badge-sub">@{username}</text>
    
    <!-- Online Status Indicator -->
    <circle cx="{width - 25}" cy="25" r="4" class="online-dot glow"/>
    
    <!-- Corner Accents -->
    <path d="M 5 12 L 5 5 L 12 5" fill="none" stroke="{color}" stroke-width="2"/>
    <path d="M {width-5} {height-12} L {width-5} {height-5} L {width-12} {height-5}" fill="none" stroke="{color}" stroke-width="2"/>
</svg>"""
