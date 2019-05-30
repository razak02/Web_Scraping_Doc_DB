

# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def scrape():
  #browser = init_browser()
 
  Mars_data ={}
 
  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)


  url = 'https://mars.nasa.gov/news/'
  browser.visit(url)




  html = browser.html
  soup = BeautifulSoup(html, 'html.parser')


  # # Collecting NASA Mars News



  # Collecting the Latest News Title and Paragraph Text
  news_title  = soup.find('div', class_='content_title').a.text
  news_p = soup.find('div', class_='article_teaser_body').text

 ## print(news_title)
 # print('--' * 50)
 # print(news_p)


  # # JPL Mars Space Featured Image 



  # Dependencies

  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)
  html = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
  browser.visit(html)
  html = browser.html    



  # Create a Beautiful Soup object

  soup = BeautifulSoup(html,'html.parser')




  # Collect image featured_image_url

  nasa_image_url = soup.find('a', class_='button fancybox')["data-fancybox-href"]
  nasa_image_url



  nasa_url = 'https://www.jpl.nasa.gov'



  # conctatinating to get the featured image

  featured_image_url =  nasa_url + nasa_image_url
 # print(featured_image_url)




  # Quit Browser

  browser.quit()


  # # Mars Weather



  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)

  url= 'https://twitter.com/marswxreport?lang=en'
  browser.visit(url)
  html = browser.html


  # Create a Beautiful Soup object
  soup = BeautifulSoup(html, 'html.parser')



  # Collect the latest Mars weather tweet from the page
  news_weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
  news_weather


  news_weather = news_weather.replace("\n", " ")
  news_weather



  news_weather_link = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').a.text
  news_weather_link



  mars_weather = news_weather.replace(news_weather_link, " ")
  mars_weather



  # Quit Browser
  browser.quit()


  # # Mars Facts


  url = 'https://space-facts.com/mars/'



  executable_path = {'executable_path': 'chromedriver.exe'}
  browser = Browser('chrome', **executable_path, headless=False)
  html = 'https://space-facts.com/mars/'
  browser.visit(html)
  html = browser.html



  # Using Pandas to Read HTML Table
  mars_facts_table = pd.read_html(url)
  mars_facts_table



  # Convert HTML to Dataframe
  mars_facts_df = mars_facts_table[0]
  mars_facts_df


  # Cleaning Dataframe
  mars_facts_df.columns = ['Description', 'Mars Facts']
  mars_facts_df.set_index('Description', inplace=True)
  mars_facts_df



  # Convert Dataframe to html table 
  mars_facts_html = mars_facts_df.to_html()
  mars_facts_html
  #print('mars_facts_html'.prettify())
  #print(soup.prettify())


  # Quit Browser
  browser.quit()

  # function to capature variables 

  

    # Store data in a dictionary
  Mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "news_weather": news_weather,
        "mars_weather":mars_weather,
        "mars_facts_html": mars_facts_html,
        "featured_image_url": featured_image_url
  }

  # Close the browser after scraping
  #browser.quit()

    # Return results
  
  print("Mission to Mars Web Sites Scrapped and Data Available")
  
  return Mars_data
  