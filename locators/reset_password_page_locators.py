from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    CODE_INPUT= (By.XPATH,"//label[text()='Введите код из письма']/parent::div/input")
    PASSWORD_INPUT= (By.XPATH,"//input[@name='Введите новый пароль']")
    PASSWORD_INPUT_SWITCHER  = (By.CSS_SELECTOR, ".input__icon.input__icon-action")
    PASSWORD_INPUT_STYLE  = (By.XPATH, PASSWORD_INPUT[1]+"/parent::div")