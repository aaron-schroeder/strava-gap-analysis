import json
import time

from scrapy import Spider
from scrapy.http import Request, FormRequest

from scraper import util


class SessionSpider(Spider):
  name = 'session'

  # Start with a login request
  def start_requests(self):
    return [
      Request('https://www.strava.com/', callback=self.parse_landing_page)
    ]
  
  def parse_landing_page(self, response):
    assert 'strava.com/dashboard' in response.url
    # print(response)

    # HACK-y: use selenium to make a request to the page containing actual data,
    # then extract the data from the JS.
    driver = util.get_webdriver(authenticated=True)
    driver.add_cookie({'_strava4_session': 'f18ie7fqh69b7ksesjo1f6r1ud2kph8l'})
    driver.get('https://www.strava.com/activities/9135174515')
    time.sleep(2)
    pageView = driver.execute_script('return pageView;')
    print(pageView)
    
    return {}
    # return Request('https://www.strava.com/activities/9135174515',
    #                callback=self.parse_activity_page)
