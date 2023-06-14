import os
import time

from scrapy import Spider
from scrapy.http import Request, FormRequest

from scraper import util


class LoginSpider(Spider):
  name = 'login'

  # Start with a login request
  def start_requests(self):
    return [
      Request('https://www.strava.com/login', callback=self.parse_login_page)
    ]
  
  def parse_login_page(self, response):
    return FormRequest.from_response(
      response,
      formdata={'email': os.getenv('STRAVA_EMAIL'),
                'password': os.getenv('STRAVA_PASSWORD')},
      callback=self.parse_landing_page
    )
  
  def parse_landing_page(self, response):
    assert 'strava.com/dashboard' in response.url
    # print(response)

    # HACK-y: use selenium to make a request to the page containing data
    # of interest, then extract the data from the JS.
    driver = util.get_webdriver()
    for cookie_name, cookie_value in response.request.cookies.items():
      # for cookie_name, cookie_value in response.cookies.items():
      print(cookie_name + ': ' + cookie_value)
      driver.add_cookie({'name': cookie_name, 'value': cookie_value})
    driver.get('https://www.strava.com/activities/9135174515')
    time.sleep(5)
    # print(driver.current_url)
    print('')
    print('')
    # print(driver.page_source)
    # pageView = driver.execute_script('return pageView;')
    # print(pageView)
    
    return 