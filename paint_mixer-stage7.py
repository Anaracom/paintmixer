# === Stage 7: Генерация идентификаторов ===
# Project: PaintMixer
import string
import secrets


PROJECT_PREFIX = "pmx"


def _generate_unique_id(project_prefix, counter, used_ids):
    """Генерация уникального идентификатора с префиксом проекта.

    Формат: {prefix}-{random-4-символа}-{sequence}.
    Случайная часть обеспечивает низкую вероятность коллизии,
    последовательность гарантирует уникальность при повторных вызовах.
    """
    alphabet = string.ascii_letters + string.digits
    random_part = "".join(secrets.choice(alphabet) for _ in range(4))
    sequence = counter + 1
    candidate = f"{project_prefix}-{random_part}-{sequence}"
    while candidate in used_ids:
        sequence += 1
        candidate = f"{project_prefix}-{random_part}-{sequence}"
    used_ids.add(candidate)
    return candidate


def generate_unique_id(project_prefix, counter, used_ids):
    """Генерация уникального идентификатора для сущности проекта.

    Args:
        project_prefix: префикс проекта (например, "pmx").
        counter: текущий счётчик сгенерированных идентификаторов.
        used_ids: множество уже сгенерированных идентификаторов.

    Returns:
        Уникальный идентификатор строкового типа.
    """
    return _generate_unique_id(project_prefix, counter, used_ids)


if __name__ == "__main__":
    used_ids = set()
    counter = 0
    for _ in range(10):
        counter += 1
        print(generate_unique_id(PROJECT_PREFIX, counter, used_ids))
