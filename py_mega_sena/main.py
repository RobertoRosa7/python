import os
import time


from selenium.webdriver.remote.webelement import WebElement
from services.mysql.mysql_service import MysqlService
from services.csv.csv_service import CsvService
from services.selenium.selenium_mega_service import SeleniumMegaService
from services.schedule.schedule_services import ScheduleService

filename: str = 'original_data.csv'


with open(os.path.join(os.getcwd(), '..', '.env'), 'r') as file_env:
    for line in file_env:
        if line.startswith('#') or not line.strip():
            continue

        key, value = line.strip().split('=', 1)
        os.environ[key] = value


def test() -> None:
    print(f"Schedule + {time.time()}")


def job_scraping() -> None:
    """ Run Scraping Mega Sena"""
    csv_service = CsvService()
    selenium_service = SeleniumMegaService()

    selenium_service.set_next_page()
    rows: list[WebElement] = selenium_service.get_rows()
    columns: list[str] = selenium_service.get_thead_columns()

    csv_service.update(filename, columns, rows, selenium_service.runner) if csv_service.is_file(
        filename) else csv_service.create(filename, columns, rows, selenium_service.runner)
    selenium_service.exit()


def job_batch() -> None:
    mysql_service = MysqlService()
    csv_service = CsvService()
    cursor = mysql_service.get_cursor()

    files_db = mysql_service.find_all(cursor)
    files_local = csv_service.get_files(filename)

    if len(files_db) == 0:
        print("### Create new registers on database ###")
        mysql_service.save_data_db(files_local, cursor)
        print("### Create with successfuly ###")

    else:
        print("### Update register database ###")
        last_index = files_db.index(files_db[-1])
        mysql_service.save_data_db(files_local, cursor, last_index)
        print("### Updated with successfuly ###")

    cursor.close()
    mysql_service.db.close()


if __name__ == '__main__':
    # job_scraping()
    # job_batch()
    ScheduleService.call_by_minutes(10, test)

    while True:
        ScheduleService.run_pending()
        time.sleep(1)
