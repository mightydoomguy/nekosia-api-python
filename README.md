# NekosiaAPI-py

Простая обёртка над [Nekosia API](https://nekosia.cat) — один файл, одна зависимость.

## Установка

Скопируй `NekosiaAPI.py` в свой проект и установи зависимость:

```bash
pip install -r requirments.txt
```

## Использование

```python
from NekosiaAPI import Nekosia

# одна картинка — ссылка
url = Nekosia.get_image_url("catgirl")


# полный JSON
data = Nekosia.get_image("catgirl")

# несколько картинок
urls = Nekosia.get_image_with_count("headphones", count=5)

# теги
Nekosia.get_list_of_tags() 
```

Полный рабочий пример — в `client.py`.

## Методы

| Метод | Возвращает |
|---|---|
| `Nekosia.get_image(tag="random")` | полный JSON (`dict`) |
| `Nekosia.get_image_with_count(tag="random", count=5)` | `list[str]` |
| `Nekosia.get_list_of_tags()` | `list[str]` |


## Лицензия

MIT — см. [LICENSE](LICENSE).  
Изображения принадлежат их авторам (см. `attribution.artist` в ответе API).
