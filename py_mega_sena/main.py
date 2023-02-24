import os
from selenium.webdriver.remote.webelement import WebElement

from services.mysql.mysql_service import MysqlService
from services.csv.csv_service import CsvService
from services.selenium.selenium_mega_service import SeleniumMegaService

filename: str = 'original_data.csv'

with open(os.path.join(os.getcwd(), '..', '.env'), 'r') as file_env:
    for line in file_env:
        if line.startswith('#') or not line.strip():
            continue

        key, value = line.strip().split('=', 1)
        os.environ[key] = value


def run() -> None:
    """ Run Scraping Mega Sena"""
    csv_service = CsvService()
    selenium_service = SeleniumMegaService()

    selenium_service.set_next_page()
    rows: list[WebElement] = selenium_service.get_rows()
    columns: list[str] = selenium_service.get_thead_columns()

    csv_service.update(filename, columns, rows, selenium_service.runner) if csv_service.is_file(
        filename) else csv_service.create(filename, columns, rows, selenium_service.runner)
    selenium_service.exit()


def test() -> None:
    mysql_service = MysqlService()
    csv_service = CsvService()
    # mega = [2566, '2023-02-18 00:00:00', 11, 23, 45, 53, 57, 59, 0, 60, 3862, 0.00, 36334.95, 806.42, '-', 37812469.50, 9000000.00, 4015967.86, 'Sim', 'Nao', '-']
    # mysql_service.insert_one(mega)
    db_files = mysql_service.find_all(mysql_service.get_cursor())
    local_files = csv_service.get_files(filename)

    if len(db_files) == 0:
        # create new register from zero

        for file in local_files[1:]:
            print(file)
    else:
        # update registers from index
        pass


if __name__ == '__main__':
    # run()
    test()
