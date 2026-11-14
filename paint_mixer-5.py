# === Stage 5: Удаление и восстановление ===
# Project: PaintMixer
import datetime
import uuid


class Recipe:
    def __init__(self, name, shade, volume, created=None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.shade = shade
        self.volume = volume
        self.created = created or datetime.datetime.now()
        self.deleted = False
        self.deleted_at = None
        self.deleted_by = None

    def soft_delete(self, user=None):
        self.deleted = True
        self.deleted_at = datetime.datetime.now()
        self.deleted_by = user

    def restore(self):
        if not self.deleted:
            raise ValueError("Рецепт не удалён")
        self.deleted = False
        self.deleted_at = None
        self.deleted_by = None

    def is_deleted(self):
        return self.deleted

    def __repr__(self):
        if self.deleted:
            return f"<Recipe {self.name!r} (удалён)>"
        return f"<Recipe {self.name!r}>"


class RecipeRepository:
    def __init__(self):
        self._items = []

    def add(self, recipe):
        self._items.append(recipe)

    def all(self):
        return list(self._items)

    def get(self, recipe_id):
        for item in self._items:
            if item.id == recipe_id:
                return item
        return None

    def find_active(self, name=None, shade=None):
        result = []
        for item in self._items:
            if item.is_deleted():
                continue
            if name and item.name != name:
                continue
            if shade and item.shade != shade:
                continue
            result.append(item)
        return result

    def remove(self, recipe_id, user=None):
        recipe = self.get(recipe_id)
        if not recipe:
            raise ValueError(f"Рецепт {recipe_id} не найден")
        recipe.soft_delete(user)
        return recipe

    def recover(self, recipe_id):
        recipe = self.get(recipe_id)
        if not recipe or not recipe.is_deleted():
            raise ValueError(f"Рецепт {recipe_id} нельзя восстановить")
        recipe.restore()
        return recipe

    def purge(self):
        for item in self._items:
            if item.is_deleted():
                self._items.remove(item)
        return len(self._items)


repository = RecipeRepository()

recipe = Recipe(name="Белый + голубой", shade="#e6f2ff", volume=500)
repository.add(recipe)

repository.remove(recipe.id, user="user-1")
print(recipe.is_deleted())

repository.recover(recipe.id)
print(recipe.is_deleted())

print(repository.find_active(shade="#e6f2ff"))

repository.purge()
print(len(repository.all()))
