import html

def get_terminal_svg(data, color="#00FFAA"):
    width = 850
    height = 210
    
    role = html.escape(str(data.get("role", "Infosec Researcher & Reverse Engineer")))
    focus = html.escape(str(data.get("focus", "Vulnerability Research | Binary Exploitation | Kernel Internals")))
    mindset = html.escape(str(data.get("mindset", '"Break to understand. Reverse to build better."')))
    
    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- 
    =======================================================================
    [EASTER_EGG #1 // CLASSIFIED INTEL // CLEARANCE: LEVEL_5]
    OPERATOR: blackalex1
    TARGET_ROLE: {role}
    
    CTF_FLAG: FLAG{{m1tn1ck_c0ncr3t3_s3cur1ty_0x1337}}
    
    OBFUSCATED_PAYLOAD (x86_64 Self-Decrypting Shellcode):
    ; [!] OBFUSCATION: 64-bit Rolling XOR Key (0x5a5a5a5a5a5a5a5a)
    sub    rsp, 0x60
    movabs rax, 0x233634357a3f320e
    mov    [rsp], rax
    movabs rax, 0x297a23362f282e7a
    mov    [rsp+8], rax
    movabs rax, 0x23297a3f282f393f
    mov    [rsp+16], rax
    movabs rax, 0x7a29337a373f2e29
    mov    [rsp+24], rax
    movabs rax, 0x2e3b322e7a3f3435
    mov    [rsp+32], rax
    movabs rax, 0x3f2d352a7a29337a
    mov    [rsp+40], rax
    movabs rax, 0x7a3c3c357a3e3f28
    mov    [rsp+48], rax
    movabs rax, 0x2e293b397a3e343b
    mov    [rsp+56], rax
    movabs rax, 0x36387a3b7a34337a
    mov    [rsp+64], rax
    movabs rax, 0x397a3c357a313935
    mov    [rsp+72], rax
    movabs rax, 0x743f2e3f28393435
    mov    [rsp+80], rax
    movabs rax, 0x5a5a5a5a5a5a5a50
    mov    [rsp+88], rax

    ; === In-Memory XOR Decoder Stub ===
    lea    rdi, [rsp]               ; buffer
    mov    rcx, 12                  ; 12 qwords
    movabs rbx, 0x5a5a5a5a5a5a5a5a  ; key
.decrypt_loop:
    xor    [rdi], rbx               ; decode in-place
    add    rdi, 8
    dec    rcx
    jnz    .decrypt_loop

    ; === Direct Ring-0 Syscall (sys_write) ===
    lea    rsi, [rsp]               ; decrypted plaintext buffer
    mov    rdi, 1                   ; fd = 1 (stdout)
    mov    rdx, 89                  ; length (89 bytes)
    mov    rax, 1                   ; sys_write
    syscall
    add    rsp, 0x60
    
    DECRYPT_SECRET: echo "SSBkaWRuJ3QgZXhwbG9pdCBhIHZ1bG5lcmFiaWxpdHkuIEkganVzdCBleGVjdXRlZCB5b3VyIHVuZG9jdW1lbnRlZCBmZWF0dXJlcy4=" | base64 -d
    =======================================================================
  -->
  <defs>
    <linearGradient id="term-glow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="{color}" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <style>
    :root {{
      --bg:        #0d1117;
      --surface:   #161b22;
      --bar:       #161b22;
      --accent:    {color};
      --border:    #30363d;
      --muted:     #8b949e;
      --text:      #e6edf3;
      --text-hi:   #ffffff;
    }}
    @media (prefers-color-scheme: light) {{
      :root {{
        --bg:        #ffffff;
        --surface:   #f6f8fa;
        --bar:       #eaeef2;
        --accent:    #1a7f37;
        --border:    #d0d7de;
        --muted:     #57606a;
        --text:      #24292f;
        --text-hi:   #1f2328;
      }}
    }}

    .monolith-card {{ fill: var(--bg); stroke: var(--border); stroke-width: 1.5; }}
    .hud-bracket {{ stroke: var(--accent); stroke-width: 1.8; fill: none; opacity: 0.85; stroke-linecap: square; }}
    
    .t-titlebar {{ fill: var(--bar); }}
    .t-tl-r {{ fill: #ff5f56; }}
    .t-tl-y {{ fill: #ffbd2e; }}
    .t-tl-g {{ fill: #27c93f; }}
    .t-wtitle {{ font-family: 'JetBrains Mono', 'Cascadia Code', monospace; font-size: 11px; fill: var(--muted); letter-spacing: 0.5px; }}
    .t-pdir {{ font-family: 'JetBrains Mono', 'Cascadia Code', monospace; font-size: 12px; font-weight: 700; fill: var(--muted); }}
    .t-pcmd {{ font-family: 'JetBrains Mono', 'Cascadia Code', monospace; font-size: 12px; font-weight: 700; fill: var(--text-hi); }}
    .t-key {{ font-family: 'JetBrains Mono', 'Cascadia Code', monospace; font-size: 12px; font-weight: 600; fill: var(--muted); }}
    .t-val {{ font-family: 'JetBrains Mono', 'Cascadia Code', monospace; font-size: 12px; font-weight: 600; fill: var(--text); }}
    .t-val-hi {{ font-family: 'JetBrains Mono', 'Cascadia Code', monospace; font-size: 12px; font-weight: 700; fill: var(--accent); }}
    .t-cursor {{ fill: var(--accent); animation: blink 1s step-end infinite; }}
    @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    .t-fadein {{ opacity: 0; animation: t-fade 0.4s ease forwards; }}
    @keyframes t-fade {{ to {{ opacity: 1; }} }}

    /* Easter Egg #3 Tooltips */
    .t-btn {{ cursor: pointer; }}
    .t-tooltip {{
      opacity: 0;
      pointer-events: none;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      transform: translateX(-4px);
    }}
    .t-btn:hover .t-tooltip {{
      opacity: 1;
      transform: translateX(0);
    }}
    .tt-bg {{ fill: #1c2128; stroke: var(--accent); stroke-width: 1; }}
    .tt-txt {{ font: bold 9.5px 'JetBrains Mono', monospace; fill: #ffffff; letter-spacing: 0.5px; }}
    .t-btn-red:hover .tt-bg {{ stroke: #ff5f56; }}
    .t-btn-yellow:hover .tt-bg {{ stroke: #ffbd2e; }}
    .t-btn-green:hover .tt-bg {{ stroke: #27c93f; }}

    /* Easter Egg #6: Selection Revelation */
    .t-secret-select {{
      font: 9px 'JetBrains Mono', monospace;
      fill: var(--bg);
      letter-spacing: 0.5px;
      user-select: text;
      -webkit-user-select: text;
    }}
    ::selection {{
      background: {color};
      color: #0d1117;
    }}
  </style>

  <rect width="{width}" height="{height}" rx="12" class="monolith-card"/>
  <rect width="{width}" height="{height}" fill="url(#term-glow)" rx="12"/>
  
  <path d="M0 12 C0 5.373 5.373 0 12 0 H838 C844.627 0 850 5.373 850 12 V32 H0 V12 Z" class="t-titlebar"/>
  
  <!-- Easter Egg #3: Interactive Terminal Window Buttons -->
  <g class="t-btn t-btn-red" transform="translate(20, 16)">
    <circle cx="0" cy="0" r="4.5" class="t-tl-r"/>
    <g class="t-tooltip">
      <rect x="48" y="-10" width="135" height="20" rx="4" class="tt-bg"/>
      <text x="54" y="4" class="tt-txt">SIGKILL // PID: 1337</text>
    </g>
  </g>

  <g class="t-btn t-btn-yellow" transform="translate(36, 16)">
    <circle cx="0" cy="0" r="4.5" class="t-tl-y"/>
    <g class="t-tooltip">
      <rect x="32" y="-10" width="168" height="20" rx="4" class="tt-bg"/>
      <text x="38" y="4" class="tt-txt">SIGSTOP // DEBUGGER_TRAP</text>
    </g>
  </g>

  <g class="t-btn t-btn-green" transform="translate(52, 16)">
    <circle cx="0" cy="0" r="4.5" class="t-tl-g"/>
    <g class="t-tooltip">
      <rect x="16" y="-10" width="176" height="20" rx="4" class="tt-bg"/>
      <text x="22" y="4" class="tt-txt">RING_0 // ESCALATE_ROOT</text>
    </g>
  </g>

  <text x="{width/2}" y="20" text-anchor="middle" class="t-wtitle">alex@blackarch: ~ (zsh) — [PID: 1337 // TTY: pts/0]</text>
  
  <!-- Outer Corner Brackets -->
  <path d="M 0 18 L 0 0 L 18 0" class="hud-bracket"/>
  <path d="M {width} 18 L {width} 0 L {width-18} 0" class="hud-bracket"/>
  <path d="M 0 {height-18} L 0 {height} L 18 {height}" class="hud-bracket"/>
  <path d="M {width} {height-18} L {width} {height} L {width-18} {height}" class="hud-bracket"/>

  <g transform="translate(30, 56)">
    <text x="0" y="0" class="t-pdir">┌──(alex㉿blackarch)-[~]</text>
    <text x="0" y="22" class="t-pcmd">└─$ whoami --verbose --identity</text>
    
    <g class="t-fadein" style="animation-delay:0.1s">
      <text x="20" y="50" class="t-key">Role:</text>
      <text x="120" y="50" class="t-val-hi">{role}</text>
    </g>
    <g class="t-fadein" style="animation-delay:0.2s">
      <text x="20" y="72" class="t-key">Focus:</text>
      <text x="120" y="72" class="t-val">{focus}</text>
    </g>
    <g class="t-fadein" style="animation-delay:0.3s">
      <text x="20" y="94" class="t-key">Mindset:</text>
      <text x="120" y="94" class="t-val">{mindset}</text>
    </g>

    <!-- Easter Egg #6: Selection Revelation Text -->
    <text x="20" y="112" class="t-secret-select">&gt;&gt; [LOOPBACK // ::1] "There is no place like 127.0.0.1" // FLAG&#123;n0_pl4c3_l1k3_127_0_0_1&#125;</text>

    <g class="t-fadein" style="animation-delay:0.4s">
      <text x="0" y="128" class="t-pcmd">└─$ <tspan class="t-cursor">█</tspan></text>
    </g>
  </g>
</svg>"""
