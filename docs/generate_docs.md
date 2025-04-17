# Інструкція з генерації документації за допомогою Sphinx

Цей проєкт використовує **Sphinx** для автоматичної генерації документації з Python-коду.

## Крок 1: Встановлення Sphinx

У терміналі виконайте команду:

```bash
pip install sphinx
```

## Крок 2: Ініціалізація документації (виконується один раз)

```bash
sphinx-quickstart
```

Рекомендується обрати:
- Відокремлення source та build директорій (`y`)
- Назва проєкту: Trajectory Calculator
- Автор: Alina Sokolova

## Крок 3: Налаштування `conf.py`

У файлі `docs/source/conf.py` потрібно:
- Додати шлях до проєкту:
```python
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```
- Переконатись, що додано `'sphinx.ext.autodoc'` до `extensions`

## Крок 4: Створення `*.rst` файлу для модулів

```bash
sphinx-apidoc -o source ..
```

Це згенерує файли документації для всіх Python-модулів у проєкті.

## Крок 5: Генерація HTML-документації

Перейдіть у папку `docs` і виконайте:

```bash
python -m sphinx source build/html
```

## Крок 6: Перевірка

Відкрийте `docs/build/html/index.html` у браузері для перегляду документації.

## Примітка

Документація створена з використанням docstring-коментарів у коді Python.
