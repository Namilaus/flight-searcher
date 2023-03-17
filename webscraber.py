from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


def scraping(urls: str) -> str:
    """

    :param urls: -> needed urls to fetch the page
    :return all datas we need about the best flight -> price and link
    """
    # cheking if there is 2 link
    isLang = False
    if len(urls) == 2:
        isLang = True
    # open brower to get source code
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    # save first url
    firstUrl = urls[0]
    # scrape data
    driver.get(firstUrl)
    #sleep(2)
    driver.find_element(By.XPATH,
                        "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc "
                        "AjY5Oe DuMIQc LQeN7 Nc7WLe']").click()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    # price list
    price = soup.find_all("div", class_="YMlIz FpEdX jLMuyc")
    # if there is price in this class type try this one
    if len(price) == 0:
        price = soup.find_all("div", class_="BVAVmf I11szd POX3ye")

    # find cheapest flight
    def intoOrder(data):
        """

        :param data: -> prices from source page of google
        :return cheaperstFlight:
        """
        # scrapting data comes into this array
        arrayOfPriceInInteger = []
        # take data into array
        for i in data:
            arrayOfPriceInInteger.append(int(i.text[1:]))
        # find the cheapestFligth
        cheapestFligth = arrayOfPriceInInteger[0]
        for i in arrayOfPriceInInteger:
            if cheapestFligth > i:
                cheapestFligth = i
        return cheapestFligth

    price = intoOrder(price)
    urls = urls[1:]
    driver.quit()
    if isLang:
        return {
            "firstflight": {
                "link": firstUrl,
                "price": price
            },
            "secondflight": {
                "infos": scraping(urls)
            }}

    return {
        "flight_price": price,
        "link": firstUrl
    }


# exampless and tests

# timer = time.time()
# myFlight = flight("ankara", "istanbul", "one way", "30.03.2023", False)
# url = myFlight.searchFlight()
# datas = scraping(url)
# timer2 = time.time()
# print(datas, timer2 - timer)
