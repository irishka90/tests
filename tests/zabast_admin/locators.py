from selenium.webdriver.common.by import By
from datetime import datetime

class BasePageLocators():
  LOGIN_FORM = (By.CLASS_NAME, "loginForm")
  LOGIN_INPUT = (By.NAME, "email")
  PASSWORD_INPUT = (By.CLASS_NAME, "baseInput.baseInputPassword__input")
  REG_SUBMIT = (By.CLASS_NAME, "button.loginForm__button")
  EVENT = (By.CLASS_NAME, "theNavBar__menu.el-menu:nth-child(2)")
  LOG_OUT = (By.CLASS_NAME, "userPanel__main.el-dropdown-selfdefine")
  OUT_BUTTON = (By.XPATH, "/html/body/ul/li/span")
  FORWARD_BUTTON = (By.XPATH, "/html/body/div/section/section/main/div[2]/div[7]/a")
  BACK_BUTTON = (By.CLASS_NAME, "basePagination__itemLink")
  CHOOSE_PAGE_3 = (By.XPATH, "//*[@id='app']/section/section/main/div[2]/div[4]/a")
  DATE_SORTING =  (By.CLASS_NAME,"baseTable__cell__sortingIndicator")
  DROP_DOWN = (By.CLASS_NAME, "dropdown__title")
  DELETE_NEWS = (By.CLASS_NAME, "dropdown__list__actionWrapper")
  DELETE_NEWS_OK = (By.CLASS_NAME,"button.modal__footerButton.--primary")
  TAKE_AWAY = (By.CLASS_NAME, "dropdown__list__actionWrapper")
  TAKE_AWAY_OK = (By.CLASS_NAME, "button.modal__footerButton.--primary")

class TextFields():
  date = datetime.today().strftime('%d-%m-%Y')
  title_en = "What is Lorem Ipsum?"
  content_en = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."
  title_ru = "Что такое Lorem Ipsum?"
  content_ru = "Lorem Ipsum - это текст-рыба, часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной рыбой для текстов на латинице с начала XVI века."
  title_es = "¿Qué es Lorem Ipsum?"
  content_es = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500."
  title_de = "Was ist Lorem Ipsum?"
  content_de = "Lorem Ipsum ist ein einfacher Demo-Text für die Print- und Schriftindustrie. Lorem Ipsum ist in der Industrie bereits der Standard Demo-Text seit 1500."


class NewsPageLocators():
  CREATE_BUTTON = (By.CLASS_NAME, "button.sectionHeader__action.--primary")
  CHOOSE_DATE = (By.CLASS_NAME, "el-input__inner")
  BG_FORM = (By.CLASS_NAME, "modal")
  CALENDAR = (By.CLASS_NAME, "el-picker-panel__body")
  DATE = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[4]")
  LANGUAGE_CHOOSE_1=(By.NAME, "_languages")
  LANGUAGE_CHOOSE_2=(By.CLASS_NAME, "multiselect")
  LANG1 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/div/div[3]/ul/li[1]/span")
  TITLE_1 = (By.NAME, "titleRu")
  DESCRIPTION_1 = (By.NAME, "contentRu")
  LANG2 = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/div/div[3]/ul/li[2]/span")
  TITLE_2 = (By.NAME, "titleEn")
  DESCRIPTION_2 = (By.NAME, "contentEn")
  LANG3 = (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/div/div[3]/ul/li[3]/span")
  TITLE_3 = (By.NAME, "titleEs")
  DESCRIPTION_3 = (By.NAME, "contentEs")
  LANG4 = (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[2]/form/div[2]/div/div/div/div[3]/ul/li[4]/span")
  TITLE_4 = (By.NAME, "titleDe")
  DESCRIPTION_4 = (By.NAME, "contentDe")
  SOURSE_LINK = (By.NAME, "sourceLink")
  TAG = (By.CLASS_NAME, "new-tag")
  PHOTO_URL =(By.CLASS_NAME, "baseInputImageTag__input")
  CHECKBOX = (By.CLASS_NAME, "baseSwitch-w.baseFormField__control.--unchecked")
  CREATE_NEWS_BUTTON = (By.CLASS_NAME, "button.modal__footerButton.--primary")
  CANCEL_BUTTON = (By.CLASS_NAME, "button.modal__footerButton")

class EventPageLocators():
  CREATE_BUTTON = (By.CLASS_NAME, "button.sectionHeader__action.--primary")
  TYPE_EVENT = (By.CLASS_NAME, "multiselect")
  TYPE_EVENT_1 = (By.CLASS_NAME, "multiselect__content:nth-child(1)")
  COUNTRY_CHOOSE = (By.CLASS_NAME, "multiselect__tags")
  COUNTRY_CHOOSE_1 = (By.CLASS_NAME, "multiselect__tags:nth-child(1)")
  REGION = (By.CLASS_NAME, "multiselect__input")
  REGION_CHOOSE = (By.CLASS_NAME, "multiselect__input:nth-child(1)")
 # TOWN = (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div[2]/form/div[4]/div/div/div/div[2]/input")
 # TOWN_CHOOSE =

