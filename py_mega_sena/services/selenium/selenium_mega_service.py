import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime

URL = "https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx"
XPATH_ROWS = '//*[@id="ctl50_g_cf05b8d5_fd75_46b5_bdfa_a623e654362c"]/div/div/table/tbody'
X_PATH_THEAD = '//*[@id="ctl50_g_cf05b8d5_fd75_46b5_bdfa_a623e654362c"]/div/div/table/thead'
X_PATH_THEAD_TR = '//*[@id="ctl50_g_cf05b8d5_fd75_46b5_bdfa_a623e654362c"]/div/div/table/thead/tr'
FILE_NAME = 'assets/original-data.csv'
 # https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Mega-Sena

remove_dot = re.compile(r'\.')
remove_dollar = re.compile(r'^[R]\$')
remove_two_words = re.compile(r'^(\w{2})$')
remove_currency = re.compile(r'^[R]\$\d+\,\d{2}$')
remove_no = re.compile(r'^(N|n)\w{2}$')
replace_dot_by_comma = re.compile('\,')


class SeleniumMegaService:
    def __init__(self) -> None:
        print("::: Selenium Service started :::")
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('headless')
        self.t_head_columns: list[str] = []
        self.driver = webdriver.Chrome(options=self.option)
        self.set_driver()

    def set_driver(self) -> None:
        self.driver.get(URL)
        print(f"::: Current page is {self.driver.title} :::")

    def get_rows(self) -> list[WebElement]:
        return self.driver.find_elements(By.XPATH, XPATH_ROWS)

    def set_head_columns(self) -> None:
        t_head = self.driver.find_element(By.XPATH, X_PATH_THEAD)
        tr = t_head.find_element(By.XPATH, X_PATH_THEAD_TR)
        t_head_rows = tr.find_elements(By.TAG_NAME, 'th')
        for column in t_head_rows:
            self.t_head_columns.append(column.text)

    def get_thead_columns(self) -> list[str]:
        return self.t_head_columns

    def set_next_page(self) -> None:
        a = self.driver.find_element(By.CLASS_NAME, 'zeta')
        self.driver.implicitly_wait(30)
        self.driver.execute_script("arguments[0].click();", a)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.set_head_columns()
        print(f"::: Current page is {self.driver.title} :::")

    def currency_to_number(self, replace_dot_by_comma, remove_dot, remove_dollar, text) -> str:
        return re.sub(replace_dot_by_comma, '.', re.sub(remove_dot, '', re.sub(remove_dollar, '', text)))

    def runner(self, filename: str, columns: list[str], rows: list[WebElement], from_index=0,
               save_csv_data=None) -> None:

        print(f"::: Runner started :::")
        for element in rows[from_index:]:
            save_csv_data(filename, data=self.clean_texts(element, columns))

    def clean_texts(self, element: WebElement, columns: list[str]) -> list[str or None]:
        lists = [None] * len(columns)
        tds = element.find_elements(By.TAG_NAME, 'td')
        cities = [td.text.replace('\n', '::').replace(' ', ':') for td in tds[14].find_elements(By.TAG_NAME, 'tbody')]

        lists[0] = int(tds[0].text)
        lists[1] = datetime.strptime(tds[1].text, "%d/%m/%Y")
        lists[2] = int(tds[2].text)
        lists[3] = int(tds[3].text)
        lists[4] = int(tds[4].text)
        lists[5] = int(tds[5].text)
        lists[6] = int(tds[6].text)
        lists[7] = int(tds[7].text)
        lists[8] = tds[8].text
        lists[9] = tds[9].text
        lists[10] = tds[10].text
        lists[11] = self.currency_to_number(replace_dot_by_comma, remove_dot, remove_dollar, tds[11].text)
        lists[12] = self.currency_to_number(replace_dot_by_comma, remove_dot, remove_dollar, tds[12].text)
        lists[13] = self.currency_to_number(replace_dot_by_comma, remove_dot, remove_dollar, tds[13].text)
        lists[14] = '-' if not cities[0] else cities[0].upper()
        lists[15] = self.currency_to_number(replace_dot_by_comma, remove_dot, remove_dollar,
                                            'R$0,00' if not tds[-6].text else tds[-6].text)
        lists[16] = self.currency_to_number(replace_dot_by_comma, remove_dot, remove_dollar,
                                            'R$0,00' if not tds[-5].text else re.sub(remove_two_words, 'R$0,00',
                                                                                     tds[-5].text))
        lists[17] = self.currency_to_number(replace_dot_by_comma, remove_dot, remove_dollar,
                                            'R$0,00' if not tds[-4].text else tds[-4].text)
        lists[18] = 'Sim' if not tds[-3].text else re.sub(remove_two_words, 'Não',
                                                          re.sub(remove_currency, 'Não', tds[-3].text))
        lists[19] = 'Não' if not tds[-2].text else re.sub(remove_currency, 'Não', tds[-2].text)
        lists[20] = '-' if not tds[-1].text else re.sub(remove_currency, '-', re.sub(remove_no, '-', tds[-1].text))

        return lists

    def exit(self) -> None:
        print(f"::: Existing... :::")
        self.driver.quit()
