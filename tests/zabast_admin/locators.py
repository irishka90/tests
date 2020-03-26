from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


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
    DATE_SORTING = (By.CLASS_NAME, "baseTable__cell__sortingIndicator")
    DATE_SORTING_ASC = (By.CLASS_NAME, "baseTable__cell__sortingIndicator.--ascending")
    DATE_SORTING_DESC = (By.CLASS_NAME, "baseTable__cell__sortingIndicator.--descending")
    DATA_TABLE_SORTING = (By.CLASS_NAME, "baseTable__body")
    DROP_DOWN = (By.CLASS_NAME, "dropdown__title")
    DELETE_NEWS = (By.CLASS_NAME, "dropdown__list__actionWrapper")
    DELETE_NEWS_OK = (By.CLASS_NAME, "button.modal__footerButton.--primary")
    TAKE_AWAY = (By.CLASS_NAME, "dropdown__list__actionWrapper")
    TAKE_AWAY_OK = (By.CLASS_NAME, "button.modal__footerButton.--primary")
    CHANGE_NEWS = (By.XPATH, "/html/body/div/section/section/main/div[1]/div/div[2]/div[1]/div[6]/div/ul/li[2]")


class TextFields():
    date = datetime.today().strftime('%d-%m-%Y')
    yesterday = "12-12-2012"
    title_en = "What is Lorem Ipsum?"
    content_en = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."
    title_en_2 = "News in english"
    content_en_2 = "Text in english"
    title_ru = "Что такое Lorem Ipsum?"
    content_ru = "Lorem Ipsum - это текст-рыба, часто используемый в печати и вэб-дизайне. Lorem Ipsum является стандартной рыбой для текстов на латинице с начала XVI века."
    title_ru_2 ="Новость на русском"
    content_ru_2 = "Текст новости на русском"
    title_es = "¿Qué es Lorem Ipsum?"
    content_es = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500."
    title_es_2 = "Noticias en español"
    content_es_2 ="Noticias de texto en español"
    title_de = "Was ist Lorem Ipsum?"
    content_de = "Lorem Ipsum ist ein einfacher Demo-Text für die Print- und Schriftindustrie. Lorem Ipsum ist in der Industrie bereits der Standard Demo-Text seit 1500."
    title_de_2 = "Deutsche Nachrichten"
    content_de_2 = "Deutscher Nachrichtentext"
    tag_1 = "Lorem"
    tag_2 = "Ipsum"
    tag_new = "new tag"
    url_source = "https://strikeapi2.herokuapp.com/"
    image = "https://picsum.photos/600/300"
    image2 = "https://picsum.photos/700/300"
    video_url = "https://youtu.be/IrZAc3Dsfkk"


class NewsPageLocators():
    CREATE_BUTTON = (By.CLASS_NAME, "button.sectionHeader__action.--primary")
    CHOOSE_DATE = (By.CLASS_NAME, "el-input__inner")
    BG_FORM = (By.CLASS_NAME, "modal")
    CALENDAR = (By.CLASS_NAME, "el-picker-panel__body")
    DATE = (By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[4]")
    LANGUAGE_CHOOSE_1 = (By.NAME, "_languages")
    LANGUAGE_CHOOSE_2 = (By.CLASS_NAME, "multiselect")
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
    TAG_NEW = (By.CLASS_NAME, "vue-input-tag-wrapper.baseFormField__control")
    PHOTO_URL = (By.XPATH, '/html/body/div/div/div/div/div[2]/div/div[2]/form/div[5]/div/div/input')
    CHECKBOX = (By.CLASS_NAME, "baseSwitch-w.baseFormField__control.--unchecked")
    CREATE_NEWS_BUTTON = (By.CLASS_NAME, "button.modal__footerButton.--primary")
    CANCEL_BUTTON = (By.CLASS_NAME, "button.modal__footerButton")
    VIDEO_ADD = (By.CLASS_NAME, "button.videoInput__button")
    VIDEO_ADD_WINDOW = (By.CLASS_NAME, "v--modal-box.v--modal")
    ADD_URL = (By.CLASS_NAME, "baseInput.baseFormField__control.--invalid")
    VIDEO_TYPE = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div/div/div[1]")
    YOUTUBE = (By.CLASS_NAME, "multiselect__option.multiselect__option--highlight")
    VIDEO_ADD_BUTTON = (By.CLASS_NAME, "button.modal__footerButton.--primary")


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
