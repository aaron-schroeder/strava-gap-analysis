import os

import dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


dotenv.load_dotenv()


def get_webdriver(authenticated=False):
  # Use existing Chrome driver setup
  # WSL (Linux) setup
  s = Service(ChromeDriverManager().install())
  chrome_options = webdriver.ChromeOptions()
  # Note: the following 3 options are necessary to run in WSL.
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(service=s, options=chrome_options)
  if authenticated:
    driver.get('https://www.strava.com')

    # Add the fresh login cookie (delicious)
    driver.add_cookie({'name': '_strava4_session', 
                      'value': os.getenv('STRAVA_SESSION_COOKIE'),
                      'domain': 'strava.com'})
  return driver