import html

def get_focus_svg(color="#00FFAA"):
    # Strategic Focus Data
    focus_areas = [
        ("RE", "Reverse Engineering", "x64dbg, IDA Pro, Ghidra"),
        ("OS", "OS Internals", "Kernel Dev / Windows & Linux"),
        ("PENTEST", "Pentesting", "Infrastructure & Web Audits"),
        ("BYPASS", "Evasion", "Advanced Detection Bypass"),
        ("NET", "Networking", "Low-level Protocols & Sniffing")
    ]
    
    # Dimensions
    width = 850
    height = 180
    
    card_w = 155
    card_h = 130
    gap = 12
    
    svg_style = f"""
    <style>
        :root {{
            --f-bg: #0d1117;
            --f-accent: {color};
            --f-text: #ffffff;
            --f-secondary: #8b949e;
            --f-border: #30363d;
        }}
        @media (prefers-color-scheme: light) {{
            :root {{
                --f-bg: #ffffff;
                --f-accent: #0969da;
                --f-text: #1f2328;
                --f-secondary: #57606a;
                --f-border: #d0d7de;
            }}
        }}

        .f-card {{
            fill: var(--f-bg);
            stroke: var(--f-border);
            stroke-width: 1;
            transition: all 0.3s;
        }}
        
        .f-card:hover {{
            stroke: var(--f-accent);
        }}

        .f-tag {{
            font: bold 12px monospace;
            fill: var(--f-accent);
            letter-spacing: 1px;
        }}

        .f-title {{
            font: bold 13px 'Segoe UI', sans-serif;
            fill: var(--f-text);
        }}

        .f-desc {{
            font: 10px 'Segoe UI', sans-serif;
            fill: var(--f-secondary);
        }}

        .f-accent-line {{
            stroke: var(--f-accent);
            stroke-width: 2;
            stroke-linecap: round;
        }}

        .f-indicator {{
            fill: var(--f-accent);
            opacity: 0.3;
            animation: pulse 2s infinite ease-in-out;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 0.3; }}
            50% {{ opacity: 0.7; }}
        }}

        .f-appear {{
            opacity: 0;
            animation: f-fadeIn 0.5s forwards;
        }}

        @keyframes f-fadeIn {{
            to {{ opacity: 1; transform: translateY(0); }}
            from {{ opacity: 0; transform: translateY(10px); }}
        }}
        
        .f-corner {{ fill: var(--f-accent); }}
    </style>
    """

    cards_html = ""
    for i, (tag, title, desc) in enumerate(focus_areas):
        x = 10 + (i * (card_w + gap))
        y = 40
        delay = i * 0.1
        
        # Split description before escaping to avoid breaking entities
        desc_line1 = html.escape(desc[:25])
        desc_line2 = html.escape(desc[25:])
        
        tag_esc = html.escape(tag)
        title_esc = html.escape(title)
        
        cards_html += f"""
        <g class="f-appear" style="animation-delay: {delay}s;">
            <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="6" class="f-card"/>
            
            <!-- Corner Accent -->
            <path d="M {x} {y+15} L {x} {y} L {x+15} {y}" fill="none" stroke="{color}" stroke-width="1.5" opacity="0.6"/>
            
            <text x="{x+12}" y="{y+25}" class="f-tag">{tag_esc}</text>
            <text x="{x+12}" y="{y+48}" class="f-title">{title_esc}</text>
            
            <!-- Wrapping description -->
            <text x="{x+12}" y="{y+70}" class="f-desc">{desc_line1}</text>
            <text x="{x+12}" y="{y+85}" class="f-desc">{desc_line2}</text>
            
            <rect x="{x+12}" y="{y+110}" width="130" height="3" rx="1.5" fill="var(--f-border)"/>
            <rect x="{x+12}" y="{y+110}" width="{40 + i*15}" height="3" rx="1.5" class="f-indicator"/>
        </g>
        """

    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
    {svg_style}
    
    <text x="10" y="25" style="font: bold 16px monospace; fill: var(--f-text); letter-spacing: 2px;">STRATEGIC_FOCUS // MODULES</text>
    <line x1="10" y1="30" x2="280" y2="30" stroke="{color}" stroke-width="1" opacity="0.3"/>

    {cards_html}
</svg>"""
