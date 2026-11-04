# === Stage 1: Каркас модуля ===
# Project: PaintMixer
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Recipe:
    title: str
    shade: str
    volume: float
    date: date = field(default_factory=date.today)


def demo_records() -> list[Recipe]:
    return [
        Recipe("Бежевый базовый", "beige", 0.5),
        Recipe("Синий глубокий", "blue", 0.25),
        Recipe("Зелёный спокойный", "green", 0.75),
        Recipe("Красный яркий", "red", 0.1),
        Recipe("Серый нейтральный", "gray", 1.0),
    ]


def main() -> None:
    records = demo_records()
    print("PaintMixer — демо-рецепты")
    print("=" * 30)
    for index, recipe in enumerate(records, start=1):
        print(f"{index}. {recipe.title} ({recipe.shade})")
        print(f"   Объём: {recipe.volume} л")
        print(f"   Дата:  {recipe.date.isoformat()}")
        print()


if __name__ == "__main__":
    main()
