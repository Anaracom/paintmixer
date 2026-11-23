# === Stage 9: Текстовый поиск ===
# Project: PaintMixer
import re


class RecipeSearch:
    """Поиск рецептов по текстовым полям без учёта регистра с подсветкой совпадений."""

    TEXT_FIELDS = ("name", "shade")

    def __init__(self, recipes):
        self.recipes = recipes

    def search(self, query):
        if not query:
            return []
        return [self._highlight(recipe) for recipe in self.recipes if self._matches(recipe, query)]

    def _matches(self, recipe, query):
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        return any(pattern.search(value) for value in self.TEXT_FIELDS if getattr(recipe, value))

    def _highlight(self, recipe):
        query = re.escape(recipe.query)
        pattern = re.compile(query, re.IGNORECASE)
        name = pattern.sub(lambda m: f"\\g<0>\\0", getattr(recipe, self.TEXT_FIELDS[0]))
        shade = pattern.sub(lambda m: f"\\g<0>\\0", getattr(recipe, self.TEXT_FIELDS[1]))
        return f"<b>{name}</b> ({shade})"
