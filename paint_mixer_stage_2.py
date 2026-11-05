# === Stage 2: Проверка полей ===
# Project: PaintMixer
import re
from datetime import datetime


VALID_DATE_FORMATS = ("%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y")


def normalize_name(value):
    return re.sub(r"\s+", " ", value.strip())


def normalize_hex(value):
    hex_clean = value.strip().lstrip("#")
    if re.fullmatch(r"[0-9a-fA-F]{6}", hex_clean):
        return "#" + hex_clean
    if re.fullmatch(r"[0-9a-fA-F]{3}", hex_clean):
        return "#" + "".join(c * 2 for c in hex_clean)
    return None


def normalize_volume(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def normalize_date(value):
    value = value.strip()
    for fmt in VALID_DATE_FORMATS:
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue
    return None


def validate_recipe(name, hex_color, volume, date):
    errors = {}

    if not name or not name.strip():
        errors["name"] = "Введите название рецепта"
    else:
        name = normalize_name(name)
        if len(name) > 100:
            errors["name"] = "Название слишком длинное (максимум 100 символов)"

    if hex_color:
        hex_color = normalize_hex(hex_color)
        if hex_color is None:
            errors["hex_color"] = "Неверный оттенок. Ожидаю HEX вида #RRGGBB или RGB"
    elif not hex_color:
        errors["hex_color"] = "Укажите оттенок рецепта"

    if volume is not None:
        volume = normalize_volume(volume)
        if volume is None:
            errors["volume"] = "Объём должен быть числом"
        elif volume <= 0:
            errors["volume"] = "Объём должен быть положительным"
        else:
            volume = round(volume, 2)
    else:
        errors["volume"] = "Укажите объём рецепта"

    if date:
        date = normalize_date(date)
        if date is None:
            errors["date"] = "Неверный формат даты. Ожидаю ДД.ММ.ГГГГ или ГГГГ-ММ-ДД"
    elif not date:
        errors["date"] = "Укажите дату создания рецепта"

    return errors
