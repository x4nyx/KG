def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    v = cmax

    if cmax == 0:
        s = 0
    else:
        s = delta / cmax

    if delta == 0:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / delta) + 360) % 360
    elif cmax == g:
        h = (60 * ((b - r) / delta) + 120) % 360
    elif cmax == b:
        h = (60 * ((r - g) / delta) + 240) % 360

    return int(round(h)), int(round(s * 100)), int(round(v * 100))


def cmyk_to_rgb(c, m, y, k):
    c, m, y, k = c / 100.0, m / 100.0, y / 100.0, k / 100.0

    r = round(255 * (1 - c) * (1 - k))
    g = round(255 * (1 - m) * (1 - k))
    b = round(255 * (1 - y) * (1 - k))

    return int(r), int(g), int(b)


def hsv_to_rgb(h, s, v):
    h /= 60.0
    s /= 100.0
    v /= 100.0

    hi = int(h) % 6
    f = h - int(h)

    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    if hi == 0:
        return int(round(v * 255)), int(round(t * 255)), int(round(p * 255))
    elif hi == 1:
        return int(round(q * 255)), int(round(v * 255)), int(round(p * 255))
    elif hi == 2:
        return int(round(p * 255)), int(round(v * 255)), int(round(t * 255))
    elif hi == 3:
        return int(round(p * 255)), int(round(q * 255)), int(round(v * 255))
    elif hi == 4:
        return int(round(t * 255)), int(round(p * 255)), int(round(v * 255))
    else:
        return int(round(v * 255)), int(round(p * 255)), int(round(q * 255))


def rgb_to_cmyk(r, g, b):
    # Нормализация значений RGB в диапазоне [0, 1]
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    # Нахождение максимального значения среди R, G и B
    cmax = max(r, g, b)

    # Вычисление значений C, M, Y, и K
    k = 1 - cmax
    c = (1 - r - k) / (1 - k) if (1 - k) != 0 else 0
    m = (1 - g - k) / (1 - k) if (1 - k) != 0 else 0
    y = (1 - b - k) / (1 - k) if (1 - k) != 0 else 0

    # Преобразование значений C, M, Y, и K в проценты
    c, m, y, k = round(c * 100), round(m * 100), round(y * 100), round(k * 100)

    return int(c), int(m), int(y), int(k)

def hex_to_rgb(hex_color):
    # Удаляем символ # и извлекаем компоненты R, G и B
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
    return r, g, b

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))