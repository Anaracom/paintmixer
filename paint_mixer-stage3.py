# === Stage 3: Хранилище в памяти ===
# Project: PaintMixer
from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional


@dataclass
class Recipe:
    name: str
    shade: str
    volume: float
    created: date = field(default_factory=date.today)


class RecipeStore:
    def __init__(self) -> None:
        self._recipes: Dict[str, Recipe] = {}

    def add(self, recipe: Recipe) -> str:
        recipe_id = str(len(self._recipes) + 1)
        self._recipes[recipe_id] = recipe
        return recipe_id

    def get(self, recipe_id: str) -> Optional[Recipe]:
        return self._recipes.get(recipe_id)

    def list(self) -> List[Recipe]:
        return list(self._recipes.values())

    def __len__(self) -> int:
        return len(self._recipes)


def demo() -> None:
    store = RecipeStore()

    first = Recipe(name="Синий с белым", shade="#4A90D9", volume=500.0)
    second = Recipe(name="Тёмно-зелёный", shade="#2F5233", volume=250.5)

    id1 = store.add(first)
    id2 = store.add(second)

    print("Добавлено рецептов:", len(store))
    print("Рецепт", id1, "->", store.get(id1).name, store.get(id1).shade, store.get(id1).volume)
    print("Рецепт", id2, "->", store.get(id2).name, store.get(id2).shade, store.get(id2).volume)
    print("Все рецепты:")
    for recipe in store.list():
        print("  ", recipe.name, recipe.shade, recipe.volume)

    print("Отсутствует:", store.get("999"))
