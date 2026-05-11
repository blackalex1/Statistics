import xml.sax.saxutils as saxutils
import time

def get_typing_svg(lines, color="#00FFAA"):
    if not lines:
        lines = ["..."]
        
    # --- Configuration ---
    char_width = 12.1 
    start_x = 25
    prefix = "$ "
    prefix_width = len(prefix) * char_width
    clip_offset = 2 
    line_dur = 4.0 
    total_dur = len(lines) * line_dur
    N = len(lines)
    
    # Use a unique ID suffix to prevent conflicts if multiple SVGs are on one page
    uid = int(time.time()) % 10000
    
    content = ""
    all_defs = ""
    
    for i, line in enumerate(lines):
        safe_text = saxutils.escape(line)
        line_len = len(line)
        
        # Timing fractions
        f_start = i / N
        f_type_start = (i + 0.05) / N
        f_type_end = (i + 0.45) / N
        f_stay_end = (i + 0.75) / N
        f_erase_end = (i + 0.95) / N
        f_end = (i + 1.0) / N
        
        # Build animation sequences (ensure strictly increasing keyTimes)
        kt_list = [0, f_start]
        val_w_list = [0, 0]
        val_x_list = [start_x + prefix_width, start_x + prefix_width]
        
        # Typing phase
        type_steps = max(1, line_len)
        for s in range(1, type_steps + 1):
            t = f_type_start + (s / type_steps) * (f_type_end - f_type_start)
            kt_list.append(t)
            w = s * char_width + clip_offset
            val_w_list.append(w)
            val_x_list.append(start_x + prefix_width + s * char_width)
            
        # Stay phase
        if f_stay_end > kt_list[-1]:
            kt_list.append(f_stay_end)
            val_w_list.append(line_len * char_width + clip_offset)
            val_x_list.append(start_x + prefix_width + line_len * char_width)
        
        # Erasing phase
        for s in range(type_steps - 1, -1, -1):
            t = f_stay_end + ((type_steps - s) / type_steps) * (f_erase_end - f_stay_end)
            if t > kt_list[-1]:
                kt_list.append(t)
                w = (s * char_width + clip_offset) if s > 0 else 0
                val_w_list.append(w)
                val_x_list.append(start_x + prefix_width + s * char_width)
            
        # Final state for this line
        if f_end > kt_list[-1]:
            kt_list.append(f_end)
            val_w_list.append(0)
            val_x_list.append(start_x + prefix_width)
        
        if 1.0 > kt_list[-1]:
            kt_list.append(1.0)
            val_w_list.append(0)
            val_x_list.append(start_x + prefix_width)
            
        kt_str = ";".join([f"{x:.4f}" for x in kt_list])
        val_w_str = ";".join([f"{x:.1f}" for x in val_w_list])
        val_x_str = ";".join([f"{x:.1f}" for x in val_x_list])
        
    # Visibility animation
        vis_values = "0;0;1;1;0;0"
        vis_times = f"0;{f_start};{f_start + 0.0001};{f_end - 0.0001};{f_end};1"
        
        # Aggregate clipPaths
        all_defs += f"""
    <clipPath id="cp-{uid}-{i}">
        <rect x="{start_x + prefix_width - clip_offset}" y="0" width="0" height="70">
            <animate attributeName="width" values="{val_w_str}" keyTimes="{kt_str}" dur="{total_dur}s" repeatCount="indefinite" calcMode="discrete" />
        </rect>
    </clipPath>"""

        content += f"""
    <g opacity="0">
        <animate attributeName="opacity" values="{vis_values}" keyTimes="{vis_times}" dur="{total_dur}s" repeatCount="indefinite" />
        <text x="{start_x}" y="52" class="t-text" xml:space="preserve"><tspan x="{start_x}" fill="#00FFAA" fill-opacity="0.4">$ </tspan><tspan x="{start_x + prefix_width}" clip-path="url(#cp-{uid}-{i})">{safe_text}</tspan></text>
        <rect y="32" width="2" height="24" class="t-cursor">
            <animate attributeName="x" values="{val_x_str}" keyTimes="{kt_str}" dur="{total_dur}s" repeatCount="indefinite" calcMode="discrete" />
        </rect>
    </g>"""

    return f"""<svg width="500" height="70" viewBox="0 0 500 70" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    {all_defs}
  </defs>
  <style>
    :root {{ --bg: #0d1117; --text: {color}; --border: #30363d; }}
    @media (prefers-color-scheme: light) {{ :root {{ --bg: #ffffff; --text: #1a7f37; --border: #d0d7de; }} }}
    .t-container {{ fill: var(--bg); stroke: var(--border); stroke-width: 2; }}
    .t-text {{ font: bold 20px 'JetBrains Mono', monospace; fill: var(--text); }}
    .t-cursor {{ fill: var(--text); animation: t-blink 0.8s step-end infinite; }}
    @keyframes t-blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
  </style>
  <rect width="500" height="70" rx="15" class="t-container"/>
  <circle cx="25" cy="20" r="5" fill="#ff5f56"/><circle cx="45" cy="20" r="5" fill="#ffbd2e"/><circle cx="65" cy="20" r="5" fill="#27c93f"/>
  {content}
</svg>"""
