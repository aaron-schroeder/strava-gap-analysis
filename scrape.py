import json
import time

import util


driver = util.get_webdriver(authenticated=True)


# TODO: find the most direct way to get all athlete activities.
# on god I am typing these in by hand 🤦 smdh
activity_ids = [9135174515, 9127177891, 9122740538, 9122739001, 9122738302]

for id in activity_ids:
  driver.get(f'https://www.strava.com/activities/{id}')
  time.sleep(2)
  stream_data = driver.execute_script("""
    return pageView.streamsRequest.streams.streamData.data;
  """)

  with open(f'out/streams_{id}.json', 'w') as f:
    json.dump(stream_data, f)