from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from Constants import *

class WebScraper:
  def __init__( self, use_browser, url):
    self.url = url

    if use_browser == CHROME:
      self.driver = webdriver.Chrome(
        service = ChromeService(
          ChromeDriverManager().install()
        ),
        options = webdriver.ChromeOptions()
      )
    elif use_browser == EDGE:
      # Edge設定
      self.driver = webdriver.Chrome(
        service = EdgeService(
          EdgeChromiumDriverManager().install()
        ),
        options = webdriver.EdgeOptions()
      )

  def access_page(self):
    self.driver.get(self.url)
    self.driver.maximize_window()

  def input_value_by_id(self, element_id, value):
    element = self.driver.find_element(By.ID, element_id)
    element.send_keys(value)

  def input_value_by_class(self, element_class, value):
    element = self.driver.find_element(By.CLASS_NAME, element_class)
    element.send_keys(value)

  def input_value_by_name(self, element_name, value):
    element = self.driver.find_element(By.NAME, element_name)
    element.send_keys(value)

  def input_value_by_css_selector(self, css_selector, value):
    element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
    element.send_keys(value)

  def click_button_by_id(self, button_id):
    element = self.driver.find_element(By.ID, button_id)
    element.click()

  def click_button_by_class(self, button_class):
    element = self.driver.find_element(By.CLASS_NAME, button_class)
    element.click()

  def click_button_by_css_selector(self, button_class):
    element = self.driver.find_element(By.CSS_SELECTOR, button_class)
    element.click()

  def quit_browser(self):
    self.driver.quit()