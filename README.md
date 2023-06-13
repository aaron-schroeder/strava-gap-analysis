## Research question: How does the GAP algorithm work?

## Approach
Good (current): upload synthetic data with constant speed and grade.

Better: Scrape the actual GAP data and investigate real-data relationship between SmoothGradeStream and (GradeAdjustedDistance, GradeAdjustedPace).
  - from the frontend
    - Heavyish lift possibly. So far I've only done this manually, but I'd only consider doing it for all activities if I got selenium/scrapy to do it. 
  - From the api
    - Streams not possible: no GAP stream provided
    - Summary data? I assume GAP is included if you pay, but I'm not sure.

## Anticipated difficulties
- Authentication will be an issue. Once I'm logged in, I can scrape ANYONE'S public data though.
- I am just sure that something will pop up between successfully authenticating and successfully using selenium.
- Handling javascript within the request implies Selenium will be used (I have not done with scrapy before)

## References
[reddit account of a person claiming to be the author of the GAP algorithm](https://www.reddit.com/user/therealslloyd/)
