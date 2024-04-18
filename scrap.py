"""
Selenium is a more suitable choice for scraping Twitter due to its ability to 
handle dynamic content and provide a more interactive and robust scraping experience.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

def scrape_twitter_account(url, ticker):
    #creating a new instance of the Chrome WebDriver
    driver = webdriver.Chrome()  #adjusting the path to the Chrome driver
    #navigating to the provided URL
    driver.get(url)
    #waiting for the page to load
    time.sleep(5)
    
    #Finding all the tweet elements using the CSS selector
    tweets = driver.find_elements(By.CSS_SELECTOR, 'p.tweet-text')
    # counting the number of tweets containing the specified stock symbol
    count = sum(1 for tweet in tweets if re.search(r'\b' + re.escape(ticker) + r'\b', tweet.text))

    #closing the browser window to release resources
    driver.quit()
    return count

#list of Twitter account URLs
url = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart",
    "https://twitter.com/RoyLMattox"
]

#stock symbol to search for
ticker = "$TSLA"
# time interval between scraping sessions (in minutes)
interval_minutes = 15
interval_seconds = interval_minutes * 60

#a while loop to scrap the twitter accounts at the specified time
while True:
    #a for loop to iterate over each Twitter account URL
    for account_url in url:
        #scraping the account for mentions of the stock symbol and printing the result
        mentions_count = scrape_twitter_account(account_url, ticker)
        print(f"{ticker} was mentioned {mentions_count} times on {account_url}")

    #wait for the specified interval before scraping again
    print(f"Waiting for {interval_minutes} minutes before the next scraping session...")
    time.sleep(interval_seconds)