"""work in progress"""

import time

import util


driver = util.get_webdriver(authenticated=True)


driver.get('https://www.strava.com/athlete/training_activities'
           '?page=1&per_page=20&new_activity_only=false')

time.sleep(2)

# print(driver.current_url)
print(driver.page_source)