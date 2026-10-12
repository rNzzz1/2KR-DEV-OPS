# Практическая работа №2.2 — DevOps Infrastructure

[![Pylint](https://github.com/rNzzz1/2KR-DEV-OPS/actions/workflows/pylint.yml/badge.svg)](https://github.com/rNzzz1/2KR-DEV-OPS/actions/workflows/pylint.yml)

## Описание проекта

Учебный проект по дисциплине **«Инструменты DevOps»** (РТУ МИРЭА, ИПТИП, Кафедра индустриального программирования).  
**Тема:** Основы инфраструктуры проекта: Git-ветвление и автоматизация CI-пайплайна в GitHub Actions.

## Структура репозитория

```text
.
├── .github/
│   └── workflows/
│       └── pylint.yml        # CI-пайплайн для проверки Pull Request в ветку dev
├── src/
│   ├── __init__.py
│   ├── calculator.py         # Математический и статистический модуль
│   └── data_processor.py     # Модуль валидации и обработки данных
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py    # Модульные тесты калькулятора
│   └── test_data_processor.py# Модульные тесты обработки данных
├── requirements.txt          # Зависимости проекта
└── README.md                 # Документация проекта
```

## Требования к окружению

- Python 3.11+
- Git 2.40+
- GitHub Actions runner (`ubuntu-latest`)

## Запуск тестов локально

```bash
python3 -m unittest discover tests
```

## Запуск линтера Pylint

```bash
pip install -r requirements.txt
pylint $(git ls-files '*.py') --output=lint.txt || true
```
