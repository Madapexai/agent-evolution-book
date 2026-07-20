# -*- coding: utf-8 -*-
"""
小红书宣传海报生成器 · 手绘插画风格（仿参考图）
白底 + 彩色高亮关键词 + 手绘图标 + 立体楼梯/卡片布局
产出 6 张 SVG 到 assets/xhs_handdrawn/
"""
import os, html, math

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "xhs_handdrawn")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

# ---- 手绘风调色板 ----
BG = "#fefefe"
BG_WARM = "#fffef8"
INK_DARK = "#2d2d2d"
INK_MED = "#555555"
BLUE = "#4a90e2"
BLUE_LIGHT = "#7eb3f0"
PURPLE = "#8b6ec9"
ORANGE = "#f5a623"
GREEN = "#50b87c"
RED = "#e86c60"
YELLOW = "#f7d154"
TEAL = "#5bc0be"
PINK = "#e88fb0"

FONT = "Noto Sans CJK SC, PingFang SC, Microsoft YaHei, sans-serif"
W, H = 1080, 1440
PAD_X = 64

def esc(s): return html.escape(str(s), quote=False)

def txt(x, y, s, size=20, fill=INK_DARK, weight=700, anchor="start", op=1):
    return ('<text x="%d" y="%d" font-family="%s" font-size="%d" '
            'font-weight="%d" fill="%s" text-anchor="%s" opacity="%.1f">%s</text>'
            ) % (x, y, FONT, size, weight, fill, anchor, op, esc(s))

def hand_rect(x, y, w, h, fill="#ffffff", stroke=INK_MED, sw=2, rx=12):
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="%d" ry="%d" '
            'fill="%s" stroke="%s" stroke-width=%.1f" stroke-linejoin="round"/>'
            ) % (x, y, w, h, rx, rx, fill, stroke, sw)

def badge_num(cx, cy, num, bg_color, size=28, tc="#ffffff"):
    r = int(size * 0.85)
    s = ('<circle cx="%d" cy="%d" r="%d" fill="%s"/>'
         '<text x="%d" y="%d" font-family="%s" font-size="%d" font-weight="800"'
         ' fill="%s" text-anchor="middle">%s</text>'
        ) % (cx, cy, r, bg_color, cx, cy + int(size*0.32), FONT, size, tc, str(num))
    return s

def underline(y, x_start, x_end, color=YELLOW, thickness=6, rx=3):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" fill="%s"/>' % (
        x_start, y, x_end-x_start, thickness, rx, color)

def mlines(x, y, lines, size=15, fill=INK_MED, gap=22, anchor="middle", weight=400):
    return ''.join(txt(x, y + i * gap, ln, size, fill, weight, anchor) for i, ln in enumerate(lines))

# ============================================================
# 图标库（用 % 格式化，避免 f-string 括号问题）
# ============================================================
def _g(x, y, sc):
    return '<g transform="translate(%d,%d) scale(%f)">' % (x, y, sc)
_endg = '</g>'

def icon_car(x, y, sc=1, body_color=ORANGE):
    c = body_color
    g = _g(x, y, sc)
    g += '<rect x="0" y="16" width="80" height="32" rx="10" fill="%s" stroke="%s" stroke-width="2"/>' % (c, INK_MED)
    g += '<path d="M18 16 Q30 -4 54 -4 Q70 -4 76 16 Z" fill="%s" stroke="%s" stroke-width="2"/>' % (c, INK_MED)
    g += '<path d="M22 14 Q32 0 48 0 Q62 0 68 14 Z" fill="#e8f0fe" opacity="0.7"/>'
    g += '<circle cx="22" cy="52" r="12" fill="%s" stroke="%s" stroke-width="3"/><circle cx="58" cy="52" r="12" fill="%s" stroke="%s" stroke-width="3"/>' % (INK_DARK, c, INK_DARK, c)
    g += '<circle cx="22" cy="52" r="5" fill="#ddd"/><circle cx="58" cy="52" r="5" fill="#ddd"/>'
    g += '<circle cx="78" cy="34" r="4" fill="#fff3cd"/>'
    g += _endg
    return g

def icon_brain(x, y, sc=1):
    g = _g(x, y, sc)
    g += '<path d="M25 5 Q35 0 45 5 Q55 0 65 5 Q72 15 68 28 Q75 40 65 50 Q70 60 60 65 Q50 75 40 70 Q30 75 20 65 Q10 60 15 50 Q5 40 12 28 Q8 15 25 5Z" fill="%s" stroke="%s" stroke-width="2"/>' % (PINK, INK_MED)
    g += '<path d="M30 20 Q40 15 50 20 M28 32 Q40 27 52 32 M30 44 Q40 39 50 44" fill="none" stroke="%s" stroke-width="1.5"/>' % INK_MED
    g += _endg
    return g

def icon_gear(x, y, sc=1, col=None):
    c = col or PURPLE
    g = _g(x, y, sc)
    for i in range(8):
        ang = i * math.pi / 4
        tx = math.cos(ang) * 28
        ty = math.sin(ang) * 28
        ra = ang * 180 / math.pi
        g += '<rect x="%.1f" y="%.1f" width="8" height="12" rx="3" fill="%s" transform="rotate(%.1f %.1f %.1f)" opacity="0.9"/>' % (tx-4, ty-6, c, ra, tx, ty)
    g += '<circle cx="0" cy="0" r="14" fill="%s" stroke="%s" stroke-width="2"/><circle cx="0" cy="0" r="8" fill="%s" stroke="%s" stroke-width="1.5"/>' % (c, INK_MED, BG, INK_MED)
    g += _endg
    return g

def icon_book(x, y, sc=1):
    g = _g(x, y, sc)
    g += '<path d="M0 8 Q20 0 40 8 L40 56 Q20 48 0 56Z" fill="%s" stroke="%s" stroke-width="2"/><path d="M40 8 Q60 0 80 8 L80 56 Q60 48 40 56Z" fill="%s" stroke="%s" stroke-width="2"/>' % (BLUE_LIGHT, INK_MED, BLUE, INK_MED)
    g += '<line x1="40" y1="8" x2="40" y2="56" stroke="%s" stroke-width="2"/>' % INK_MED
    for k in range(3):
        g += '<line x1="8" y1="%d" x2="32" y2="%d" stroke="%s" stroke-width="1.5" opacity="0.4"/>' % (20+k*10, 20+k*10, INK_MED)
        g += '<line x1="48" y1="%d" x2="72" y2="%d" stroke="%s" stroke-width="1.5" opacity="0.4"/>' % (20+k*10, 20+k*10, INK_MED)
    g += _endg
    return g

def icon_chat(x, y, sc=1):
    g = _g(x, y, sc)
    g += '<path d="M0 0 Q0 -24 28 -24 L56 -24 Q84 -24 84 0 Q84 24 56 24 L20 24 L4 38 L10 24 L0 24Q0 24 0 0Z" fill="%s" stroke="%s" stroke-width="2"/>' % (GREEN, INK_MED)
    g += '<line x1="16" y1="-4" x2="68" y2="-4" stroke="#fff" stroke-width="2.5" opacity="0.7"/>'
    g += '<line x1="16" y1="8" x2="52" y2="8" stroke="#fff" stroke-width="2.5" opacity="0.7"/>'
    g += _endg
    return g

def icon_tool(x, y, sc=1):
    g = _g(x, y, sc)
    g += '<path d="M8 52 L36 24 A16 16 0 1 1 52 8 L24 36 L8 52Z" fill="%s" stroke="%s" stroke-width="2"/>' % (ORANGE, INK_MED)
    g += '<circle cx="46" cy="14" r="8" fill="none" stroke="%s" stroke-width="2"/>' % INK_MED
    g += _endg
    return g

def icon_lock(x, y, sc=1, color=RED):
    g = _g(x, y, sc)
    g += '<rect x="4" y="20" width="40" height="32" rx="6" fill="%s" stroke="%s" stroke-width="2"/>' % (color, INK_MED)
    g += '<path d="M14 20 L14 12 Q14 0 24 0 Q34 0 34 12 L34 20" fill="none" stroke="%s" stroke-width="3"/>' % INK_MED
    g += '<circle cx="24" cy="36" r="5" fill="%s"/><line x1="24" y1="36" x2="24" y2="42" stroke="%s" stroke-width="2.5"/>' % (INK_DARK, INK_DARK)
    g += _endg
    return g

def icon_checkmark(x, y, sc=1, color=GREEN):
    g = _g(x, y, sc)
    g += '<circle cx="20" cy="20" r="20" fill="%s" opacity="0.15"/><circle cx="20" cy="20" r="20" fill="none" stroke="%s" stroke-width="2.5"/>' % (color, color)
    g += '<path d="M10 21 L17 28 L31 12" fill="none" stroke="%s" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/>' % color
    g += _endg
    return g

def icon_warning(x, y, sc=1):
    g = _g(x, y, sc)
    g += '<path d="M24 2 L46 42 L2 42Z" fill="%s" stroke="%s" stroke-width="2"/>' % (YELLOW, INK_MED)
    g += txt(24, 34, "!", 26, INK_DARK, 800, "middle")
    g += _endg
    return g

def icon_loop_arrow(x, y, sc=1, color=PURPLE):
    g = _g(x, y, sc)
    g += '<path d="M0 -32 A32 32 0 1 1 -22 -22" fill="none" stroke="%s" stroke-width="4" stroke-linecap="round"/>' % color
    g += '<path d="M-22 -22 l -4 10 l12 -2 z" fill="%s"/>' % color
    g += '<circle r="20" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="6 4" opacity="0.5"/><circle r="6" fill="%s" opacity="0.3"/>' % (color, color)
    g += _endg
    return g

def icon_fleet(x, y, sc=1):
    g = _g(x, y, sc)
    positions = [(0, 0, 0.7, ORANGE), (-30, 28, 0.55, BLUE), (30, 28, 0.55, GREEN)]
    for px, py, ps, pc in positions:
        g += icon_car(px, py, ps, pc)
    g += _endg
    return g

def adjust(hex_c, amt):
    h = hex_c.lstrip('#')
    r = max(0,min(255,int(h[0:2],16)+amt))
    gv = max(0,min(255,int(h[2:4],16)+amt))
    b = max(0,min(255,int(h[4:6],16)+amt))
    return '#%02x%02x%02x' % (r,gv,b)

# ============================================================
# 立体楼梯绘制
# ============================================================
def draw_stairs(x, y, steps_data, step_w=420, step_h=82):
    n = len(steps_data)
    g = ''
    for i in range(n - 1, -1, -1):
        num, label, sub_label, color, icon_svg = steps_data[i]
        sx = x + (n - 1 - i) * 36
        sy = y + i * step_h
        depth = 30
        # 侧面立体
        sp = '%d,%d %d,%d %d,%d %d,%d' % (
            sx+step_w, sy+step_h, sx+step_w+depth, sy+step_h-depth,
            sx+depth, sy+step_h-depth, sx, sy+step_h)
        g += '<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.5" opacity="0.6"/>' % (sp, adjust(color,-20), INK_MED)
        # 正面台阶
        g += hand_rect(sx, sy, step_w, step_h, "#ffffff", INK_MED, 1.8, 10)
        # 顶边3D线
        tp = '%d,%d %d,%d %d,%d %d,%d' % (sx, sy, sx+depth, sy-depth, sx+step_w+depth, sy-depth, sx+step_w, sy)
        g += '<polygon points="%s" fill="none" stroke="%s" stroke-width="1.5" opacity="0.4"/>' % (tp, INK_MED)
        # 编号
        g += badge_num(sx + 44, sy + step_h/2, num, color, 26)
        # 图标
        if icon_svg:
            g += '<g transform="translate(%d,%d)">%s</g>' % (sx + 100, sy + step_h/2 - 22, icon_svg)
        # 文字
        g += txt(sx + 150, sy + step_h/2 - 2, label, 26, INK_DARK, 800, "start")
        g += txt(sx + 150, sy + step_h/2 + 28, sub_label, 16, INK_MED, 400, "start")
    # 左侧箭头
    ax, ay = x - 20, y + n*step_h - 60
    g += '<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="8 6" opacity="0.7"/>' % (ax, ay+120, ax-30, ay+60, ax, ay, BLUE)
    g += '<path d="M%d,%d L%d,%d L%d,%d" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>' % (ax-8, ay+12, ax, ay, ax+12, ay+8, BLUE)
    # 右下角小植物
    gx = x + step_w + n*36 + 20
    gy = y + n*step_h - 40
    g += '<g transform="translate(%d,%d)" opacity="0.6"><ellipse cx="0" cy="20" rx="18" ry="8" fill="%s" opacity="0.3"/>' % (gx, gy, GREEN)
    g += '<path d="M0 20 Q-10 0 -4 -16 M0 20 Q10 0 4 -16 M0 20 Q0 -5 0 -18" fill="none" stroke="%s" stroke-width="2.5"/>' % GREEN
    g += '<circle cx="-4" cy="-16" r="4" fill="%s" opacity="0.6"/><circle cx="4" cy="-16" r="4" fill="%s" opacity="0.6"/><circle cx="0" cy="-18" r="4" fill="%s" opacity="0.6"/></g>' % (GREEN, GREEN, GREEN)
    # 闪光
    for dx, dy, sz in [(50, -20, 12), (70, -40, 8), (90, -10, 6)]:
        g += '<g transform="translate(%d,%d)"><path d="M0-%d Q0 0 %d 0 Q0 0 0 %d Q0 0 -%d 0 Q0 0 0-%dZ" fill="%s" opacity="0.5"/></g>' % (gx+dx, gy+dy, sz, sz, sz, sz, sz, YELLOW)
    return g

def card_row(x, y, cards, card_w=300, card_h=200, gap=24):
    g = ''
    for i, (label, desc, color, icon_fn) in enumerate(cards):
        cx = x + i * (card_w + gap)
        g += hand_rect(cx, y, card_w, card_h, "#ffffff", color, 2, 16)
        g += '<rect x="%d" y="%d" width="%d" height="8" rx="4" fill="%s"/>' % (cx, y, card_w, color)
        if icon_fn:
            g += '<g transform="translate(%d,%d)">%s</g>' % (cx + card_w/2 - 30, y + 36, icon_fn(0, 0, 0.9))
        g += txt(cx + card_w/2, y + 110, label, 24, INK_DARK, 700, "middle")
        g += mlines(cx + card_w/2, y + 140, [desc], 15, INK_MED, 22, "middle")
    return g

def comparison_split(lt, li, rt, ri, x, y, w, h, lc=RED, rc=GREEN):
    g = ''
    mid = x + w / 2
    pd = 36
    hw = w/2 - pd/2
    # 左半
    g += hand_rect(x, y, hw, h, adjust(lc,-35), lc, 2, 16)
    g += txt(mid - w/4, y + 50, lt, 30, lc, 800, "middle")
    ly = y + 100
    for item in li:
        g += txt(mid - w/4 + 20, ly, "X  " + item, 19, INK_DARK, 500, "start"); ly += 38
    # 右半
    g += hand_rect(mid + pd/2, y, hw, h, adjust(rc,-35), rc, 2, 16)
    g += txt(mid + w/4, y + 50, rt, 30, rc, 800, "middle")
    ry = y + 100
    for item in ri:
        g += txt(mid + w/4 + 20, ry, "V  " + item, 19, INK_DARK, 500, "start"); ry += 38
    # VS
    g += txt(mid, y + h/2, "VS", 36, ORANGE, 900, "middle")
    return g

def wrap(inner):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">\n%s\n</svg>' % (W, H, W, H, inner)

def save(name, svg):
    p = os.path.join(OUT, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name, len(svg), "bytes")

# ============================================================
# 图 1 · AI 的七层关系（复刻参考图风格）
# ============================================================
def poster_01():
    inner = '<rect width="%d" height="%d" fill="%s"/>' % (W, H, BG_WARM)
    
    title = "AI 的七层关系"
    inner += txt(PAD_X, 100, title, 76, BLUE, 800, "start")
    inner += underline(114, PAD_X, PAD_X + len(title)*52, YELLOW, 7, 3)
    
    lines_y = 170; lh = 52
    paragraphs = [
        [("你说出", INK_DARK), ("提示词", ORANGE), ("，交给", INK_DARK), ("Agent", ORANGE), ("大管家；", INK_DARK)],
        [("所有沟通内容拆成", INK_DARK), ("Token", GREEN), ("记录，全部存入", INK_DARK), ("上下文", GREEN), ("备忘录；", INK_DARK)],
        [("Harness", PURPLE), ("家规全程约束管家行为，不乱干活；", INK_DARK)],
        [("管家通过", INK_DARK), ("MCP", RED), ("联络中枢，外接各类资源；", INK_DARK)],
        [("再调用自身的", INK_DARK), ("Skills", ORANGE), ("技能，一步步自主完成你交代的所有任务", INK_DARK)],
    ]
    for parts in paragraphs:
        cx = PAD_X
        for text, color in parts:
            inner += txt(cx, lines_y, text, 26, color or INK_DARK, 400, "start")
            cx += len(text) * 28 + 2
        lines_y += lh
    
    steps = [
        ("1", "Token", "模型理解的最小单位", PURPLE, icon_gear(0,0,0.6)),
        ("2", "提示词", "告诉模型要做什么", BLUE, icon_chat(0,0,0.55)),
        ("3", "上下文", "提供相关背景信息", GREEN, icon_book(0,0,0.55)),
        ("4", "Agent", "自主决策与执行的智能体", ORANGE, icon_car(0,0,0.55)),
        ("5", "Harness", "编排与运行的工程框架", PURPLE, icon_gear(0,0,0.6)),
        ("6", "MCP", "连接与扩展的协议层", RED, icon_tool(0,0,0.55)),
        ("7", "Skills", "可复用的能力与经验", ORANGE, icon_checkmark(0,0,0.6)),
    ]
    inner += draw_stairs(PAD_X + 20, 620, steps, step_w=480, step_h=92)
    
    inner += txt(W - PAD_X, H - 50, "《智驾时代：Agent 进化简史》", 18, INK_MED, 400, "end", 0.7)
    return wrap(inner)

# ============================================================
# 图 2 · 什么是 Agent
# ============================================================
def poster_02():
    inner = '<rect width="%d" height="%d" fill="%s"/>' % (W, H, BG_WARM)
    inner += txt(PAD_X, 90, "01  ", 64, BLUE, 800, "start")
    inner += txt(PAD_X + 90, 90, "什么是 Agent", 64, INK_DARK, 800, "start")
    inner += underline(104, PAD_X, W - PAD_X*2, BLUE_LIGHT, 7, 3)
    
    dy = 150
    inner += hand_rect(PAD_X, dy, W - PAD_X*2, 160, "#f0f6ff", BLUE, 2, 18)
    inner += txt(PAD_X + 30, dy + 55, "Agent 就是一辆会自己开的「智能车」——它不只是陪你聊天，", 24, INK_DARK, 500, "start")
    inner += txt(PAD_X + 30, dy + 100, "而是真正替你做事：读文件、写代码、跑测试、发邮件……", 24, INK_DARK, 500, "start")
    
    inner += comparison_split(
        "Chatbot 聊天机器人", ["只会说不会做","你问一句它答一句","方向盘在你手里"],
        "Agent 智能体", ["能说又能干","自己规划并执行","方向盘交出去了"],
        PAD_X, 360, W - PAD_X*2, 340)
    
    qy = 750
    inner += hand_rect(PAD_X + 40, qy, W - PAD_X*2 - 80, 140, "#fff8e6", ORANGE, 2, 18)
    inner += txt(W/2, qy + 58, "ChatGPT 是副驾陪聊的朋友，Agent 是替你开车的司机", 26, INK_DARK, 600, "middle")
    
    parts = [
        ("大脑", "LLM 做所有决策", PURPLE, icon_brain),
        ("视野", "上下文决定能看到什么", BLUE, icon_book),
        ("工具", "手脚与真实世界交互", ORANGE, icon_tool),
        ("安全", "Harness 刹车与交规", RED, icon_lock),
        ("记忆", "短期+长期知识存储", GREEN, icon_book),
        ("记录", "可观测与可审计", TEAL, lambda x,y,s: icon_checkmark(x,y,s,TEAL)),
    ]
    cw, ch, gap = 310, 180, 24
    inner += card_row(PAD_X + 20, 930, parts[:3], cw, ch, gap)
    inner += card_row(PAD_X + 20, 930 + ch + 24, parts[3:], cw, ch, gap)
    
    inner += txt(W - PAD_X, H - 50, "《智驾时代：Agent 进化简史》", 18, INK_MED, 400, "end", 0.7)
    return wrap(inner)

# ============================================================
# 图 3 · 五代演化楼梯
# ============================================================
def poster_03():
    inner = '<rect width="%d" height="%d" fill="%s"/>' % (W, H, BG_WARM)
    inner += txt(PAD_X, 80, "02  ", 64, ORANGE, 800, "start")
    inner += txt(PAD_X + 90, 80, "Agent 的五代演化", 64, INK_DARK, 800, "start")
    inner += underline(94, PAD_X, W - PAD_X*2, YELLOW, 7, 3)
    inner += txt(PAD_X, 155, "从「手摇启动」到「全自动驾驶」，不是替代而是层层叠加", 23, INK_MED, 500, "start")
    
    steps = [
        ("1", "Prompt", "手摇启动 · 会聊天的提示词", ORANGE, icon_chat(0,0,0.5)),
        ("2", "Context", "视野开启 · 带上记忆与资料", BLUE, icon_book(0,0,0.5)),
        ("3", "Harness", "装上底盘 · 能调用工具的安全系统", PURPLE, icon_gear(0,0,0.55)),
        ("4", "Loop", "自主驱动 · 自己规划、反思、重试", GREEN, icon_loop_arrow(0,0,0.6)),
        ("5", "Auto-Org", "组队进化 · 多智能体自组织", TEAL, icon_fleet(0,0,0.55)),
    ]
    inner += draw_stairs(PAD_X + 40, 230, steps, step_w=520, step_h=108)
    
    iy = 1320
    inner += hand_rect(PAD_X + 30, iy, W - PAD_X*2 - 60, 90, "#f0fff4", GREEN, 2, 16)
    inner += txt(W/2, iy + 55, "新范式不是淘汰旧的，而是把旧的包起来变成更大系统的一部分", 22, INK_DARK, 600, "middle")
    inner += txt(W - PAD_X, H - 50, "《智驾时代：Agent 进化简史》", 18, INK_MED, 400, "end", 0.7)
    return wrap(inner)

# ============================================================
# 图 4 · Harness 公式 + 红绿灯
# ============================================================
def poster_04():
    inner = '<rect width="%d" height="%d" fill="%s"/>' % (W, H, BG_WARM)
    inner += txt(PAD_X, 80, "03  ", 64, RED, 800, "start")
    inner += txt(PAD_X + 90, 80, "Agent 的核心公式", 64, INK_DARK, 800, "start")
    inner += underline(94, PAD_X, W - PAD_X*2, YELLOW, 7, 3)
    
    fy = 170
    inner += hand_rect(PAD_X + 40, fy, W - PAD_X*2 - 80, 180, "#fff5f0", RED, 3, 24)
    inner += txt(W/2, fy + 75, "Agent", 52, INK_DARK, 800, "middle")
    inner += txt(W/2, fy + 130, "=   LLM（聪明的大脑）  +  Harness（安全系统）", 32, INK_DARK, 600, "middle")
    
    qy = 390
    inner += txt(PAD_X + 30, qy, "没有 Harness 的 Agent，就像没有刹车的跑车——", 26, RED, 600, "start")
    inner += txt(PAD_X + 30, qy + 44, "跑得越快，死得越惨", 28, INK_DARK, 800, "start")
    
    light_y = 500
    lights = [
        ("红灯 · 绝对禁止", "删数据库、改生产配置\n系统直接拦截，碰都不能碰", RED),
        ("黄灯 · 需要确认", "删文件、改配置、部署上线\nAI 说清楚原因，人点头才能干", ORANGE),
        ("绿灯 · 自动执行", "读文件、跑测试、写代码\n只读操作或容易回滚，放手去做", GREEN),
    ]
    lw, lh, lgap = 310, 220, 28
    lx0 = (W - (3*lw + 2*lgap)) / 2
    for i, (t, d, col) in enumerate(lights):
        lx = lx0 + i*(lw + lgap)
        inner += hand_rect(lx, light_y, lw, lh, "#ffffff", col, 2.5, 18)
        inner += '<rect x="%d" y="%d" width="%d" height="10" rx="5" fill="%s"/>' % (lx, light_y, lw, col)
        inner += txt(lx + lw/2, light_y + 50, t, 22, col, 700, "middle")
        for j, ln in enumerate(d.split('\n')):
            inner += txt(lx + lw/2, light_y + 90 + j*32, ln, 17, INK_MED, 400, "middle")
    
    sy = 780
    inner += txt(PAD_X, sy, "Harness 五大子系统（从输入到输出的完整闭环）：", 24, INK_DARK, 600, "start")
    subs = [("Context","看到什么","前挡风玻璃",BLUE),("Memory","记住什么","导航+记录仪",PURPLE),
             ("Tool","能做什么","机械手+工具箱",ORANGE),("Policy","不能做什么","刹车+交规",RED),
             ("Verification","做对了没","质检+路考",GREEN)]
    ssy = sy + 50
    for i,(nm,q,a,c) in enumerate(subs):
        sx = PAD_X + (i%3)*340; siy = ssy + (i//3)*100
        inner += badge_num(sx+20, siy+16, i+1, c, 22)
        inner += txt(sx+52, siy+8, nm, 22, c, 700, "start")
        inner += txt(sx+52, siy+36, "-> %s  (%s)" % (q, a), 17, INK_MED, 400, "start")
    
    inner += txt(W - PAD_X, H - 50, "《智驾时代：Agent 进化简史》", 18, INK_MED, 400, "end", 0.7)
    return wrap(inner)

# ============================================================
# 图 5 · 三重悖论
# ============================================================
def poster_05():
    inner = '<rect width="%d" height="%d" fill="%s"/>' % (W, H, BG_WARM)
    inner += txt(PAD_X, 80, "04  ", 64, PURPLE, 800, "start")
    inner += txt(PAD_X + 90, 80, "三重悖论", 64, INK_DARK, 800, "start")
    inner += underline(94, PAD_X, W - PAD_X*2, PINK, 7, 3)
    inner += txt(PAD_X, 155, "越聪明的 Agent，反而越矛盾？三个「反过来」拆不开", 23, INK_MED, 500, "start")
    
    paradoxes = [
        ("1 记忆悖论", "记越多，反而越糊涂",
         ["记忆的核心不是「存储」，而是「选择」","信息塞太满，有用的那条反而不显眼","业界现在拼的是「谁忘得聪明」，不是谁记得多"],
         ORANGE, icon_book),
        ("2 推理悖论", "脚手架越复杂，故障越多",
         ["用 Harness 补模型推理的不足","但脚手架本身会制造新问题","补一个洞，可能在别处戳出三个洞"],
         PURPLE, icon_gear),
        ("3 进化悖论", "想改自己，谁来当裁判？",
         ["Agent 想自己改进自己","但自己评自己，越评越高（退化循环）","只有引入更高层的外部验证，改进才持久"],
         RED, icon_loop_arrow),
    ]
    cw2 = W - PAD_X*2; ch2 = 320; cy = 210; cgap = 24
    for ttle, sub, bullets, col, icfn in paradoxes:
        inner += hand_rect(PAD_X, cy, cw2, ch2, "#ffffff", col, 2, 18)
        inner += '<rect x="%d" y="%d" width="%d" height="8" rx="4" fill="%s"/>' % (PAD_X, cy, cw2, col)
        inner += icfn(PAD_X + 50, cy + ch2/2 - 30, 1.0)
        inner += txt(PAD_X + 120, cy + 50, ttle, 30, col, 800, "start")
        inner += txt(PAD_X + 120, cy + 90, sub, 22, INK_DARK, 600, "start")
        by = cy + 130
        for b in bullets:
            inner += txt(PAD_X + 120, by, "*  " + b, 19, INK_MED, 400, "start"); by += 38
        cy += ch2 + cgap
    
    smy = 1240
    inner += hand_rect(PAD_X + 30, smy, W - PAD_X*2 - 60, 100, "#faf0ff", PURPLE, 2, 16)
    inner += txt(W/2, smy + 58, "三者互相缠绕形成闭环：记忆需要推理筛选 -> 推理需要记忆 -> 进化需要两者评估", 20, INK_DARK, 550, "middle")
    inner += txt(W - PAD_X, H - 50, "《智驾时代：Agent 进化简史》", 18, INK_MED, 400, "end", 0.7)
    return wrap(inner)

# ============================================================
# 图 6 · Builder vs Reviewer
# ============================================================
def poster_06():
    inner = '<rect width="%d" height="%d" fill="%s"/>' % (W, H, BG_WARM)
    inner += txt(PAD_X, 80, "05  ", 64, TEAL, 800, "start")
    inner += txt(PAD_X + 90, 80, "AI 不能给自己打分", 64, INK_DARK, 800, "start")
    inner += underline(94, PAD_X, W - PAD_X*2, TEAL, 7, 3)
    
    qy = 150
    inner += hand_rect(PAD_X, qy, W - PAD_X*2, 100, "#fff0f0", RED, 2, 16)
    inner += txt(PAD_X + 30, qy + 40, "让 AI 检查自己的工作 = 让考生自己改卷子 -> 分数只会越判越高", 24, RED, 600, "start")
    inner += txt(PAD_X + 30, qy + 78, "因为写代码和检查用的是同一个大脑，犯的错大概率也发现不了", 19, INK_MED, 400, "start")
    
    scene_y = 290; bw2, bh2 = 440, 380
    inner += hand_rect(PAD_X, scene_y, bw2, bh2, "#f0f8ff", BLUE, 2, 18)
    inner += '<rect x="%d" y="%d" width="%d" height="8" rx="4" fill="%s"/>' % (PAD_X, scene_y, bw2, BLUE)
    inner += txt(PAD_X + bw2/2, scene_y + 50, "Builder 建造者", 28, BLUE, 800, "middle")
    inner += txt(PAD_X + bw2/2, scene_y + 90, "目标：把事情做成", 19, INK_MED, 400, "middle")
    inner += '<g transform="translate(%d,%d)"><g transform="scale(0.9)">%s</g></g>' % (PAD_X+bw2/2-40, scene_y+120, icon_car(0,0,1,BLUE))
    bt = ["V  建设性思维 —— 怎么实现","V  关注功能、效率、进度","V  可以修改文件、执行命令","X  容易放过自己的错误"]
    ty = scene_y + 220
    for t in bt:
        cc = INK_DARK if t.startswith("V") else RED
        inner += txt(PAD_X + 30, ty, t, 19, cc, 500, "start"); ty += 36
    
    rx = W - PAD_X - bw2
    inner += hand_rect(rx, scene_y, bw2, bh2, "#f0fff4", GREEN, 2, 18)
    inner += '<rect x="%d" y="%d" width="%d" height="8" rx="4" fill="%s"/>' % (rx, scene_y, bw2, GREEN)
    inner += txt(rx + bw2/2, scene_y + 50, "Reviewer 审查者", 28, GREEN, 800, "middle")
    inner += txt(rx + bw2/2, scene_y + 90, "目标：把好质量关", 19, INK_MED, 400, "middle")
    inner += '<g transform="translate(%d,%d)"><g transform="scale(1.0)">%s</g></g>' % (rx+bw2/2-30, scene_y+120, icon_checkmark(0,0,1))
    rt = ["V  批判性思维 —— 哪里有问题","V  关注质量、安全、规范","X  只能读取，不能修改","V  专门挑刺找漏洞"]
    ty = scene_y + 220
    for t in rt:
        cc = INK_DARK if t.startswith("V") else GREEN
        inner += txt(rx + 30, ty, t, 19, cc, 500, "start"); ty += 36
    
    inner += txt(W/2, scene_y + bh2/2, "! 互\n搏", 28, ORANGE, 800, "middle")
    
    conc_y = 720
    inner += hand_rect(PAD_X + 40, conc_y, W - PAD_X*2 - 80, 120, "#fff8e6", ORANGE, 2, 18)
    inner += txt(W/2, conc_y + 45, "矛盾产生真相", 28, ORANGE, 800, "middle")
    inner += txt(W/2, conc_y + 85, "一个想快点做完，一个确保没问题 —— 互相博弈、互相校正，质量才靠谱", 20, INK_DARK, 500, "middle")
    
    vy = 880
    inner += txt(PAD_X, vy, "三层验证法（从基础到终极）：", 24, INK_DARK, 600, "start")
    vsteps = [("1","运行检查","能不能跑起来？",BLUE),("2","独立审查","做得对不对？",PURPLE),("3","明确通过条件","算不算完成？",GREEN)]
    vyy = vy + 48
    for nm,vn,vd,c in vsteps:
        inner += badge_num(PAD_X+20, vyy+14, nm, c, 24)
        inner += txt(PAD_X+56, vyy+8, vn, 22, c, 700, "start")
        inner += txt(PAD_X+56, vyy+36, vd, 17, INK_MED, 400, "start")
        vyy += 72
    
    inner += txt(W - PAD_X, H - 50, "《智驾时代：Agent 进化简史》", 18, INK_MED, 400, "end", 0.7)
    return wrap(inner)

if __name__ == "__main__":
    save("hd_01_七层关系.svg", poster_01())
    save("hd_02_什么是Agent.svg", poster_02())
    save("hd_03_五代演化.svg", poster_03())
    save("hd_04_Harness公式.svg", poster_04())
    save("hd_05_三重悖论.svg", poster_05())
    save("hd_06_双Agent互搏.svg", poster_06())
    print("done.")
