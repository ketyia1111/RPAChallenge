from WebScraper import WebScraper
from ExcelHandler import ExcelHandler
from Config import Config
from Constants import *
import asyncio

async def input_data(scraper, row):
  first_name = row[COLUMN_FIRST_NAME]
  last_name = row[COLUMN_LAST_NAME]
  company_name = row[COLUMN_COMPANY_NAME]
  department = row[COLUMN_DEPARTMENT]
  address = row[COLUMN_ADDRESS]
  email = row[COLUMN_EMAIL]
  phone_number = row[COLUMN_PHONE_NUMBER]

  # 入力
  scraper.input_value_by_css_selector(INPUT_SELECTOR_TEMPLATE.format(FIELD_LAST_NAME), last_name)
  scraper.input_value_by_css_selector(INPUT_SELECTOR_TEMPLATE.format(FIELD_DEPARTMENT), department)
  scraper.input_value_by_css_selector(INPUT_SELECTOR_TEMPLATE.format(FIELD_PHONE_NUMBER), phone_number)
  scraper.input_value_by_css_selector(INPUT_SELECTOR_TEMPLATE.format(FIELD_EMAIL), email)
  scraper.input_value_by_css_selector(INPUT_SELECTOR_TEMPLATE.format(FIELD_COMPANY_NAME), company_name)
  scraper.input_value_by_css_selector(INPUT_SELECTOR_TEMPLATE.format(FIELD_ADDRESS), address)
  scraper.input_value_by_css_selector(INPUT_SELECTOR_TEMPLATE.format(FIELD_FIRST_NAME), first_name)

  scraper.click_button_by_css_selector(SUBMIT_BUTTON_SELECTOR)

async def main():
  # Configファイル設定
  config = Config(CONFIG_INI)

  #エクセルファイル取得
  excel = ExcelHandler(
    config.get(
      SETTING,
      TARGET_FILE
    )
  )
  #データを取得
  data_dict = excel.read_excel()

  # WebScraperのインスタンスを作成
  scraper = WebScraper(
    config.get(
      SETTING,
      USE_BROWSER
    ),
    config.get(
      SETTING,
      TARGET_URL
    )
  )

  scraper.access_page()
  scraper.click_button_by_class(START_BUTTON_CLASS)

  for row in data_dict:
    await input_data(scraper, row)
  
  input(PROMPT_CLOSE_BROWSER)

if __name__ == MAIN_FUNCTION_NAME:
  asyncio.run(main())