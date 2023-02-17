from selenium.webdriver.remote.webelement import WebElement
from py_mega_sena.services.csv.csv_service import CsvService
from py_mega_sena.services.selenium.selenium_mega_service import SeleniumMegaService


def run() -> None:
    """ Run Scraping Mega Sena"""
    csv_service = CsvService()
    selenium_service = SeleniumMegaService()

    filename: str = 'original_data.csv'

    selenium_service.set_next_page()
    rows: list[WebElement] = selenium_service.get_rows()
    columns: list[str] = selenium_service.get_thead_columns()
    csv_service.update(filename, columns, rows, selenium_service.runner) if csv_service.is_file(
        filename) else csv_service.create(filename, columns, rows, selenium_service.runner)
    selenium_service.exit()


if __name__ == '__main__':
    run()
