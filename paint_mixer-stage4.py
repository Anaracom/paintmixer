# === Stage 4: Редактирование записей ===
# Project: PaintMixer
from datetime import date


class Recipe:
    """Рецепт смешения красок."""

    def __init__(self, name, shade, volume, created):
        self.name = name
        self.shade = shade
        self.volume = volume
        self.created = created

    def update(self, changes):
        """Применить частичное обновление по допустимым полям."""
        allowed = {
            "name": str,
            "shade": str,
            "volume": (int, float),
            "created": date,
        }
        for key, value in changes.items():
            if key not in allowed:
                raise ValueError(f"Недопустимое поле для редактирования: {key!r}")
            if not isinstance(value, allowed[key]):
                raise TypeError(f"Недопустимый тип для поля {key!r}: {type(value).__name__}")
            if key == "volume" and value <= 0:
                raise ValueError(f"Объём не может быть отрицательным: {value}")
            if key == "name" and not value.strip():
                raise ValueError("Название не может быть пустым")
            if key == "created" and value.year < 1900:
                raise ValueError(f"Дата создания вне разумных пределов: {value}")
            setattr(self, key, value)

    def to_dict(self):
        return {
            "name": self.name,
            "shade": self.shade,
            "volume": self.volume,
            "created": self.created.isoformat() if self.created else None,
        }


def edit_recipe(recipe, changes):
    """Редактировать рецепт по идентификатору, применяя проверку полей."""
    recipe.update(changes)
    return recipe.to_dict()


def apply_recipe_patch(recipe, patch):
    """Применить JSON-подобный патч к рецепту, игнорируя неизвестные поля."""
    if isinstance(patch, dict):
        for key, value in patch.items():
            if key in {"name", "shade", "volume", "created"}:
                recipe.update({key: value})
    return recipe
