import xml.sax.saxutils as saxutils

def get_typing_svg(lines, color="#00FFAA"):
    if not lines:
        lines = ["..."]
        
    # --- Configuration ---
    char_width = 12.1 
    start_x = 25
    prefix = "$ "
    prefix_width = len(prefix) * char_width
    
    # Slight offset to prevent clipping of first/last characters
    clip_offset = 2 
    
    line_dur = 4.0 
    total_dur = len(lines) * line_dur
    N = len(lines)
    
    text_elements = ""
    
    for i, line in enumerate(lines):
        safe_text = saxutils.escape(line)
        line_len = len(line)
        
        f_start = i / N
        f_type_start = (i + 0.1) / N
        f_type_end = (i + 0.4) / N
        f_stay_end = (i + 0.7) / N
        f_erase_end = (i + 0.9) / N
        f_end = (i + 1.0) / N
        
        type_steps = line_len
        kt_list = [0, f_start]
        val_w_list = [0, 0]
        val_x_list = [start_x + prefix_width, start_x + prefix_width]
        
        for s in range(type_steps + 1):
            t = f_type_start + (s / type_steps) * (f_type_end - f_type_start)
            kt_list.append(t)
            # Add clip_offset only if width > 0 to prevent showing first char prematurely
            w = (s * char_width + clip_offset) if s > 0 else 0
            val_w_list.append(w)
            val_x_list.append(start_x + prefix_width + s * char_width)
            
        kt_list.append(f_stay_end)
        val_w_list.append(line_len * char_width + clip_offset)
        val_x_list.append(start_x + prefix_width + line_len * char_width)
        
        for s in range(type_steps, -1, -1):
            t = f_stay_end + ((type_steps - s) / type_steps) * (f_erase_end - f_stay_end)
            kt_list.append(t)
            w = (s * char_width + clip_offset) if s > 0 else 0
            val_w_list.append(w)
            val_x_list.append(start_x + prefix_width + s * char_width)
            
        kt_list.append(f_end)
        val_w_list.append(0)
        val_x_list.append(start_x + prefix_width)
        
        if f_end < 1.0:
            kt_list.append(1.0)
            val_w_list.append(0)
            val_x_list.append(start_x + prefix_width)
            
        kt_str = ";".join([f"{x:.4f}" for x in kt_list])
        val_w_str = ";".join([f"{x:.1f}" for x in val_w_list])
        val_x_str = ";".join([f"{x:.1f}" for x in val_x_list])
        
        text_elements += f"""
        <g class="t-line" style="animation: t-fade-{i} {total_dur}s infinite;">
            <clipPath id="t-clip-{i}">
                <rect x="{start_x + prefix_width - clip_offset}" y="0" width="0" height="70">
                    <animate attributeName="width" values="{val_w_str}" keyTimes="{kt_str}" dur="{total_dur}s" repeatCount="indefinite" calcMode="discrete" />
                </rect>
            </clipPath>
            
            <text x="{start_x}" y="52" class="t-text">
                <tspan fill-opacity="0.5">$ </tspan>
                <tspan clip-path="url(#t-clip-{i})">{safe_text}</tspan>
            </text>
            
            <!-- Cursor -->
            <rect y="32" width="12" height="24" rx="2" class="t-cursor">
                <animate attributeName="x" values="{val_x_str}" keyTimes="{kt_str}" dur="{total_dur}s" repeatCount="indefinite" calcMode="discrete" />
            </rect>
        </g>
        
        <style>
            @keyframes t-fade-{i} {{
                0%, {f_start*100}% {{ opacity: 0; visibility: hidden; }}
                {f_start*100 + 0.01}%, {f_end*100 - 0.01}% {{ opacity: 1; visibility: visible; }}
                {f_end*100}%, 100% {{ opacity: 0; visibility: hidden; }}
            }}
        </style>
        """

    return f"""<svg width="500" height="70" viewBox="0 0 500 70" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    :root {{ --bg: #0d1117; --text: {color}; --border: #30363d; }}
    @media (prefers-color-scheme: light) {{ :root {{ --bg: #ffffff; --text: #1a7f37; --border: #d0d7de; }} }}
    
    .t-container {{ fill: var(--bg); stroke: var(--border); stroke-width: 2; }}
    .t-text {{ font: bold 20px 'JetBrains Mono', monospace; fill: var(--text); }}
    .t-cursor {{ fill: var(--text); animation: t-blink 0.8s step-end infinite; }}
    
    @keyframes t-blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
  </style>
  
  <rect width="500" height="70" rx="15" class="t-container"/>
  
  <!-- Terminal dots -->
  <circle cx="25" cy="20" r="5" fill="#ff5f56"/>
  <circle cx="45" cy="20" r="5" fill="#ffbd2e"/>
  <circle cx="65" cy="20" r="5" fill="#27c93f"/>
  
  {text_elements}
</svg>"""
