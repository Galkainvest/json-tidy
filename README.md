[![tests](https://img.shields.io/github/actions/workflow/status/Galkainvest/json-tidy/tests.yml?branch=main)](../../actions)
[![license](https://img.shields.io/github/license/Galkainvest/json-tidy)](LICENSE)

# json-tidy
Маленький інструмент для охайного форматування JSON. Працює з файлом або з stdin.

## Вимоги
- Python 3.10+

## Використання
```bash
# Красивий вивід файлу
python json_tidy.py data.json

# З індентом 4 і сортуванням ключів
python json_tidy.py data.json -i 4 -s

# Через пайп
type data.json | python json_tidy.py -i 2
