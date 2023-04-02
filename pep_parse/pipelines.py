from collections import defaultdict

from pep_parse.constants import BASE_DIR, CUR_TIME, FIELDS_NAME, FILE_NAME


class PepParsePipeline:
    def __init__(self) -> None:
        """Конструктор класса."""
        self.result_dir = BASE_DIR / "results"
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider) -> None:
        """Метод определения словаря для парсинга."""
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        """Метод подсчета кол-ва конкретных статусов."""
        self.results[item["status"]] = self.results.get(item["status"], 0) + 1

        return item

    def close_spider(self, spider) -> None:
        """Метод создания файла со сводкой по статусам PEP."""
        file_dir = self.result_dir / FILE_NAME.format(time=CUR_TIME)

        with open(file_dir, mode="w", encoding="utf-8") as file:
            file.write(f"{FIELDS_NAME[0]}, {FIELDS_NAME[1]}\n")

            for key, value in self.results.items():
                file.write(f"{key},{value}\n")

            total = sum(self.results.values())

            file.write(f"Total, {total}\n")
