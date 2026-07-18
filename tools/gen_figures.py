# -*- coding: utf-8 -*-
"""
Agent 进化简史 · SVG 插画生成器
基于 banner 视觉调性：深紫底 + 橙→琥珀→绿渐变。
产出真实矢量插画（非 Mermaid 文本框图）到 assets/figures/。
"""
import os, html

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "figures")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

# ---- 调色板（与 banner.svg 一致）----
BG1, BG2 = "#1a0a2e", "#2d1b4e"
ORANGE, AMBER, GREEN = "#ff7043", "#ffa726", "#66bb6a"
WHITE = "#ffffff"
MUTED = "#b39ddb"
MUTED2 = "#7e57c2"
INK = "#15101f"
FONT = "Inter, 'Noto Sans CJK SC', 'PingFang SC', 'Microsoft YaHei', sans-serif"

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
      <stop offset="0%" style="stop-color:{AMBER};stop-opacity:0.35"/>
      <stop offset="100%" style="stop-color:{AMBER};stop-opacity:0"/>
    </radialGradient>
    <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
    <filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
    <marker id="ar" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="{AMBER}"/></marker>
    <marker id="arO" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="{ORANGE}"/></marker>
    <marker id="arG" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="{GREEN}"/></marker>
    <marker id="arW" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="{WHITE}"/></marker>
  </defs>'''

def esc(s):
    return html.escape(str(s), quote=False)

def txt(x, y, s, size=16, fill=WHITE, weight=600, anchor="start", opacity=1, spacing=0):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'opacity="{opacity}" letter-spacing="{spacing}">{esc(s)}</text>')

def mlines(x, y, lines, size=13, fill=MUTED, gap=19, anchor="middle", weight=400):
    return ''.join(txt(x, y + i * gap, ln, size, fill, weight, anchor) for i, ln in enumerate(lines))

def card(x, y, w, h, fill="rgba(255,255,255,0.04)", stroke=AMBER, rx=14, sw=1.5, op=1):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"/>')

def node(x, y, w, h, title, sub, color=AMBER, tsize=18, ssize=12.5, fill="rgba(255,255,255,0.05)"):
    """卡片节点：标题居中上，副标题多行居中下。"""
    inner = card(x, y, w, h, fill, color, 14, 1.6)
    tw = txt(x + w / 2, y + 30, title, tsize, WHITE, 700, "middle")
    if isinstance(sub, str):
        sub = [sub]
    sw_text = mlines(x + w / 2, y + 30 + tsize + 6, sub, ssize, MUTED, 17, "middle")
    # 顶部色条
    bar = f'<rect x="{x}" y="{y}" width="{w}" height="5" rx="2.5" fill="{color}"/>'
    return inner + bar + tw + sw_text

def arrow(x1, y1, x2, y2, color="ar", sw=2.5, dash=None):
    dash = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="url(#acc)" '
            f'stroke-width="{sw}" marker-end="url(#{color})"{dash} '
            f'opacity="0.9"/>') if color in ("ar",) else \
           (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{sw}" marker-end="url(#{color})"{dash} '
            f'opacity="0.9"/>')

def glow_circle(cx, cy, r, color=AMBER, op=0.3):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" opacity="{op}" filter="url(#blur)"/>'

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

def wrap(w, h, inner, border=True):
    b = (f'<rect x="6" y="6" width="{w-12}" height="{h-12}" rx="18" fill="none" '
         f'stroke="{MUTED2}" stroke-width="1" opacity="0.5"/>') if border else ''
    foot = txt(w - 16, h - 14, "智驾时代 · Agent 进化简史", 11, MUTED2, 400, "end", 0.8)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">\n{DEFS}\n'
            f'<rect width="{w}" height="{h}" rx="22" fill="url(#bg)"/>\n'
            f'{inner}\n{b}\n{foot}\n</svg>')

def save(name, svg):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name, len(svg), "bytes")

# ============================================================
# 1. 英雄图：智能车 = Agent
# ============================================================
def fig_cover_car():
    w, h = 920, 520
    inn = ''
    inn += txt(60, 64, "Agent = 一辆会自己开的智能车", 30, WHITE, 800, "start", 0, -0.5)
    inn += txt(60, 96, "LLM 是大脑，Harness 是整车安全系统——合起来，才是一辆能上路的车。", 15, MUTED, 400)
    # 道路
    inn += f'<rect x="0" y="430" width="{w}" height="90" fill="{INK}" opacity="0.6"/>'
    inn += f'<line x1="0" y1="462" x2="{w}" y2="462" stroke="{AMBER}" stroke-width="3" stroke-dasharray="22 18" opacity="0.7"/>'
    # 光晕
    inn += glow_circle(460, 290, 150, AMBER, 0.22)
    # 车
    inn += car(460, 330, 1.25, AMBER)
    # LLM 大脑（车顶）
    inn += node(360, 150, 200, 86, "LLM · 大脑", ["理解 / 推理 / 生成", "罐子里的大脑"], ORANGE, 19, 13)
    inn += arrow(460, 236, 460, 268, "arO", 3)
    # Harness 车身标注
    inn += node(640, 300, 230, 92, "Harness · 整车安全系统", ["记忆 · 工具 · 上下文", "权限 · 验证 · 治理"], GREEN, 18, 13)
    inn += arrow(636, 330, 690, 333, "arG", 2.5)
    # 远端五代路标
    signs = [("Prompt", ORANGE), ("Context", AMBER), ("Harness", AMBER), ("Loop", GREEN), ("Auto-Org", GREEN)]
    sx = 80
    for i, (t, c) in enumerate(signs):
        x = sx + i * 84
        inn += f'<rect x="{x}" y="408" width="64" height="26" rx="6" fill="{INK}" stroke="{c}" stroke-width="1.5" opacity="0.9"/>'
        inn += txt(x + 32, 425, t, 11, c, 600, "middle")
    inn += txt(60, 408, "演化来路 →", 12, MUTED, 400)
    return wrap(w, h, inn)

# ============================================================
# 2. 五代演化高速路
# ============================================================
def fig_five_generations():
    w, h = 980, 520
    gens = [
        ("第一代", "Prompt", "会聊天的提示词", "红绿灯：你问我答", ORANGE),
        ("第二代", "Context", "看得见上下文", "挡风玻璃：该看的才看", AMBER),
        ("第三代", "Harness", "能动手的整车系统", "整车：记忆+工具+权限", AMBER),
        ("第四代", "Loop", "自己跑的自动驾驶", "循环：想—做—看", GREEN),
        ("第五代", "Auto-Org", "自进化的组织", "车队：多体自组织", GREEN),
    ]
    inn = ''
    inn += txt(60, 60, "五代演化：一条越来越智能的高速路", 28, WHITE, 800, "start", 0, -0.5)
    # 路面
    ry = 400
    inn += f'<rect x="40" y="{ry}" width="{w-80}" height="64" rx="14" fill="{INK}" opacity="0.6"/>'
    inn += f'<line x1="60" y1="{ry+32}" x2="{w-60}" y2="{ry+32}" stroke="{AMBER}" stroke-width="3" stroke-dasharray="20 16" opacity="0.7"/>'
    # 阶段卡片
    n = len(gens); m = 70; cw = 150; gap = (w - 120 - n * cw) / (n - 1)
    xs = [m + i * (cw + gap) for i in range(n)]
    for i, (gen, name, one, car_, c) in enumerate(gens):
        x = xs[i]
        inn += node(x, 150, cw, 150, name, [gen, one], c, 20, 13)
        # 车标
        inn += car(x + cw / 2, ry - 18, 0.42, c)
        # 连接箭头（路面之上）
        if i < n - 1:
            inn += arrow(x + cw + 6, ry - 18, xs[i + 1] - 6, ry - 18, "ar", 2.5)
        # 汽车类比注释
        inn += txt(x + cw / 2, ry + 56, car_, 12.5, c, 600, "middle")
    # 起点终点
    inn += txt(60, 130, "起点", 12, MUTED, 400)
    inn += txt(w - 60, 130, "终点：自主进化", 12, MUTED, 400, "end")
    return wrap(w, h, inn)

# ============================================================
# 3. Harness 五子系统（汽车部件类比）
# ============================================================
def fig_harness_5subs():
    w, h = 980, 620
    inn = ''
    inn += txt(60, 56, "Harness 五大子系统：一辆能可靠干活的车的五个部位", 25, WHITE, 800, "start", 0, -0.5)
    # 中央车体
    inn += glow_circle(360, 340, 180, AMBER, 0.16)
    inn += car(360, 340, 1.5, AMBER)
    # 五个标注（左右各二+一）
    items = [
        (640, 110, "Context", "看到什么", "前挡风玻璃：该透明透明，该遮挡遮挡", ORANGE),
        (640, 230, "Memory · RAG", "记住什么", "导航+行车记录仪：该存多久、怎么隔离", AMBER),
        (640, 350, "Tool", "能做什么", "机械手+工具箱：真正去拧螺丝", GREEN),
        (640, 470, "Policy", "不能做什么", "刹车+交通规则：红线绝不越", ORANGE),
        (640, 560, "Verification", "做对了吗", "后视镜+年检：结果复核再交付", GREEN),
    ]
    for (x, y, t, q, sub, c) in items:
        inn += node(x, y, 290, 86, t, [q, sub], c, 18, 12.5)
        # 指向车体
        inn += arrow(x - 8, y + 43, 470, 340, "ar", 2)
    # 左侧公式
    inn += node(60, 230, 230, 90, "Agent = LLM + Harness", ["一整套工程系统", "而非单一技术"], ORANGE, 17, 13)
    return wrap(w, h, inn)

# ============================================================
# 4. 七层架构（纵深防护）
# ============================================================
def fig_harness_7layers():
    w, h = 760, 700
    layers = [
        ("L7 治理 Governance", "规则 · 权限 · 成本 · 合规", ORANGE),
        ("L6 验证 Verification", "自动化测试 · 独立审查 · 人工审批", ORANGE),
        ("L5 可观测性 Observability", "做了什么 · 花了多少 · 出了什么错", AMBER),
        ("L4 生命周期 Lifecycle", "任务启停 · 子任务拆分", AMBER),
        ("L3 上下文管理 Context", "System Prompt · 项目规则 · Skills", GREEN),
        ("L2 工具接口 Tools", "注册 · 协议 · 权限 · MCP", GREEN),
        ("L1 执行环境 Runtime", "沙箱 · 权限隔离 · 资源限制", GREEN),
    ]
    inn = ''
    inn += txt(40, 52, "Harness 七层架构：一层层垒起的纵深防护", 23, WHITE, 800, "start", 0, -0.5)
    top = 90; lh = 74; lw = w - 120; lx = 60
    for i, (t, sub, c) in enumerate(layers):
        y = top + i * (lh + 6)
        inn += node(lx, y, lw, lh, t, sub, c, 17, 12.5, "rgba(255,255,255,0.05)")
        # 右侧层级指示
        inn += txt(lx + lw - 16, y + lh / 2 + 5, f"{7-i}", 22, c, 800, "end", 0.85)
    # 沙箱小人（L1 内）
    inn += txt(lx + 20, top + 6 * (lh + 6) + lh / 2 + 5, "🛡 安全屋", 13, GREEN, 700)
    # 侧边向上箭头
    inn += arrow(lx + lw + 22, top + 6 * (lh + 6) + lh / 2, lx + lw + 22, top + lh / 2, "arG", 2.5)
    inn += txt(lx + lw + 30, top + 3 * (lh + 6), "越往上越高级", 12, MUTED, 400, "start")
    return wrap(w, h, inn)

# ============================================================
# 5. 三重悖论
# ============================================================
def fig_triple_paradox():
    w, h = 980, 470
    inn = ''
    inn += txt(60, 56, "三重悖论：Agent 越强，越要回答这三个“反过来”的问题", 23, WHITE, 800, "start", 0, -0.5)
    panels = [
        ("记忆悖论", "Memory Paradox", ["记得越多 ≠ 越聪明", "记忆要管理：存多久、", "怎么隔离、何时丢弃"], ORANGE),
        ("推理悖论", "Reasoning Paradox", ["想得越细 ≠ 越对", "分步思考提升准确率，", "但也会走入过度推理"], AMBER),
        ("进化悖论", "Evolution Paradox", ["改自己 ≠ 更可靠", "自进化带来能力跃迁，", "也带来失控风险"], GREEN),
    ]
    pw, ph, px = 290, 300, 60
    gaps = (w - 120 - 3 * pw) / 2
    for i, (t, en, subs, c) in enumerate(panels):
        x = px + i * (pw + gaps)
        y = 110
        inn += node(x, y, pw, ph, t, [en] + subs, c, 22, 13)
        # 悖论环：两个相反箭头
        cyc = y + 150
        inn += (f'<circle cx="{x+pw/2}" cy="{cyc}" r="34" fill="none" stroke="{c}" stroke-width="3" opacity="0.8"/>'
                f'<path d="M {x+pw/2-24} {cyc-24} A 34 34 0 0 1 {x+pw/2+24} {cyc-24}" '
                f'fill="none" stroke="{c}" stroke-width="3" marker-end="url(#ar)" opacity="0.9"/>'
                f'<path d="M {x+pw/2+24} {cyc+24} A 34 34 0 0 1 {x+pw/2-24} {cyc+24}" '
                f'fill="none" stroke="{WHITE}" stroke-width="2.5" marker-end="url(#arW)" opacity="0.7"/>')
        inn += txt(x + pw / 2, cyc + 6, "⇄", 22, WHITE, 700, "middle")
    return wrap(w, h, inn)

# ============================================================
# 6. Agent 循环
# ============================================================
def fig_agent_loop():
    w, h = 660, 660
    cx, cy, R = 330, 340, 180
    inn = ''
    inn += txt(330, 50, "Agent Loop：转起来的车才叫自动驾驶", 22, WHITE, 800, "middle", 0, -0.5)
    steps = [
        ("观察 Observe", "看环境 / 读上下文", ORANGE, -90),
        ("思考 Think", "LLM 推理下一步", AMBER, 30),
        ("行动 Act", "调用工具去做", GREEN, 150),
    ]
    for (t, sub, c, deg) in steps:
        import math
        rad = math.radians(deg)
        nx, ny = cx + R * math.cos(rad), cy + R * math.sin(rad)
        inn += glow_circle(nx, ny, 70, c, 0.18)
        inn += node(nx - 80, ny - 50, 160, 100, t, sub, c, 18, 12.5)
    # 圆弧箭头 观察->思考->行动->观察
    inn += (f'<path d="M {cx+R} {cy} A {R} {R} 0 0 1 {cx+R*math.cos(math.radians(30)):.0f} {cy+R*math.sin(math.radians(30)):.0f}" '
            f'fill="none" stroke="url(#acc)" stroke-width="3" marker-end="url(#ar)" opacity="0.85"/>')
    inn += (f'<path d="M {cx+R*math.cos(math.radians(30)):.0f} {cy+R*math.sin(math.radians(30)):.0f} A {R} {R} 0 0 1 {cx+R*math.cos(math.radians(150)):.0f} {cy+R*math.sin(math.radians(150)):.0f}" '
            f'fill="none" stroke="url(#acc)" stroke-width="3" marker-end="url(#ar)" opacity="0.85"/>')
    inn += (f'<path d="M {cx+R*math.cos(math.radians(150)):.0f} {cy+R*math.sin(math.radians(150)):.0f} A {R} {R} 0 0 1 {cx+R} {cy} " '
            f'fill="none" stroke="url(#acc)" stroke-width="3" marker-end="url(#ar)" opacity="0.85"/>')
    inn += node(cx - 70, cy - 28, 140, 56, "Agent Loop", ["永不停转的闭环"], AMBER, 18, 12.5)
    # 外部环境
    inn += txt(330, 600, "外部环境：被观察、被改变", 13, MUTED, 400, "middle")
    return wrap(w, h, inn)

# ============================================================
# 7. ReAct 交错
# ============================================================
def fig_react():
    w, h = 920, 520
    inn = ''
    inn += txt(60, 56, "ReAct：推理与行动，像开车一样交替进行", 25, WHITE, 800, "start", 0, -0.5)
    seq = [
        ("思考", "先看红绿灯", AMBER),
        ("行动", "踩油门、变道", ORANGE),
        ("观察", "车到哪了?", GREEN),
        ("思考", "下一个路口", AMBER),
        ("行动", "打方向转弯", ORANGE),
        ("观察", "是否到位?", GREEN),
    ]
    n = len(seq); bw, bh = 120, 80; x0, y0 = 70, 180; dx = (w - 140 - bw) / (n - 1)
    for i, (t, sub, c) in enumerate(seq):
        x = x0 + i * dx
        y = y0 + (i % 2) * 110  # 上下交错
        inn += node(x, y, bw, bh, t, sub, c, 18, 12.5)
        if i < n - 1:
            # 折线连接
            xn = x0 + (i + 1) * dx
            yn = y0 + ((i + 1) % 2) * 110
            midx = (x + xn) / 2
            inn += (f'<path d="M {x+bw} {y+bh/2} C {midx} {y+bh/2}, {midx} {yn+bh/2}, {xn} {yn+bh/2}" '
                    f'fill="none" stroke="url(#acc)" stroke-width="2.5" marker-end="url(#ar)" opacity="0.85"/>')
    inn += txt(60, h - 40, "推理(Thought)与行动(Action)交织，观察(Observation)穿插其中——这就是 ReAct 模式。", 14, MUTED, 400)
    return wrap(w, h, inn)

# ============================================================
# 8. 上下文漏斗
# ============================================================
def fig_context_funnel():
    w, h = 780, 540
    inn = ''
    inn += txt(60, 56, "Context Engineering：给 AI 装一块“聪明的挡风玻璃”", 23, WHITE, 800, "start", 0, -0.5)
    # 漏斗
    inn += f'<path d="M 140 140 L 360 140 L 300 300 L 200 300 Z" fill="rgba(255,167,38,0.12)" stroke="{AMBER}" stroke-width="2"/>'
    inn += txt(250, 175, "原始信息 Raw", 16, WHITE, 700, "middle")
    inn += txt(250, 200, "海量上下文涌入", 12.5, MUTED, 400, "middle")
    # 挡风玻璃过滤
    inn += node(430, 160, 300, 130, "前挡风玻璃：筛选 / 遮挡", ["该透明的透明（任务相关）", "该遮挡的遮挡（噪音 / 越权）", "压缩后只留最该看的"], ORANGE, 17, 12.5)
    inn += arrow(360, 220, 428, 225, "arO", 2.5)
    # 过滤掉的
    inn += txt(250, 340, "↳ 被挡掉的噪音 / 越权内容", 12.5, MUTED2, 400, "middle")
    # 压缩后上下文
    inn += node(140, 360, 250, 110, "压缩后的上下文", ["精炼、有序、按时序", "送入模型窗口"], GREEN, 17, 12.5)
    inn += arrow(300, 290, 265, 358, "arG", 2.5)
    # LLM
    inn += node(470, 380, 250, 110, "LLM 窗口", ["只看到“该看的”", "推理更准、成本更低"], ORANGE, 18, 12.5)
    inn += arrow(390, 415, 468, 415, "arO", 2.5)
    return wrap(w, h, inn)

# ============================================================
# 9. Chatbot vs Agent
# ============================================================
def fig_chatbot_vs_agent():
    w, h = 980, 480
    inn = ''
    inn += txt(60, 54, "Chatbot 与 Agent：差的不只是“会不会做”", 24, WHITE, 800, "start", 0, -0.5)
    # 左：Chatbot
    inn += node(60, 110, 400, 300, "Chatbot · 聊天机器人", ["你问一句，它答一句", "不会真的去做"], ORANGE, 20, 13)
    inn += txt(110, 210, "问 → 答 → 停", 18, ORANGE, 700, "middle")
    inn += txt(110, 250, "（没有手，没有脚）", 14, MUTED, 400, "middle")
    # 一直停在原地的小人
    inn += f'<circle cx="320" cy="320" r="26" fill="none" stroke="{ORANGE}" stroke-width="3" opacity="0.7"/>'
    inn += txt(320, 326, "原地", 13, ORANGE, 600, "middle")
    # 右：Agent
    inn += node(520, 110, 400, 300, "Agent · 智能体", ["问 → 想 → 做 → 看", "闭环驱动、真去执行"], GREEN, 20, 13)
    # 闭环
    import math
    ccx, ccy, cr = 720, 260, 70
    inn += (f'<circle cx="{ccx}" cy="{ccy}" r="{cr}" fill="none" stroke="url(#acc)" stroke-width="3" opacity="0.85"/>')
    inn += txt(ccx, ccy - 30, "想", 15, AMBER, 700, "middle")
    inn += txt(ccx + 50, ccy, "做", 15, ORANGE, 700, "middle")
    inn += txt(ccx, ccy + 34, "看", 15, GREEN, 700, "middle")
    inn += txt(ccx - 50, ccy, "问", 15, WHITE, 700, "middle")
    inn += car(ccx, ccy + 110, 0.4, GREEN)
    # 中间箭头
    inn += arrow(470, 260, 512, 260, "arG", 3)
    inn += txt(490, 245, "本质差别", 12, MUTED, 400, "middle")
    return wrap(w, h, inn)

# ============================================================
# 10. 自组织
# ============================================================
def fig_auto_org():
    w, h = 920, 520
    inn = ''
    inn += txt(60, 56, "Auto-Organization：从一盘散沙到一支车队", 25, WHITE, 800, "start", 0, -0.5)
    import math, random
    random.seed(7)
    # 左：散点 swarm
    inn += txt(90, 130, "一群零散 Agent", 15, MUTED, 600, "middle")
    for i in range(14):
        x = 50 + random.randint(0, 230); y = 170 + random.randint(0, 250)
        c = random.choice([ORANGE, AMBER, GREEN])
        inn += f'<circle cx="{x}" cy="{y}" r="9" fill="{c}" opacity="0.85"/>'
    # 中间箭头 + 自组织
    inn += arrow(330, 290, 470, 290, "ar", 3)
    inn += txt(400, 250, "自组织", 14, WHITE, 700, "middle")
    inn += txt(400, 272, "Self-Organization", 11, MUTED2, 400, "middle")
    # 右：车队结构
    inn += txt(700, 130, "协同进化的组织", 15, MUTED, 600, "middle")
    # 协调者
    inn += node(600, 160, 200, 70, "协调者 Coordinator", ["分配 · 汇总 · 纠偏"], ORANGE, 16, 12.5)
    # 三个 worker
    for i, c in enumerate([AMBER, GREEN, ORANGE]):
        x = 600 + i * 100
        inn += node(x, 300, 90, 80, f"Agent {i+1}", ["专职子任务"], c, 15, 12)
        inn += arrow(700, 232, x + 45, 298, "ar", 2)
    # 底边：共享记忆/进化
    inn += node(600, 430, 300, 60, "共享记忆 · 共同进化", ["经验沉淀、能力跃迁"], GREEN, 16, 12.5)
    for i in range(3):
        inn += arrow(645 + i * 100, 382, 645 + i * 100, 428, "arG", 2)
    return wrap(w, h, inn)

# ============================================================
# 新增：架构图 Architecture & 流程图 Flowchart
# ============================================================
def fproc(x, y, w, h, label, sub=None, color=AMBER, tsize=15):
    g = card(x, y, w, h, "rgba(255,255,255,0.05)", color, 12, 1.6)
    g += txt(x + w / 2, y + h / 2 - (4 if sub else 0), label, tsize, WHITE, 700, "middle")
    if sub:
        g += txt(x + w / 2, y + h / 2 + 16, sub, 11, MUTED, 400, "middle")
    return g

def fdec(x, y, s, label, color=ORANGE, tsize=14):
    pts = f"{x},{y-s} {x+s},{y} {x},{y+s} {x-s},{y}"
    g = f'<polygon points="{pts}" fill="rgba(255,255,255,0.07)" stroke="{color}" stroke-width="2.2"/>'
    g += txt(x, y + 5, label, tsize, WHITE, 700, "middle")
    return g

def fstart(x, y, w, h, label, color=GREEN):
    g = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{color}" opacity="0.18" stroke="{color}" stroke-width="2"/>'
    g += txt(x + w / 2, y + h / 2 + 5, label, 15, WHITE, 700, "middle")
    return g

def fig_arch_system():
    w, h = 980, 640
    inn = ''
    inn += txt(60, 56, "整体 Agent 系统架构：环境 → LLM → Harness → 执行", 23, WHITE, 800, "start", 0, -0.5)
    inn += fproc(60, 100, 860, 70, "① 环境层 Environment", "用户 · 工具 · 数据 · 互联网", ORANGE, 17)
    inn += arrow(490, 170, 490, 198, "ar", 2.5)
    inn += fproc(340, 200, 300, 80, "② LLM 推理核心", "大模型大脑：理解 · 推理 · 生成", AMBER, 17)
    inn += arrow(490, 280, 490, 308, "ar", 2.5)
    inn += txt(60, 334, "③ Harness 五大子系统（整车安全系统）", 15, MUTED, 600)
    subs = [("Context", ORANGE), ("Memory", AMBER), ("Tool", GREEN), ("Policy", ORANGE), ("Verification", GREEN)]
    n = 5; bw = 164; gap = (860 - n * bw) / (n - 1); x0 = 60
    for i, (t, c) in enumerate(subs):
        x = x0 + i * (bw + gap)
        inn += fproc(x, 348, bw, 86, t, None, c, 15)
    inn += arrow(490, 434, 490, 462, "ar", 2.5)
    inn += fproc(60, 464, 860, 70, "④ 执行环境 Runtime", "沙箱 · 权限隔离 · 资源限制 → 工具执行 / 动作落地", GREEN, 17)
    inn += f'<rect x="44" y="192" width="892" height="356" rx="18" fill="none" stroke="{MUTED2}" stroke-width="1.3" stroke-dasharray="8 6" opacity="0.5"/>'
    inn += txt(56, 210, "Harness 整车安全系统", 12, MUTED2, 600)
    inn += (f'<path d="M 936 499 C 1000 499, 1000 135, 936 135" fill="none" stroke="url(#acc)" '
            f'stroke-width="2.5" marker-end="url(#ar)" opacity="0.8"/>')
    inn += txt(952, 320, "反馈闭环", 12, MUTED, 400, "middle")
    inn += txt(60, 604, "输入从环境进入，经 LLM 推理、Harness 调度五大子系统，在执行环境中落地动作，结果再反馈回环境。", 13, MUTED, 400)
    return wrap(w, h, inn)

def fig_arch_toolcall():
    w, h = 940, 520
    inn = ''
    inn += txt(60, 56, "工具调用架构：LLM 经 Router / MCP 路由调用工具", 22, WHITE, 800, "start", 0, -0.5)
    inn += fproc(60, 200, 180, 96, "LLM 大脑", "决定调用哪个工具", ORANGE, 17)
    inn += arrow(240, 248, 298, 248, "ar", 2.5)
    inn += fproc(300, 200, 200, 96, "Tool Router", "MCP 协议 · 注册 / 路由", AMBER, 17)
    tools = [("Search 搜索", ORANGE, 80), ("Code Exec 代码执行", GREEN, 200),
             ("DB Query 数据库", AMBER, 320), ("API Call 接口", ORANGE, 440)]
    for (t, c, y) in tools:
        inn += arrow(500, 248, 598, y + 35, "ar", 2)
        inn += fproc(600, y, 280, 70, t, None, c, 16)
    inn += (f'<path d="M 600 390 C 470 430, 320 420, 250 320" fill="none" '
            f'stroke="{MUTED2}" stroke-width="1.8" stroke-dasharray="7 5" marker-end="url(#arW)" opacity="0.6"/>')
    inn += txt(360, 452, "结果回传 LLM", 12, MUTED2, 400, "middle")
    inn += txt(60, 480, "LLM 决定动作 → Router 按 MCP 协议选定并调用工具 → 执行结果经 Router 回传 LLM，进入下一轮推理。", 13, MUTED, 400)
    return wrap(w, h, inn)

def fig_arch_multagent():
    w, h = 940, 560
    inn = ''
    inn += txt(60, 56, "多智能体编排架构：协调者 + 共享总线 + Worker 池", 22, WHITE, 800, "start", 0, -0.5)
    inn += fproc(320, 90, 300, 84, "Orchestrator 协调者", "分配 · 汇总 · 纠偏", ORANGE, 17)
    inn += arrow(470, 174, 470, 202, "ar", 2.5)
    inn += fproc(210, 204, 520, 60, "共享消息总线 / 全局记忆 Shared Bus", None, AMBER, 16)
    workers = [("Planner 规划", GREEN, 70), ("Coder 编码", AMBER, 290),
               ("Tester 测试", ORANGE, 510), ("Reviewer 审查", GREEN, 730)]
    for (t, c, x) in workers:
        inn += arrow(470, 264, x + 100, 322, "ar", 2)
        inn += fproc(x, 324, 200, 96, t, None, c, 15)
        inn += (f'<path d="M {x+100} 420 C {x+100} 470, 470 484, 470 268" fill="none" '
                f'stroke="{MUTED2}" stroke-width="1.6" stroke-dasharray="6 5" marker-end="url(#arW)" opacity="0.5"/>')
    inn += txt(60, 510, "协调者把任务拆给各 Worker，Worker 经共享总线交换中间结果，最终由协调者汇总。自组织即在此涌现。", 13, MUTED, 400)
    return wrap(w, h, inn)

def fig_flow_task():
    w, h = 820, 800
    cx = 410
    inn = ''
    inn += txt(60, 52, "任务执行主流程：一个会自己转的闭环", 22, WHITE, 800, "start", 0, -0.5)
    inn += fstart(cx - 90, 70, 180, 50, "接收任务", GREEN)
    inn += arrow(cx, 120, cx, 140, "ar", 2.5)
    inn += fproc(cx - 110, 140, 220, 54, "规划子任务", None, AMBER, 15)
    inn += arrow(cx, 194, cx, 214, "ar", 2.5)
    inn += fproc(cx - 110, 214, 220, 54, "思考：LLM 推理下一步", None, AMBER, 15)
    inn += arrow(cx, 268, cx, 288, "ar", 2.5)
    inn += fproc(cx - 110, 288, 220, 54, "选择并调用工具", None, ORANGE, 15)
    inn += arrow(cx, 342, cx, 362, "ar", 2.5)
    inn += fproc(cx - 110, 362, 220, 54, "执行动作 / 观察结果", None, ORANGE, 15)
    inn += arrow(cx, 416, cx, 444, "ar", 2.5)
    inn += fdec(cx, 474, 52, "完成?", ORANGE, 15)
    inn += (f'<path d="M {cx-52} 474 C 215 474, 195 241, {cx-110} 241" fill="none" '
            f'stroke="url(#acc)" stroke-width="2.4" marker-end="url(#ar)" opacity="0.85"/>')
    inn += txt(195, 360, "否 ↺", 14, MUTED, 600, "middle")
    inn += arrow(cx, 526, cx, 552, "ar", 2.5)
    inn += fproc(cx - 90, 552, 180, 54, "验证结果", None, GREEN, 15)
    inn += arrow(cx, 606, cx, 634, "ar", 2.5)
    inn += fdec(cx, 664, 46, "通过?", GREEN, 15)
    inn += fproc(cx + 72, 644, 150, 50, "修正 / 重试", None, ORANGE, 14)
    inn += (f'<path d="M {cx+72} 669 C 300 706, 240 262, {cx-110} 241" fill="none" '
            f'stroke="{ORANGE}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arO)" opacity="0.7"/>')
    inn += txt(cx + 150, 700, "否", 13, ORANGE, 600, "middle")
    inn += arrow(cx, 710, cx, 736, "ar", 2.5)
    inn += fstart(cx - 90, 736, 180, 50, "交付结果", GREEN)
    return wrap(w, h, inn)

def fig_flow_context_pipeline():
    w, h = 860, 580
    cx = 380
    inn = ''
    inn += txt(60, 52, "上下文工程流水线：给 LLM 喂对的料", 22, WHITE, 800, "start", 0, -0.5)
    inn += fstart(cx - 110, 70, 220, 50, "原始信号", ORANGE)
    inn += txt(cx, 100, "（对话 / 文件 / 工具结果）", 12, MUTED, 400, "middle")
    inn += arrow(cx, 120, cx, 146, "ar", 2.5)
    inn += fproc(cx - 110, 146, 220, 50, "① 采集 Collect", None, AMBER, 15)
    inn += arrow(cx, 196, cx, 222, "ar", 2.5)
    inn += fproc(cx - 110, 222, 220, 50, "② 筛选 Filter", "去噪 · 脱敏 · 截断", AMBER, 15)
    inn += (f'<path d="M {cx+110} 247 C 620 247, 660 320, 660 352" fill="none" '
            f'stroke="{MUTED2}" stroke-width="2" marker-end="url(#arW)" opacity="0.6"/>')
    inn += txt(700, 322, "× 丢弃", 13, MUTED2, 600, "middle")
    inn += txt(700, 342, "噪音 / 越权", 11, MUTED2, 400, "middle")
    inn += arrow(cx, 272, cx, 298, "ar", 2.5)
    inn += fproc(cx - 110, 298, 220, 50, "③ 压缩 Compress", "摘要 · 重排", GREEN, 15)
    inn += arrow(cx, 348, cx, 374, "ar", 2.5)
    inn += fproc(cx - 110, 374, 220, 50, "④ 注入 Inject", "送入 LLM 窗口", GREEN, 15)
    inn += arrow(cx, 424, cx, 450, "ar", 2.5)
    inn += fproc(cx - 110, 450, 220, 50, "⑤ 回收 Forget", "过期清理 · 记忆隔离", ORANGE, 15)
    inn += txt(60, 542, "该透明的透明，该遮挡的遮挡——上下文工程就是给 AI 装一块“聪明的挡风玻璃”。", 13, MUTED, 400)
    return wrap(w, h, inn)

def fig_flow_verification():
    w, h = 860, 660
    cx = 360
    inn = ''
    inn += txt(60, 52, "验证流水线：一道道关，过不了就打回", 22, WHITE, 800, "start", 0, -0.5)
    inn += fstart(cx - 100, 70, 200, 50, "Agent 产出", ORANGE)
    gates = [("自动测试", ORANGE, 170), ("静态检查", AMBER, 270),
             ("独立审查", GREEN, 370), ("人工审批", ORANGE, 470)]
    prev_y = 120
    for (t, c, y) in gates:
        inn += arrow(cx, prev_y, cx, y - 46, "ar", 2.2)
        inn += fdec(cx, y, 46, "通过?", c, 15)
        inn += (f'<path d="M {cx-46} {y} C 150 {y}, 150 250, {cx-100} 95" fill="none" '
                f'stroke="{c}" stroke-width="2" stroke-dasharray="6 5" marker-end="url(#arO)" opacity="0.55"/>')
        inn += txt(120, y, "否→打回", 11, c, 600, "middle")
        prev_y = y + 46
    inn += arrow(cx, 516, cx, 560, "ar", 2.5)
    inn += fstart(cx - 100, 560, 200, 50, "合并 / 上线", GREEN)
    inn += txt(60, 630, "每一道关卡都过不了就打回重做——验证（Verification）是 Harness 质量的最后一道闸。", 13, MUTED, 400)
    return wrap(w, h, inn)

if __name__ == "__main__":
    save("fig_cover_car.svg", fig_cover_car())
    save("fig_five_generations.svg", fig_five_generations())
    save("fig_harness_5subs.svg", fig_harness_5subs())
    save("fig_harness_7layers.svg", fig_harness_7layers())
    save("fig_triple_paradox.svg", fig_triple_paradox())
    save("fig_agent_loop.svg", fig_agent_loop())
    save("fig_react.svg", fig_react())
    save("fig_context_funnel.svg", fig_context_funnel())
    save("fig_chatbot_vs_agent.svg", fig_chatbot_vs_agent())
    save("fig_auto_org.svg", fig_auto_org())
    # 新增：架构图 & 流程图
    save("fig_arch_system.svg", fig_arch_system())
    save("fig_arch_toolcall.svg", fig_arch_toolcall())
    save("fig_arch_multagent.svg", fig_arch_multagent())
    save("fig_flow_task.svg", fig_flow_task())
    save("fig_flow_context_pipeline.svg", fig_flow_context_pipeline())
    save("fig_flow_verification.svg", fig_flow_verification())
    print("DONE")
