from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from functions import dateUmwandeln



# go to the site
class flight:
    def __init__(self,wherefrom:str,to:str,oneOrRound:str,date:str,returnDate:str)-> None:
        self.wherefrom = wherefrom
        self.to = to
        self.oneOrRound = oneOrRound
        self.date = dateUmwandeln(date)
        if returnDate == False:
            pass
        else:
            self.returnDate = dateUmwandeln(returnDate)



    def searchFlight(self) -> str:
        # go to google
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)

        driver.get('https://www.google.com')
        driver.find_element(By.CLASS_NAME, "sy4vM").click()

        # define the search bar from google
        searchBar = driver.find_element(By.CLASS_NAME, "gLFyf")



        def oneWay():
            try:
                searchBar.send_keys(f"{self.wherefrom} to {self.to} at {self.date.replace('.',' ')} flight one way")
                searchBar.submit()
                flightSection = driver.find_element(By.XPATH, "//span[@class='Z4Cazf OSrXXb']")
                flightSection.click()
            except ValueError:
                print(ValueError)
                oneWay()

            url = [driver.current_url]
            driver.quit()
            return url

        def roundTrip() -> str:
            if self.returnDate == False:
                print("please enter a date")
                return 0

            try:
                url = []
                searchBar.send_keys(f"{self.wherefrom} to {self.to} round trip")
                searchBar.submit()
                flightSection = driver.find_element(By.XPATH, "//span[@class='Z4Cazf OSrXXb']")
                flightSection.click()
                sleep(2)
                dateInput = driver.find_element(By.XPATH, "//input[@placeholder='Departure']")
                returnInput = driver.find_element(By.XPATH, "//input[@placeholder='Return']")
                for i in range(0,11):
                    dateInput.send_keys(Keys.BACK_SPACE)

                dateInput.send_keys(self.date)
                sleep(1)
                for i in range(0,11):
                    returnInput.send_keys(Keys.BACK_SPACE)
                returnInput.send_keys(self.returnDate)
                sleep(2)
                for i in range(0,11):
                    returnInput.send_keys(Keys.BACK_SPACE)
                returnInput.send_keys(self.returnDate)

                sleep(1)
                url.append(driver.current_url)
                sleep(1)
                driver.find_element(By.XPATH,"//div[@class='mxvQLc ceis6c uj4xv uVdL1c A8qKrc']").click()
                sleep(1)
                url.append(driver.current_url)
                driver.quit()
                return url

            except ValueError:
                print(ValueError)
                roundTrip()




        if self.oneOrRound == "one way":
            return oneWay()
        else:
            return roundTrip()




#myfligth  = flight("ankara","istanbul","round way","30.3.2023","12.4.2023")

#print(myfligth.searchFlight())
