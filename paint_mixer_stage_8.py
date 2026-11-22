# === Stage 8: Фильтрация записей ===
# Project: PaintMixer
import datetime


def filter_recipes(
    recipes,
    *,
    shade=None,
    date_from=None,
    date_to=None,
):
    """Фильтрует записи рецептов по оттенку и диапазону дат.

    recipes — список объектов рецептов.
    shade — точное совпадение значения поля «оттенок» или None для всех.
    date_from — начальная граница диапазона дат (включительно) или None.
    date_to — конечная граница диапазона дат (включительно) или None.
    """
    shade = None if shade is None else str(shade)
    date_from = None if date_from is None else _to_date(date_from)
    date_to = None if date_to is None else _to_date(date_to)

    result = []
    for recipe in recipes:
        if shade is not None and str(recipe.shade) != shade:
            continue
        if date_from is not None and recipe.date < date_from:
            continue
        if date_to is not None and recipe.date > date_to:
            continue
        result.append(recipe)
    return result


def _to_date(value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


if __name__ == "__main__":
    sample = [
        {"shade": "красный", "date": datetime.date(2024, 1, 15)},
        {"shade": "синий", "date": datetime.date(2024, 5, 20)},
        {"shade": "красный", "date": datetime.date(2025, 3, 10)},
    ]
    for record in filter_recipes(sample, shade="красный", date_from="2024-01-01", date_to="2024-12-31"):
        print(record["shade"], record["date"])
