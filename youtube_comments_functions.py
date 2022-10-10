# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:51:50 2022

@author: tosea
"""


def google_translate_via_selenium(original_text):
    import time
    from selenium import webdriver
    import selenium 
    from webdriver_manager.chrome import ChromeDriverManager
    
    # Give Language code in which you want to translate the text:=>
    lang_code = 'en '
    # Provide text that you want to translate:=>
    input1 = original_text
    # launch browser with selenium:=>
    c = webdriver.ChromeOptions()
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=c)
        # copy google Translator link here:=>
    browser.get("https://translate.google.co.in/?sl=auto&tl="+lang_code+"&text="+input1+"&op=translate")
    # just wait for some time for translating
    time.sleep(5)
    
    # Given below x path contains the translated output that we are storing in output variable:
    # 1. Translated text, 2. Detected language
    translated_text = browser.find_element('xpath','/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]/span[1]/span/span').text
    detected_language = browser.find_element('xpath', "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[2]/div/div[2]/div/div/span/button[1]/span[1]/span").text
    
    import re
    #extract the detected langauge's name, capitalize only the first alphabet
    detected_language = re.sub(" - DETECTED", "", detected_language).title()
    browser.close()
    
    return translated_text, detected_language

