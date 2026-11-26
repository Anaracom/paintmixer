# === Stage 10: Теги ===
# Project: PaintMixer
from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional, Set


@dataclass
class Recipe:
    title: str
    shade: str
    volume: float
    created: date = field(default_factory=date.today)
    tags: Set[str] = field(default_factory=set)


@dataclass
class Pigment:
    name: str
    base_color: str
    inventory: float = 0.0


class RecipeTagManager:
    def __init__(self) -> None:
        self._recipes: Dict[str, Recipe] = {}

    def add_recipe(self, recipe: Recipe) -> None:
        self._recipes[recipe.title] = recipe

    def add_tag(self, title: str, tag: str) -> None:
        recipe = self._recipes.get(title)
        if recipe is None:
            raise KeyError(f"Рецепт '{title}' не найден")
        if tag not in recipe.tags:
            recipe.tags.add(tag)

    def remove_tag(self, title: str, tag: str) -> bool:
        recipe = self._recipes.get(title)
        if recipe is None:
            raise KeyError(f"Рецепт '{title}' не найден")
        if tag in recipe.tags:
            recipe.tags.discard(tag)
            return True
        return False

    def search_by_tag(self, tag: str) -> List[Recipe]:
        return [
            recipe for recipe in self._recipes.values() if tag in recipe.tags
        ]
