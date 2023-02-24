import os
import csv
from datetime import datetime
from selenium.webdriver.remote.webelement import WebElement


class CsvService:
    def __init__(self) -> None:
        self.base_file = os.path.join(os.getcwd(), 'assets')

    def is_file(self, filename: str) -> bool:
        return os.path.isfile(self.get_path(filename))

    def get_path(self, filename) -> str:
        return os.path.join(self.base_file, filename)

    def get_files(self, filename: str) -> list[str]:
        with open(self.get_path(filename), mode='r', encoding='utf-8') as file_reader:
            return list(csv.reader(file_reader, delimiter=';'))

    def save_csv_headers(self, filename, data) -> None:
        with open(self.get_path(filename), mode='w', encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(data)
            f.close()

    def save_csv_data(self, filename, data) -> None:
        with open(self.get_path(filename), mode='r', encoding='utf-8') as file_reader:
            reader = csv.reader(file_reader)
            next(reader, None)

            with open(self.get_path(filename), mode='a', encoding='utf-8') as fwriter:
                writer = csv.writer(fwriter, delimiter=';')
                print(f"Logged::{datetime.now()}::{data}")
                writer.writerow(data)
            file_reader.close()
            fwriter.close()

    def create(self, filename: str, columns: list[str], rows: list[WebElement], runner) -> None:
        print("::: CSV Create Data :::")
        self.save_csv_headers(filename, columns)
        runner(filename, columns, rows, None, self.save_csv_data)

        print("::: CSV Finished :::")

    def update(self, filename: str, columns: list[str], rows: list[WebElement], runner) -> None:
        print("::: CSV Update Data :::")
        with open(self.get_path(filename), mode='r', encoding='utf-8') as file_reader:
            readers = list(csv.reader(file_reader, delimiter=';'))
            file_reader.close()

        index = readers.index(readers[-1])

        if len(rows[index:]) > 0:
            runner(filename, columns, rows, index, self.save_csv_data)

        print("::: CSV Finished :::")
