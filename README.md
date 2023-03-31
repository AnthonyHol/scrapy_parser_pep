# Парсинг документации Python (PEP) при помощи Scrapy
## Спринт 19 — scrapy_parser_pep

## Описание проекта
Асинхронный парсер, собирающий данные (номер, название и статус) о Python Enhancement Proposals (PEP) с сайта https://www.python.org/, а также формирующий сводку по количеству PEP каждого статуса в отдельный .csv файл.

### Технологии
- Python 3.11.0
- Scrapy 2.5.1

## Запуск проекта
1. Установить виртуальное окружение (Linux)
```
python3 -m venv env
source venv/bin/activate
```

2. Установить требующиеся зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

3. Запуск парсера
```
scrapy crawl pep
```
