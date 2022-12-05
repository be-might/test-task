from src.base_page_object import BasePageObjectClass


class LandingPageObject(BasePageObjectClass):
    YOUR_QUESTION_FIELD = "//textarea[@placeholder='Describe your question or add a photo']"
    SOLVE_BUTTON = "//button[normalize-space()='Solve']"
    EMAIL_FIELD = "//input[@id='email']"
    MODAL_CONTINUE_BUTTON = "//button[normalize-space()='Continue']"
    GET_TRIAL_BUTTON = "//button[normalize-space()='Get Trial']"

    PAYMENT_IFRAME = "//iframe[@id='solid-payment-form-iframe']"
    CARD_NUMBER = "//input[@id='ccnumber']"
    CARD_EXPIRATION_DATE = "//input[@id='cardExpiry']"
    CARD_CVV = "//input[@id='cvv2']"
    ZIP_CODE = "//input[@placeholder='XXXXX']"
    SUBMIT_BUTTON = "//span[@class='title']"

    TRY_AGAIN_BUTTON = "//button[@type='button'][normalize-space()='Try again']"

    SEND_LATER_BUTTON = "//div[@class='container pt-9 pb-13 pt-lg-15 pb-lg-17']//a[@class='btn btn-outline-black w-100 font-weight-bold'][contains(text(),'I’ll send it later')]"

    def __init__(self, driver):
        super().__init__()

        self._driver = driver
        self._url = 'https://mathguru.live/?source=test'

