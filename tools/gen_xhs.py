# -*- coding: utf-8 -*-
"""
小红书宣传海报生成器 · 《智驾时代：Agent 进化简史》
竖版 1080 x 1440，深紫底 + 橙→琥珀→绿渐变，复用全书视觉母题。
产出 5 张 SVG 到 assets/xhs/，可用 chromium 渲染 PNG。
"""
import os, html

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "xhs")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

# ---- 调色板（与 banner / gen_figures 一致）----
BG1, BG2 = "#1a0a2e", "#2d1b4e"
ORANGE, AMBER, GREEN = "#ff7043", "#ffa726", "#66bb6a"
WHITE = "#ffffff"
MUTED = "#b39ddb"
MUTED2 = "#7e57c2"
INK = "#15101f"
FONT = "Inter, 'Noto Sans CJK SC', 'PingFang SC', 'Microsoft YaHei', sans-serif"
W, H = 1080, 1440
PAD = 72

DEFS = f'''
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{BG1}"/>
      <stop offset="50%" style="stop-color:{BG2}"/>
      <stop offset="100%" style="stop-color:{BG1}"/>
    </linearGradient>
    <linearGradient id="acc" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{ORANGE}"/>
      <stop offset="50%" style="stop-color:{AMBER}"/>
      <stop offset="100%" style="stop-color:{GREEN}"/>
    </linearGradient>
    <linearGradient id="accV" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{ORANGE}"/>
      <stop offset="100%" style="stop-color:{GREEN}"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:{AMBER};stop-opacity:0.30"/>
      <stop offset="100%" style="stop-color:{AMBER};stop-opacity:0"/>
    </radialGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
    <filter id="blur"><feGaussianBlur stdDeviation="8"/></filter>
    <marker id="arA" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="{AMBER}"/></marker>
  </defs>'''

def esc(s): return html.escape(str(s), quote=False)

def txt(x, y, s, size=16, fill=WHITE, weight=600, anchor="start", op=1, spacing=0, font=FONT):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'opacity="{op}" letter-spacing="{spacing}">{esc(s)}</text>')

def mlines(x, y, lines, size=13, fill=MUTED, gap=19, anchor="middle", weight=400, spacing=0):
    return ''.join(txt(x, y + i * gap, ln, size, fill, weight, anchor, 1, spacing) for i, ln in enumerate(lines))

def glow(cx, cy, r, color=AMBER, op=0.3):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{op}" filter="url(#blur)"/>'

def chip(x, y, label, fill=AMBER, size=22, padx=20, pady=11, tcolor=INK, weight=700):
    w = len(label) * (size * 0.92) + padx * 2
    r = size + pady
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{r*2 - pady*0+pady*0 + pady*2}" rx="{r}" fill="{fill}"/>'
    # 简化：高度 = size + pady*2
    hh = size + pady * 2
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="{hh/2}" fill="{fill}"/>'
    t = txt(x + w / 2, y + hh / 2 + size * 0.36, label, size, tcolor, weight, "middle")
    return rect + t, x + w

def card(x, y, w, h, fill="rgba(255,255,255,0.045)", stroke=MUTED2, rx=18, sw=1.5, op=1, bar=None):
    r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>'
    b = f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="3" fill="{bar}"/>' if bar else ''
    return r + b

def car(cx, cy, s=1, body=AMBER):
    g = f'<g transform="translate({cx},{cy}) scale({s})">'
    g += f'<ellipse cx="0" cy="44" rx="108" ry="14" fill="#000000" opacity="0.28"/>'
    g += f'<rect x="-102" y="-14" width="204" height="44" rx="16" fill="{body}"/>'
    g += f'<path d="M -60 -14 L -42 -54 Q -36 -60 -28 -60 L 32 -60 Q 42 -60 50 -50 L 70 -14 Z" fill="{body}" opacity="0.95"/>'
    g += f'<path d="M -50 -18 L -36 -52 L 26 -52 L 42 -18 Z" fill="{BG1}" opacity="0.7"/>'
    g += f'<circle cx="-58" cy="30" r="21" fill="{INK}" stroke="{body}" stroke-width="4"/>'
    g += f'<circle cx="58" cy="30" r="21" fill="{INK}" stroke="{body}" stroke-width="4"/>'
    g += f'<circle cx="-58" cy="30" r="7" fill="{body}"/><circle cx="58" cy="30" r="7" fill="{body}"/>'
    g += f'<circle cx="94" cy="3" r="6" fill="#fff3e0"/>'
    g += '</g>'
    return g

def title_block(lines, x, y0, size, color, weight=800, lh=None, anchor="start", spacing=0):
    lh = lh or int(size * 1.16)
    out = []
    for i, ln in enumerate(lines):
        out.append(txt(x, y0 + i * lh, ln, size, color, weight, anchor, 1, spacing))
    return "".join(out), y0 + len(lines) * lh

def bg_layer():
    # 背景 + 网格 + 角落光晕 + 同心环装饰
    s = f'<rect width="{W}" height="{H}" rx="0" fill="url(#bg)"/>'
    grid = []
    for gx in range(PAD, W, 72):
        grid.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="#ffffff" stroke-width="1" opacity="0.025"/>')
    for gy in range(PAD, H, 72):
        grid.append(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke="#ffffff" stroke-width="1" opacity="0.025"/>')
    s += ''.join(grid)
    s += glow(W - 120, 150, 260, AMBER, 0.22)
    s += glow(120, H - 160, 240, ORANGE, 0.16)
    # 角落同心环
    s += f'<g transform="translate({W-90},{H-110})" opacity="0.18">'
    s += f'<circle r="120" fill="none" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="10 8"/>'
    s += f'<circle r="78" fill="none" stroke="{AMBER}" stroke-width="2" stroke-dasharray="9 7"/>'
    s += f'<circle r="40" fill="none" stroke="{GREEN}" stroke-width="2"/></g>'
    return s

def footer(book=True):
    y = H - 52
    s = f'<line x1="{PAD}" y1="{y-26}" x2="{W-PAD}" y2="{y-26}" stroke="{MUTED2}" stroke-width="1" opacity="0.4"/>'
    s += txt(PAD, y, "智驾时代 · Agent 进化简史", 20, WHITE, 700, "start")
    s += txt(W - PAD, y, "GitHub 免费开读 ↗", 19, AMBER, 700, "end")
    s += txt(PAD, y + 30, "github.com/Madapexai/agent-evolution-book", 15, MUTED2, 400, "start", 0.9)
    return s

def kicker(x, y, s):
    return txt(x, y, s, 20, AMBER, 700, "start", 0.95, spacing=2)

def bullet_list(x, y, items, color=AMBER, size=24, gap=66):
    out = []
    cy = y
    for i, it in enumerate(items):
        num = str(i + 1)
        c = [ORANGE, AMBER, GREEN][i % 3]
        # 编号圆
        out.append(f'<circle cx="{x+22}" cy="{cy+size*0.34}" r="22" fill="{c}" opacity="0.18"/>')
        out.append(f'<circle cx="{x+22}" cy="{cy+size*0.34}" r="22" fill="none" stroke="{c}" stroke-width="2"/>')
        out.append(txt(x + 22, cy + size * 0.34 + size * 0.36, num, size, c, 800, "middle"))
        # 主标题
        out.append(txt(x + 60, cy + size * 0.72, it[0], size, WHITE, 700, "start"))
        # 副说明
        if len(it) > 1:
            out.append(txt(x + 60, cy + size * 0.72 + 30, it[1], 17, MUTED, 400, "start"))
        cy += gap
    return "".join(out), cy

# ============================================================
# 海报 1：主打 · 一个比喻读懂 Agent
# ============================================================
def poster_01():
    inner = bg_layer()
    # kicker + chip
    ck, _ = chip(PAD, 64, "AI 干货 · 开源好书", AMBER, size=23)
    inner += ck
    inner += kicker(W - 300, 92, "NEW BOOK")
    # 标题
    t, ty = title_block(
        ["读懂 AI Agent", "只需要一个比喻"], PAD, 150, 74, WHITE, 800, spacing=0)
    inner += t
    # 标题下划线
    inner += f'<rect x="{PAD}" y="{ty+14}" width="210" height="8" rx="4" fill="url(#acc)"/>'
    # 副标题
    inner += txt(PAD, ty + 64, "把 AI 想成一辆车，它的进化史一目了然", 26, MUTED, 500, "start")
    # —— 中心：盘山路 + 5 个里程碑 + 车 ——
    cx0, y0 = PAD + 40, 1180
    ms = [
        (PAD + 50, 1150, "1", "Prompt", ORANGE),
        (PAD + 250, 1040, "2", "Context", f"#{ORANGE}"),
        (PAD + 450, 900, "3", "Harness", AMBER),
        (PAD + 650, 720, "4", "Loop", f"#{AMBER}"),
        (PAD + 850, 540, "5", "Auto-Org", GREEN),
    ]
    # 道路（穿过里程碑的曲线）
    road = "M%d,%d Q %d,%d %d,%d Q %d,%d %d,%d Q %d,%d %d,%d Q %d,%d %d,%d" % (
        ms[0][0], ms[0][1], 175, 1100, ms[1][0], ms[1][1],
        350, 980, ms[2][0], ms[2][1],
        550, 820, ms[3][0], ms[3][1],
        750, 640, ms[4][0], ms[4][1])
    inner += f'<path d="{road}" fill="none" stroke="#3a2a5e" stroke-width="30" stroke-linecap="round"/>'
    inner += f'<path d="{road}" fill="none" stroke="{AMBER}" stroke-width="3" stroke-dasharray="14 14" opacity="0.8"/>'
    for (mx, my, n, name, col) in ms:
        c = col if col.startswith("#") else {"ORANGE": ORANGE, "AMBER": AMBER, "GREEN": GREEN}[col]
        inner += f'<circle cx="{mx}" cy="{my}" r="30" fill="{INK}" stroke="{c}" stroke-width="4"/>'
        inner += txt(mx, my + 11, n, 30, c, 800, "middle")
        inner += txt(mx, my + 58, name, 20, WHITE, 700, "middle")
    inner += car(ms[4][0] + 70, ms[4][1] - 30, 0.95, GREEN)
    # —— 要点 ——
    bl, _ = bullet_list(PAD, 1240, [
        ("五代演化主线", "从会聊天的 Prompt 到能自组织的系统"),
        ("Harness 驾驶系统", "五子系统 × 七层纵深，拆开看明白"),
        ("中英双语 + 图解", "16 张矢量插画，零基础也能读"),
    ], gap=64)
    inner += bl
    inner += footer()
    return wrap(inner)

# ============================================================
# 海报 2：五代演化速览
# ============================================================
def poster_02():
    inner = bg_layer()
    ck, _ = chip(PAD, 64, "一图速览 · 5 个时代", AMBER, size=23)
    inner += ck
    inner += kicker(W - 360, 92, "5 GENERATIONS")
    t, ty = title_block(["AI Agent", "走过的 5 个时代"], PAD, 150, 74, WHITE, 800)
    inner += t
    inner += f'<rect x="{PAD}" y="{ty+14}" width="210" height="8" rx="4" fill="url(#acc)"/>'
    inner += txt(PAD, ty + 60, "每一代，车都更聪明一点", 26, MUTED, 500, "start")

    gens = [
        ("第一代", "Prompt", "会聊天的提示词", ORANGE),
        ("第二代", "Context", "带上记忆与资料", AMBER),
        ("第三代", "Harness", "能调用工具的驾驶系统", f"#{AMBER}"),
        ("第四代", "Loop", "自主规划、反思、重试", f"#{GREEN}"),
        ("第五代", "Auto-Org", "多智能体自我组织", GREEN),
    ]
    bw, bh = 470, 132
    x1, x2 = PAD, PAD + bw + 36
    ystart = 470
    yg = 150
    cols = [x1, x2, x1, x2, x1]
    for i, (g, en, desc, col) in enumerate(gens):
        c = col if col.startswith("#") else {"ORANGE": ORANGE, "AMBER": AMBER, "GREEN": GREEN}[col]
        x = cols[i]
        y = ystart + (i // 2) * yg
        inner += card(x, y, bw, bh, "rgba(255,255,255,0.05)", c, 18, 1.5, c)
        inner += txt(x + 28, y + 52, g, 22, c, 800, "start")
        inner += txt(x + 28, y + 92, en, 30, WHITE, 800, "start")
        inner += txt(x + 28, y + 120, desc, 18, MUTED, 400, "start")
        # 序号大标
        inner += txt(x + bw - 34, y + 64, str(i + 1), 44, c, 800, "end", 0.35)
    # 连接箭头（竖向示意）
    inner += footer()
    return wrap(inner)

# ============================================================
# 海报 3：Harness 双视角
# ============================================================
def poster_03():
    inner = bg_layer()
    ck, _ = chip(PAD, 64, "核心框架 · Harness", AMBER, size=23)
    inner += ck
    inner += kicker(W - 360, 92, "TWO VIEWS")
    t, ty = title_block(["Agent 的“驾驶系统”", "到底由什么组成"], PAD, 150, 60, WHITE, 800)
    inner += t
    inner += f'<rect x="{PAD}" y="{ty+12}" width="210" height="8" rx="4" fill="url(#acc)"/>'
    inner += txt(PAD, ty + 56, "同一个系统，两种拆法：横向看功能，纵向看纵深", 24, MUTED, 500, "start")

    # 左列：五子系统
    lx, lw = PAD, 470
    inner += txt(lx, 470, "功能视角 · 五子系统", 24, AMBER, 800, "start")
    subs = [("Context", "上下文"), ("Memory", "记忆"), ("Tool", "工具"), ("Policy", "策略"), ("Verification", "验证")]
    sy, sh = 492, 96
    for i, (en, zh) in enumerate(subs):
        y = sy + i * (sh + 12)
        inner += card(lx, y, lw, sh, "rgba(255,255,255,0.05)", AMBER, 14, 1.5, AMBER)
        inner += txt(lx + 26, y + sh / 2 + 8, en, 24, WHITE, 700, "start")
        inner += txt(lx + 26, y + sh / 2 + 34, zh, 16, MUTED, 400, "start")
        inner += txt(lx + lw - 24, y + sh / 2 + 8, f"0{i+1}", 26, AMBER, 800, "end", 0.5)
    # 右列：七层纵深
    rx, rw = PAD + 500, 436
    inner += txt(rx, 470, "纵深视角 · 七层架构", 24, GREEN, 800, "start")
    layers = ["L1 执行环境", "L2 工具网关", "L3 运行时", "L4 上下文", "L5 策略", "L6 协调", "L7 治理"]
    ry, lh2 = 492, 60
    for i, nm in enumerate(layers):
        y = ry + i * (lh2 + 6)
        op = 0.5 + i * 0.06
        inner += f'<rect x="{rx}" y="{y}" width="{rw}" height="{lh2}" rx="12" fill="{GREEN}" opacity="{op*0.18}" stroke="{GREEN}" stroke-width="1.5"/>'
        inner += txt(rx + 22, y + lh2 / 2 + 8, nm, 20, WHITE, 600, "start")
    # 中缝标签
    inner += txt(lx + lw + 18 + rw / 2, 900, "同一套系统", 18, MUTED2, 600, "middle")
    inner += footer()
    return wrap(inner)

# ============================================================
# 海报 4：三重悖论
# ============================================================
def poster_04():
    inner = bg_layer()
    ck, _ = chip(PAD, 64, "深度思考 · 3 个悖论", ORANGE, size=23, tcolor=WHITE)
    inner += ck
    inner += kicker(W - 300, 92, "PARADOX")
    t, ty = title_block(["越聪明的 Agent", "反而越矛盾？"], PAD, 150, 70, WHITE, 800)
    inner += t
    inner += f'<rect x="{PAD}" y="{ty+14}" width="210" height="8" rx="4" fill="url(#acc)"/>'
    inner += txt(PAD, ty + 64, "书里点破的三个“越……越……”陷阱", 26, MUTED, 500, "start")

    paradox = [
        ("记忆悖论", "记得越多，反而越容易跑偏", ORANGE),
        ("推理悖论", "想得越深，越可能绕回原地", AMBER),
        ("进化悖论", "越能自组织，越难被理解", GREEN),
    ]
    cw, ch = 290, 540
    gap = 26
    total = cw * 3 + gap * 2
    x0 = (W - total) / 2
    y0 = 470
    for i, (name, desc, col) in enumerate(paradox):
        x = x0 + i * (cw + gap)
        inner += card(x, y0, cw, ch, "rgba(255,255,255,0.05)", col, 18, 1.5, col)
        inner += txt(x + cw / 2, y0 + 80, f"0{i+1}", 56, col, 800, "middle", 0.45)
        # 循环箭头图标
        ix, iy = x + cw / 2, y0 + 210
        inner += f'<g transform="translate({ix},{iy})" opacity="0.9">'
        inner += f'<path d="M -34 0 A 34 34 0 1 1 -24 -24" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
        inner += f'<path d="M -24 -24 l 14 2 l -6 14 z" fill="{col}"/>'
        inner += f'<circle cx="0" cy="0" r="9" fill="{col}" opacity="0.5"/></g>'
        inner += txt(x + cw / 2, y0 + 320, name, 34, WHITE, 800, "middle")
        inner += mlines(x + cw / 2, y0 + 372, [desc], 20, MUTED, 28, "middle")
    inner += txt(W / 2, y0 + ch + 70, "三个悖论，书中都给了可落地的破局思路", 24, AMBER, 700, "middle")
    inner += footer()
    return wrap(inner)

# ============================================================
# 海报 5：中英双语 · 新书上线
# ============================================================
def poster_05():
    inner = bg_layer()
    ck, _ = chip(PAD, 64, "新书上线 · 免费开源", GREEN, size=23, tcolor=INK)
    inner += ck
    inner += kicker(W - 320, 92, "OPEN SOURCE")
    t, ty = title_block(["一本能读懂的", "AI Agent 进化书"], PAD, 150, 72, WHITE, 800)
    inner += t
    inner += f'<rect x="{PAD}" y="{ty+14}" width="210" height="8" rx="4" fill="url(#acc)"/>'
    inner += txt(PAD, ty + 64, "中文图解 + 英文对照，开页即读", 26, MUTED, 500, "start")

    # 中央：打开的书 + 中 / EN
    bx, by = W / 2, 560
    inner += glow(bx, by, 200, AMBER, 0.2)
    # 书页（两页）
    inner += f'<g transform="translate({bx},{by})">'
    inner += f'<path d="M -260 40 Q -130 -10 0 30 L 0 150 Q -130 110 -260 160 Z" fill="#241640" stroke="{MUTED2}" stroke-width="2"/>'
    inner += f'<path d="M 260 40 Q 130 -10 0 30 L 0 150 Q 130 110 260 160 Z" fill="#2a1a4a" stroke="{MUTED2}" stroke-width="2"/>'
    inner += f'<line x1="0" y1="30" x2="0" y2="150" stroke="{MUTED2}" stroke-width="2"/>'
    # 书脊装饰
    inner += f'<path d="M -260 40 Q -130 -10 0 30" fill="none" stroke="{AMBER}" stroke-width="2" opacity="0.6"/>'
    inner += f'<path d="M 260 40 Q 130 -10 0 30" fill="none" stroke="{GREEN}" stroke-width="2" opacity="0.6"/>'
    # 文字块
    for k in range(4):
        inner += f'<rect x="-235" y="{55+k*22}" width="190" height="5" rx="2.5" fill="{MUTED2}" opacity="0.5"/>'
        inner += f'<rect x="45" y="{55+k*22}" width="190" height="5" rx="2.5" fill="{MUTED2}" opacity="0.5"/>'
    inner += f'<text x="-130" y="20" font-family="{FONT}" font-size="40" font-weight="800" fill="{AMBER}" text-anchor="middle">中</text>'
    inner += f'<text x="130" y="20" font-family="{FONT}" font-size="34" font-weight="800" fill="{GREEN}" text-anchor="middle">EN</text>'
    inner += '</g>'

    # 特性 chips（2x2）
    feats = [("免费开源", AMBER), ("中文图解", ORANGE), ("一手出处", GREEN), ("持续更新", f"#{AMBER}")]
    fw, fh = 400, 92
    gx, gy = 30, 0
    x0 = PAD
    y0 = 880
    positions = [(x0, y0), (x0 + fw + gx, y0), (x0, y0 + fh + gy), (x0 + fw + gx, y0 + fh + gy)]
    for (name, col), (px, py) in zip(feats, positions):
        c = col if col.startswith("#") else {"AMBER": AMBER, "ORANGE": ORANGE, "GREEN": GREEN}[col]
        inner += card(px, py, fw, fh, "rgba(255,255,255,0.05)", c, 16, 1.5, c)
        inner += f'<circle cx="{px+40}" cy="{py+fh/2}" r="14" fill="{c}"/>'
        inner += txt(px + 40, py + fh / 2 + 6, "✓", 20, INK, 800, "middle") if False else txt(px + 40, py + fh / 2 + 6, "●", 16, INK, 800, "middle")
        inner += txt(px + 72, py + fh / 2 + 9, name, 28, WHITE, 700, "start")
    inner += txt(W / 2, y0 + 2 * (fh + gy) + 36, "现在就去 GitHub 免费读完整版 ↗", 24, AMBER, 700, "middle")
    inner += footer()
    return wrap(inner)

def wrap(inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}">\n{DEFS}\n{inner}\n</svg>')

def save(name, svg):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name, len(svg), "bytes")

if __name__ == "__main__":
    save("xhs_01_master.svg", poster_01())
    save("xhs_02_five_gen.svg", poster_02())
    save("xhs_03_harness.svg", poster_03())
    save("xhs_04_paradox.svg", poster_04())
    save("xhs_05_bilingual.svg", poster_05())
    print("done.")
