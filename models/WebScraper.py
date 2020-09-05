from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_opts

class scrapper:
    def __init__(self):
        self.driver= webdriver.chrome
        self.opts = chr_opts
    
    def quit(self):
        self.driver.quit() 