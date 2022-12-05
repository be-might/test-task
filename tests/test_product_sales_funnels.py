
from src.landing_page import LandingPageObject


def test_success_solve_button_flow(get_driver, id_generator):
    """
    In this test we check that main flow with valid data pass successfully
    """
    landing_page_obj = LandingPageObject(get_driver)
    landing_page_obj.navigate_to_page()
    landing_page_obj.send_keys(landing_page_obj.YOUR_QUESTION_FIELD, '2+2')
    landing_page_obj.click_element(landing_page_obj.SOLVE_BUTTON)
    landing_page_obj.send_keys(landing_page_obj.EMAIL_FIELD, f'{id_generator}@tests.com')
    landing_page_obj.click_element(landing_page_obj.MODAL_CONTINUE_BUTTON)
    landing_page_obj.click_element(landing_page_obj.GET_TRIAL_BUTTON)

    landing_page_obj.switch_to_frame(landing_page_obj.PAYMENT_IFRAME)
    landing_page_obj.click_element(landing_page_obj.CARD_NUMBER)
    landing_page_obj.send_keys(landing_page_obj.CARD_NUMBER, '4532456618142692')
    landing_page_obj.click_element(landing_page_obj.CARD_EXPIRATION_DATE)
    landing_page_obj.send_keys(landing_page_obj.CARD_EXPIRATION_DATE, '03')
    landing_page_obj.send_keys(landing_page_obj.CARD_EXPIRATION_DATE, '2029')
    landing_page_obj.click_element(landing_page_obj.CARD_CVV)
    landing_page_obj.send_keys(landing_page_obj.CARD_CVV, '967')
    landing_page_obj.click_element(landing_page_obj.ZIP_CODE)
    landing_page_obj.send_keys(landing_page_obj.ZIP_CODE, '02000')
    landing_page_obj.click_element(landing_page_obj.SUBMIT_BUTTON)


def test_invalid_card_data(get_driver, id_generator):
    """
    In this test we check that after passing wrong card data user will navigate to error page
    with button to turn back to card input modal
    """
    landing_page_obj = LandingPageObject(get_driver)
    landing_page_obj.navigate_to_page()
    landing_page_obj.send_keys(landing_page_obj.YOUR_QUESTION_FIELD, '2+2')
    landing_page_obj.click_element(landing_page_obj.SOLVE_BUTTON)
    landing_page_obj.send_keys(landing_page_obj.EMAIL_FIELD, f'{id_generator}@tests.com')
    landing_page_obj.click_element(landing_page_obj.MODAL_CONTINUE_BUTTON)
    landing_page_obj.click_element(landing_page_obj.GET_TRIAL_BUTTON)

    landing_page_obj.switch_to_frame(landing_page_obj.PAYMENT_IFRAME)
    landing_page_obj.click_element(landing_page_obj.CARD_NUMBER)
    landing_page_obj.send_keys(landing_page_obj.CARD_NUMBER, '4532456618142692')
    landing_page_obj.click_element(landing_page_obj.CARD_EXPIRATION_DATE)
    landing_page_obj.send_keys(landing_page_obj.CARD_EXPIRATION_DATE, '04')
    landing_page_obj.send_keys(landing_page_obj.CARD_EXPIRATION_DATE, '2029')
    landing_page_obj.click_element(landing_page_obj.CARD_CVV)
    landing_page_obj.send_keys(landing_page_obj.CARD_CVV, '967')
    landing_page_obj.click_element(landing_page_obj.ZIP_CODE)
    landing_page_obj.send_keys(landing_page_obj.ZIP_CODE, '02000')
    landing_page_obj.click_element(landing_page_obj.SUBMIT_BUTTON)

    try_again_button = landing_page_obj.find_element(landing_page_obj.TRY_AGAIN_BUTTON)
    assert try_again_button.text == 'Try again'


def test_send_later_button_flow(get_driver, id_generator):
    """
    In this test we check that we get to the success flow through "I'll send it later button"
    """
    landing_page_obj = LandingPageObject(get_driver)
    landing_page_obj.navigate_to_page()
    landing_page_obj.send_keys(landing_page_obj.YOUR_QUESTION_FIELD, '2+2')
    landing_page_obj.click_element(landing_page_obj.SOLVE_BUTTON)
    landing_page_obj.send_keys(landing_page_obj.EMAIL_FIELD, f'{id_generator}@tests.com')
    landing_page_obj.click_element(landing_page_obj.MODAL_CONTINUE_BUTTON)
    get_trial_button = landing_page_obj.find_element(landing_page_obj.GET_TRIAL_BUTTON)
    assert get_trial_button.text == 'Get Trial'
