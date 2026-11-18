# === Stage 6: Связи между сущностями ===
# Project: PaintMixer
from datetime import date


class Pigment:
    def __init__(self, name, batch, batch_date, remaining, used):
        self.name = name
        self.batch = batch
        self.batch_date = batch_date
        self.remaining = remaining
        self.used = used

    def __repr__(self):
        return (f"Pigment(name={self.name!r}, batch={self.batch!r}, "
                f"batch_date={self.batch_date!r}, remaining={self.remaining}, "
                f"used={self.used})")


class Recipe:
    def __init__(self, name, tint, volume, date):
        self.name = name
        self.tint = tint
        self.volume = volume
        self.date = date


def get_pigments_for_recipe(recipe, pigments):
    recipe_pigments = []
    for pigment in pigments:
        if pigment.name == recipe.tint:
            recipe_pigments.append(pigment)
    return recipe_pigments


def check_integrity(recipe, pigments):
    recipe_pigments = get_pigments_for_recipe(recipe, pigments)
    if len(recipe_pigments) == 0:
        return False
    for pigment in recipe_pigments:
        if pigment.batch is None:
            return False
        if pigment.batch_date is None:
            return False
        if pigment.remaining is None:
            return False
        if pigment.used is None:
            return False
    return True


if __name__ == "__main__":
    p1 = Pigment("красный", 101, date(2023, 5, 10), 500, 200)
    p2 = Pigment("белый", 102, date(2023, 5, 12), 1000, 0)
    p3 = Pigment("синий", 103, date(2023, 5, 15), 300, 150)
    pigments = [p1, p2, p3]

    r1 = Recipe("розовый", "красный", 250, date(2023, 6, 1))
    print("Рецепт:", r1)
    print("Пигменты:", get_pigments_for_recipe(r1, pigments))
    print("Целостность:", check_integrity(r1, pigments))

    r2 = Recipe("бирюзовый", "зелёный", 300, date(2023, 6, 2))
    print("Рецепт:", r2)
    print("Пигменты:", get_pigments_for_recipe(r2, pigments))
    print("Целостность:", check_integrity(r2, pigments))
