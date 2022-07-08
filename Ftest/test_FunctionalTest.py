from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    # def tearDown(self):
    #     self.browser.quit()
        
    def test_start_list_and_retrieve_it(self):
        self.browser.get(self.live_server_url)
        self.assertIn('WASD Gamers', self.browser.title)

        headerText = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('WASD Gamers', headerText)
        
        inputName = self.browser.find_element_by_id('for1Form')
        inputName.send_keys('Justin')
        #time.sleep(1)
        
        inputNumber = self.browser.find_element_by_id('for2Form')
        inputNumber.send_keys('1')
        #time.sleep(1)
        
        inputReview = self.browser.find_element_by_id('for3Form')
        inputReview.send_keys('Super Idol')
        #time.sleep(1)
        
        btnConfirm = self.browser.find_element_by_id('btnConfirm')
        btn1 = self.browser.find_element_by_id('agree1')
        btn2 = self.browser.find_element_by_id('disagree2')
        btn3 = self.browser.find_element_by_id('neutral3')

        self.assertEqual(inputName.get_attribute('placeholder'),'Enter name.')
        self.assertEqual(inputReview.get_attribute('placeholder'),'Comment.')
        
        btn1.click()
        time.sleep(1)

        btn2.click()
        time.sleep(1)

        btn3.click()
        time.sleep(1)

        btnConfirm.click()
        time.sleep(1)
        
        table = self.browser.find_element_by_id('testTable')
        row_data = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Justin, 1, Super Idol, Agree, Disagree, Neutral', [row.text for row in row_data])
        #self.assertTrue(any(row.text == '1: Test Name'), "No tables yet")

if __name__=='__main__':
    unittest.main(warnings='ignore')

