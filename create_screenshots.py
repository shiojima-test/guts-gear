#!/usr/bin/env python3
"""Generate UI mockup screenshots for the 環境マッピングマップ PowerPoint"""

from PIL import Image, ImageDraw, ImageFont
import os

OUT = "/home/user/guts-gear/screenshots"
os.makedirs(OUT, exist_ok=True)

# Fonts
JP = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
EN = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
EN_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def font(size, bold=False, jp=True):
    try:
        if jp:
            return ImageFont.truetype(JP, size)
        return ImageFont.truetype(EN_BOLD if bold else EN, size)
    except:
        return ImageFont.load_default()

# Colors
NAVY = (30, 48, 96)       # #1E3060
BLUE2 = (47, 110, 181)    # #2F6EB5
ACCENT = (91, 155, 213)   # #5B9BD5
TEAL = (58, 171, 168)     # #3AABA8
ORANGE = (232, 138, 10)   # #E88A0A
BLUE_S = (46, 142, 196)   # #2E8EC4
WHITE = (255, 255, 255)
BG = (240, 244, 248)      # #f0f4f8
PANEL = (255, 255, 255)
BORDER = (221, 228, 236)
TEXT = (26, 36, 51)
TEXT2 = (74, 96, 128)
TEXT3 = (143, 170, 187)
GREEN = (93, 197, 115)
YELLOW = (240, 192, 64)
RED = (229, 90, 78)

# Facility data (subset for display)
FACILITIES = [
    ("IW", "交流", "国立岩手山青少年交流の家", "岩手県", 78),
    ("BD", "交流", "国立磐梯青少年交流の家", "福島県", 65),
    ("AK", "交流", "国立赤城青少年交流の家", "群馬県", 52),
    ("NT", "交流", "国立能登青少年交流の家", "石川県", 71),
    ("NR", "交流", "国立乗鞍青少年交流の家", "岐阜県", 45),
    ("CH", "交流", "国立中央青少年交流の家", "静岡県", 82),
    ("AW", "交流", "国立淡路青少年交流の家", "兵庫県", 69),
    ("SB", "交流", "国立三瓶青少年交流の家", "島根県", 58),
    ("HD", "自然", "国立日高青少年自然の家", "北海道", 73),
    ("HN", "自然", "国立花山青少年自然の家", "宮城県", 61),
    ("NK", "自然", "国立那須甲子青少年自然の家", "福島県", 48),
    ("ST", "自然", "国立信州高遠青少年自然の家", "長野県", 55),
    ("MY", "自然", "国立妙高青少年自然の家", "新潟県", 67),
]

def score_color(s):
    if s >= 75: return TEAL
    if s >= 55: return GREEN
    if s >= 35: return YELLOW
    return RED

def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = bbox
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def draw_header(draw, w, y0=0):
    """Draw the header bar"""
    draw.rectangle([0, y0, w, y0+52], fill=PANEL)
    draw.line([0, y0+52, w, y0+52], fill=BORDER, width=1)
    draw.text((14, y0+16), "国立青少年教育施設 環境マッピングマップ", fill=TEXT, font=font(14))
    draw.line([350, y0+14, 350, y0+38], fill=BORDER, width=1)
    draw.text((360, y0+20), "高校情報II データサイエンス授業用", fill=TEXT3, font=font(9))
    # Serial button
    draw_rounded_rect(draw, [w-260, y0+12, w-160, y0+40], 7, fill=TEAL)
    draw.text((w-252, y0+17), "シリアル接続", fill=WHITE, font=font(10))
    # Status
    draw.ellipse([w-140, y0+21, w-134, y0+27], fill=ORANGE)
    draw.text((w-128, y0+18), "デモモード", fill=TEXT3, font=font(10))

def draw_ctrl_strip(draw, w, y0=52):
    """Draw the control strip with season/time buttons"""
    draw.rectangle([0, y0, w, y0+36], fill=(245, 248, 251))
    draw.line([0, y0+36, w, y0+36], fill=BORDER, width=1)
    draw.text((14, y0+12), "季節", fill=TEXT3, font=font(9))
    seasons = [("🌸 春", False), ("☀️ 夏", True), ("🍂 秋", False), ("❄️ 冬", False)]
    x = 50
    for label, active in seasons:
        bx = x + 5
        by = y0 + 6
        bw = 55
        bh = 24
        if active:
            draw_rounded_rect(draw, [bx, by, bx+bw, by+bh], 12, fill=TEAL)
            draw.text((bx+10, by+5), label, fill=WHITE, font=font(11))
        else:
            draw_rounded_rect(draw, [bx, by, bx+bw, by+bh], 12, fill=None, outline=BORDER, width=1)
            draw.text((bx+10, by+5), label, fill=TEXT3, font=font(11))
        x += 62
    draw.line([x+10, y0+8, x+10, y0+28], fill=BORDER, width=1)
    draw.text((x+20, y0+12), "時間帯", fill=TEXT3, font=font(9))
    times = [("朝", False), ("昼", True), ("夕", False), ("夜", False)]
    x += 60
    for label, active in times:
        bx = x + 5
        by = y0 + 6
        bw = 50
        bh = 24
        if active:
            draw_rounded_rect(draw, [bx, by, bx+bw, by+bh], 12, fill=TEAL)
            draw.text((bx+12, by+5), label, fill=WHITE, font=font(11))
        else:
            draw_rounded_rect(draw, [bx, by, bx+bw, by+bh], 12, fill=None, outline=BORDER, width=1)
            draw.text((bx+12, by+5), label, fill=TEXT3, font=font(11))
        x += 57
    draw.text((w-80, y0+12), "夏・昼", fill=TEXT3, font=font(9))

def draw_status_bar(draw, w, y0=88):
    """Draw the status bar"""
    draw.rectangle([0, y0, w, y0+26], fill=PANEL)
    draw.line([0, y0+26, w, y0+26], fill=BORDER, width=1)
    draw.ellipse([14, y0+9, 20, y0+15], fill=ORANGE)
    draw.text((26, y0+6), "デモモード稼働中 — 29施設", fill=TEXT2, font=font(10))
    draw.text((w-140, y0+6), "2025/01/15 14:30", fill=TEXT3, font=font(10))

def draw_sidebar_left(draw, x0, y0, w, h, highlight_idx=-1):
    """Draw the left sidebar with facility list"""
    draw.rectangle([x0, y0, x0+w, y0+h], fill=PANEL)
    draw.line([x0+w, y0, x0+w, y0+h], fill=BORDER, width=1)

    # Metrics grid
    metrics = [
        ("平均温度", "26.3℃", TEAL),
        ("平均湿度", "58.2%", BLUE_S),
        ("平均照度", "687lx", ORANGE),
        ("平均CO2", "512ppm", GREEN),
    ]
    my = y0 + 8
    for i, (lbl, val, col) in enumerate(metrics):
        mx = x0 + 10 + (i % 2) * 132
        mrow = my + (i // 2) * 48
        draw_rounded_rect(draw, [mx, mrow, mx+125, mrow+42], 7, fill=(245, 248, 251), outline=BORDER)
        draw.text((mx+8, mrow+6), lbl, fill=TEXT3, font=font(8))
        draw.text((mx+8, mrow+20), val, fill=col, font=font(14))

    # Separator
    my = y0 + 112
    draw.line([x0, my, x0+w, my], fill=BORDER, width=1)

    # Facility list
    draw.text((x0+14, my+6), "交流の家", fill=TEXT3, font=font(9))
    fy = my + 22
    for i, (fid, ftype, fname, region, score) in enumerate(FACILITIES):
        if fy + 50 > y0 + h:
            break
        col = ORANGE if ftype == "交流" else TEAL
        bg = (245, 253, 252) if i == highlight_idx else PANEL
        border_c = TEAL if i == highlight_idx else BORDER

        if ftype == "自然" and i > 0 and FACILITIES[i-1][1] == "交流":
            draw.text((x0+14, fy+2), "自然の家", fill=TEXT3, font=font(9))
            fy += 18

        draw_rounded_rect(draw, [x0+8, fy, x0+w-8, fy+46], 8, fill=bg, outline=border_c, width=1)
        # Score badge
        sc = score_color(score)
        draw_rounded_rect(draw, [x0+14, fy+8, x0+42, fy+22], 4, fill=sc)
        draw.text((x0+17, fy+9), str(score), fill=WHITE, font=font(8))
        # Name
        short_name = fname.replace("国立", "").replace("青少年交流の家", "").replace("青少年自然の家", "")
        draw.text((x0+48, fy+6), short_name, fill=TEXT, font=font(10))
        draw.text((x0+48, fy+20), region, fill=TEXT3, font=font(8))
        # Mini bars
        for bi in range(4):
            bx = x0 + 48 + bi * 55
            draw.rectangle([bx, fy+34, bx+45, fy+37], fill=BORDER)
            bw = int(45 * (0.3 + 0.6 * ((score + bi * 13) % 100) / 100))
            draw.rectangle([bx, fy+34, bx+bw, fy+37], fill=sc)
        fy += 50

def draw_map_area(draw, x0, y0, w, h):
    """Draw map area with markers"""
    draw.rectangle([x0, y0, x0+w, y0+h], fill=(230, 237, 240))
    # Grid lines for map feel
    for gx in range(x0, x0+w, 60):
        draw.line([gx, y0, gx, y0+h], fill=(218, 225, 230), width=1)
    for gy in range(y0, y0+h, 60):
        draw.line([x0, gy, x0+w, gy], fill=(218, 225, 230), width=1)

    # Simplified Japan shape
    draw.text((x0+w//2-30, y0+10), "OpenStreetMap", fill=TEXT3, font=font(9))

    # Draw markers at rough positions
    marker_positions = [
        (0.55, 0.15, "IW", 78, "交流"), (0.52, 0.28, "BD", 65, "交流"),
        (0.48, 0.32, "AK", 52, "交流"), (0.35, 0.30, "NT", 71, "交流"),
        (0.38, 0.38, "NR", 45, "交流"), (0.50, 0.42, "CH", 82, "交流"),
        (0.32, 0.50, "AW", 69, "交流"), (0.22, 0.42, "SB", 58, "交流"),
        (0.20, 0.48, "ET", 62, "交流"), (0.18, 0.58, "OS", 70, "交流"),
        (0.12, 0.62, "AS", 55, "交流"), (0.08, 0.88, "ON", 88, "交流"),
        (0.55, 0.08, "HD", 73, "自然"), (0.52, 0.20, "HN", 61, "自然"),
        (0.42, 0.35, "MY", 67, "自然"), (0.38, 0.35, "TY", 60, "自然"),
        (0.32, 0.45, "WK", 64, "自然"), (0.40, 0.40, "ST", 55, "自然"),
        (0.15, 0.55, "YT", 57, "自然"), (0.10, 0.60, "YS", 66, "自然"),
        (0.48, 0.40, "OC", 74, "その他"),
    ]
    for rx, ry, fid, score, ftype in marker_positions:
        mx = x0 + int(w * rx)
        my = y0 + int(h * ry)
        sc = score_color(score)
        border_c = ORANGE if ftype == "交流" else TEAL if ftype == "自然" else BLUE_S
        r = 16
        draw.ellipse([mx-r, my-r, mx+r, my+r], fill=sc, outline=border_c, width=3)
        draw.text((mx-8, my-6), str(score), fill=WHITE, font=font(10))

def draw_legend(draw, x0, y0):
    """Draw the legend box"""
    lw, lh = 140, 200
    draw_rounded_rect(draw, [x0, y0, x0+lw, y0+lh], 8, fill=PANEL, outline=BORDER)
    draw.text((x0+10, y0+8), "快適スコア", fill=TEXT, font=font(10))
    items = [
        (TEAL, "75〜 快適"), (GREEN, "55〜75 良好"),
        (YELLOW, "35〜55 普通"), (RED, "〜35 不快"),
    ]
    ly = y0 + 28
    for col, label in items:
        draw.ellipse([x0+10, ly+2, x0+20, ly+12], fill=col)
        draw.text((x0+26, ly), label, fill=TEXT2, font=font(10))
        ly += 20
    draw.line([x0+10, ly, x0+lw-10, ly], fill=BORDER, width=1)
    ly += 6
    types = [(ORANGE, "交流の家"), (TEAL, "自然の家"), (BLUE_S, "その他")]
    for col, label in types:
        draw.ellipse([x0+10, ly+2, x0+20, ly+12], fill=WHITE, outline=col, width=3)
        draw.text((x0+26, ly), label, fill=TEXT2, font=font(10))
        ly += 20

def draw_sidebar_right(draw, x0, y0, w, h, active_tab="season"):
    """Draw the right sidebar with data panels"""
    draw.rectangle([x0, y0, x0+w, y0+h], fill=PANEL)
    draw.line([x0, y0, x0, y0+h], fill=BORDER, width=1)

    # Tab bar
    tabs = [("季節", "season"), ("分布", "dist"), ("相関", "corr"), ("時系列", "ts"), ("異常", "anom"), ("CSV", "csv")]
    tw = w // len(tabs)
    for i, (label, tid) in enumerate(tabs):
        tx = x0 + i * tw
        active = tid == active_tab
        if active:
            draw.rectangle([tx, y0, tx+tw, y0+30], fill=(245, 253, 252))
            draw.line([tx, y0+28, tx+tw, y0+28], fill=TEAL, width=2)
            draw.text((tx+tw//2-12, y0+8), label, fill=TEAL, font=font(10))
        else:
            draw.text((tx+tw//2-12, y0+8), label, fill=TEXT3, font=font(10))
    draw.line([x0, y0+30, x0+w, y0+30], fill=BORDER, width=1)

    py = y0 + 40
    if active_tab == "season":
        draw.text((x0+12, py), "現在のパターン", fill=TEXT3, font=font(9))
        py += 18
        info_lines = [
            "季節: ☀️ 夏 (6〜8月)",
            "時間帯: ☀️ 昼 (10:00〜15:00)",
            "特徴: 全国的に高温多湿",
            "日射量が最も多い時間帯",
        ]
        for line in info_lines:
            draw.text((x0+12, py), line, fill=TEXT2, font=font(11))
            py += 20
        py += 10
        draw.text((x0+12, py), "全施設の平均値", fill=TEXT3, font=font(9))
        py += 18
        draw_rounded_rect(draw, [x0+12, py, x0+w-12, py+80], 7, fill=(245, 248, 251), outline=BORDER)
        stats = ["温度: 26.3℃", "湿度: 58.2%", "照度: 687 lx", "CO2: 512 ppm"]
        for j, s in enumerate(stats):
            draw.text((x0+22, py+8+j*18), s, fill=TEXT2, font=font(10))
        py += 96
        draw.text((x0+12, py), "データサイエンスのヒント", fill=TEXT3, font=font(9))
        py += 18
        draw_rounded_rect(draw, [x0+12, py, x0+w-12, py+90], 7, fill=(245, 253, 252), outline=None)
        draw.line([x0+12, py, x0+15, py+90], fill=TEAL, width=3)
        hints = [
            "季節や時間帯を変更すると、",
            "気温・湿度・照度・CO2の値が変化",
            "📈 相関タブで「緯度×温度」を選ぶと",
            "北の施設ほど気温が低い傾向が見えます",
        ]
        for j, h in enumerate(hints):
            draw.text((x0+22, py+8+j*20), h, fill=TEXT2, font=font(10))

    elif active_tab == "corr":
        draw.text((x0+12, py), "X軸", fill=TEXT3, font=font(9))
        draw_rounded_rect(draw, [x0+12, py+14, x0+w//2-6, py+34], 6, fill=(245, 248, 251), outline=BORDER)
        draw.text((x0+18, py+17), "📍 緯度", fill=TEXT2, font=font(10))
        draw.text((x0+w//2+6, py), "Y軸", fill=TEXT3, font=font(9))
        draw_rounded_rect(draw, [x0+w//2+6, py+14, x0+w-12, py+34], 6, fill=(245, 248, 251), outline=BORDER)
        draw.text((x0+w//2+12, py+17), "🌡 温度", fill=TEXT2, font=font(10))
        py += 50
        # Scatter plot area
        cx, cy = x0+30, py+10
        cw, ch = w-60, 160
        draw_rounded_rect(draw, [cx-2, cy-2, cx+cw+2, cy+ch+2], 6, fill=WHITE, outline=BORDER)
        # Axes
        draw.line([cx, cy+ch, cx+cw, cy+ch], fill=TEXT3, width=1)
        draw.line([cx, cy, cx, cy+ch], fill=TEXT3, width=1)
        # Scatter dots (simulating negative correlation lat vs temp)
        import random
        random.seed(42)
        for i in range(25):
            lat = 26 + i * 0.7
            temp = 32 - (lat - 26) * 0.5 + random.uniform(-2, 2)
            dx = int((lat - 26) / 18 * cw)
            dy = int((1 - (temp - 15) / 25) * ch)
            draw.ellipse([cx+dx-4, cy+dy-4, cx+dx+4, cy+dy+4], fill=TEAL, outline=None)
        # Trend line
        draw.line([cx+10, cy+30, cx+cw-10, cy+ch-20], fill=RED, width=2)
        py += ch + 20
        # Stats
        draw_rounded_rect(draw, [x0+12, py, x0+w-12, py+50], 7, fill=(245, 248, 251), outline=BORDER)
        draw.text((x0+22, py+8), "相関係数 r = -0.847", fill=TEXT2, font=font(10))
        draw.text((x0+22, py+26), "回帰式: y = -0.45x + 42.1", fill=TEXT2, font=font(10))

    elif active_tab == "dist":
        draw.text((x0+12, py), "項目を選択", fill=TEXT3, font=font(9))
        draw_rounded_rect(draw, [x0+12, py+14, x0+w-12, py+34], 6, fill=(245, 248, 251), outline=BORDER)
        draw.text((x0+18, py+17), "🌡 温度 (℃)", fill=TEXT2, font=font(10))
        py += 50
        draw.text((x0+12, py), "ヒストグラム", fill=TEXT3, font=font(9))
        py += 16
        # Histogram
        cx, cy = x0+30, py
        cw, ch = w-60, 100
        draw_rounded_rect(draw, [cx-2, cy-2, cx+cw+2, cy+ch+2], 6, fill=WHITE, outline=BORDER)
        bar_heights = [20, 35, 60, 85, 70, 45, 25, 15]
        bw = cw // len(bar_heights)
        for i, bh in enumerate(bar_heights):
            draw.rectangle([cx+i*bw+2, cy+ch-bh, cx+(i+1)*bw-2, cy+ch], fill=TEAL)
        py += ch + 20
        draw.text((x0+12, py), "箱ひげ図", fill=TEXT3, font=font(9))
        py += 16
        # Box plot
        cx2, cy2 = x0+30, py
        ch2 = 60
        draw_rounded_rect(draw, [cx2-2, cy2-2, cx2+cw+2, cy2+ch2+2], 6, fill=WHITE, outline=BORDER)
        bx_mid = cx2 + cw//2
        draw.line([bx_mid-80, cy2+ch2//2, bx_mid+80, cy2+ch2//2], fill=TEXT3, width=1)  # whiskers
        draw.rectangle([bx_mid-40, cy2+15, bx_mid+40, cy2+ch2-15], fill=None, outline=TEAL, width=2)
        draw.line([bx_mid, cy2+15, bx_mid, cy2+ch2-15], fill=ORANGE, width=2)  # median
        py += ch2 + 20
        draw_rounded_rect(draw, [x0+12, py, x0+w-12, py+80], 7, fill=(245, 248, 251), outline=BORDER)
        bstats = ["平均: 26.3℃", "中央値: 26.0℃", "標準偏差: 3.8℃", "範囲: 18.2〜33.1℃"]
        for j, s in enumerate(bstats):
            draw.text((x0+22, py+8+j*18), s, fill=TEXT2, font=font(10))

def draw_popup(draw, x0, y0):
    """Draw a marker popup"""
    pw, ph = 260, 200
    draw_rounded_rect(draw, [x0, y0, x0+pw, y0+ph], 10, fill=PANEL, outline=BORDER)
    # Shadow effect
    # Header
    draw.rectangle([x0+1, y0+1, x0+pw-1, y0+60], fill=PANEL)
    draw.line([x0, y0+60, x0+pw, y0+60], fill=BORDER, width=1)
    # Badge
    draw_rounded_rect(draw, [x0+12, y0+12, x0+42, y0+26], 4, fill=ORANGE)
    draw.text((x0+16, y0+13), "交流", fill=WHITE, font=font(8))
    draw.text((x0+48, y0+10), "国立中央青少年交流の家", fill=TEXT, font=font(11))
    draw.text((x0+48, y0+26), "静岡県 御殿場市", fill=TEXT3, font=font(9))
    draw.text((x0+12, y0+42), "N35.29  500m  スコア: 82", fill=TEXT3, font=font(9))

    # Sensor bars
    sensors = [
        ("🌡", "温度", 25.8, "℃", 0.65, TEAL),
        ("💧", "湿度", 55.3, "%", 0.55, BLUE_S),
        ("💡", "照度", 720, "lx", 0.72, ORANGE),
        ("🌿", "CO2", 490, "ppm", 0.40, GREEN),
    ]
    by = y0 + 70
    for icon, lbl, val, unit, pct, col in sensors:
        draw.text((x0+12, by), lbl, fill=TEXT3, font=font(9))
        # Bar background
        draw.rectangle([x0+50, by+4, x0+170, by+8], fill=BORDER)
        # Bar fill
        draw.rectangle([x0+50, by+4, x0+50+int(120*pct), by+8], fill=col)
        # Value
        vstr = str(int(val)) if isinstance(val, (int, float)) and val == int(val) else f"{val}"
        draw.text((x0+180, by), vstr, fill=TEXT, font=font(11))
        draw.text((x0+220, by+2), unit, fill=TEXT3, font=font(8))
        by += 28


# ═══════════════════════════════════════════
# Generate all screenshots
# ═══════════════════════════════════════════

W, H = 1400, 900

# Screenshot 1: Full page
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)
draw_header(draw, W)
draw_ctrl_strip(draw, W)
draw_status_bar(draw, W)
draw_sidebar_left(draw, 0, 114, 280, H-114)
draw_map_area(draw, 280, 114, W-280-350, H-114)
draw_legend(draw, W-350-160, H-220)
draw_sidebar_right(draw, W-350, 114, 350, H-114, "season")
img.save(f"{OUT}/01_full.png")
print("01_full.png done")

# Screenshot 2: Sidebar left (facility list)
img2 = Image.new("RGB", (320, 700), BG)
draw2 = ImageDraw.Draw(img2)
draw_sidebar_left(draw2, 10, 10, 300, 680, highlight_idx=5)
img2.save(f"{OUT}/02_sidebar.png")
print("02_sidebar.png done")

# Screenshot 3: Right panel - season tab
img3 = Image.new("RGB", (400, 600), BG)
draw3 = ImageDraw.Draw(img3)
draw_sidebar_right(draw3, 10, 10, 380, 580, "season")
img3.save(f"{OUT}/03_right_season.png")
print("03_right_season.png done")

# Screenshot 3b: Right panel - correlation tab
img3b = Image.new("RGB", (400, 600), BG)
draw3b = ImageDraw.Draw(img3b)
draw_sidebar_right(draw3b, 10, 10, 380, 580, "corr")
img3b.save(f"{OUT}/03b_right_corr.png")
print("03b_right_corr.png done")

# Screenshot 3c: Right panel - distribution tab
img3c = Image.new("RGB", (400, 600), BG)
draw3c = ImageDraw.Draw(img3c)
draw_sidebar_right(draw3c, 10, 10, 380, 580, "dist")
img3c.save(f"{OUT}/03c_right_dist.png")
print("03c_right_dist.png done")

# Screenshot 4: Header + control strip
img4 = Image.new("RGB", (W, 120), BG)
draw4 = ImageDraw.Draw(img4)
draw_header(draw4, W)
draw_ctrl_strip(draw4, W)
img4.save(f"{OUT}/04_header.png")
print("04_header.png done")

# Screenshot 5: Popup
img5 = Image.new("RGB", (300, 240), BG)
draw5 = ImageDraw.Draw(img5)
draw_popup(draw5, 20, 20)
img5.save(f"{OUT}/05_popup.png")
print("05_popup.png done")

# Screenshot 6: Legend
img6 = Image.new("RGB", (180, 240), BG)
draw6 = ImageDraw.Draw(img6)
draw_legend(draw6, 20, 20)
img6.save(f"{OUT}/06_legend.png")
print("06_legend.png done")

print("All screenshots generated!")
