from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chr_opts

class scrapper:
    def __init__(self):
        self.driver= webdriver.chrome
        self.opts = chr_opts
    
    def close(self):
        self.driver.quit()
    
    def get_driver(self):
        return self.driver
    
    def set_opts_headless(self,Boolean):
        self.opts.headless = Boolean