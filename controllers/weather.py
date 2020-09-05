from models.webscrapper import scrapper

class weather:
    def __init__(self,location):
        self.scrapper = scrapper()
        self.driver = self.scrapper.get_driver()
        self.location = location
    
    def searcher(self,driver):
        driver=self.driver
        driver.find_element_by_class_name("search-form").send_keys(self.location)
        
    def run(self):
        driver= self.driver
        driver.get("https://www.accuweather.com/")

    def close(self):
        self.scrapper.close()