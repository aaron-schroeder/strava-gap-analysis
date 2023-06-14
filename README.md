## Research question: How does the GAP algorithm work?

## Approach
Good (current): upload synthetic data with constant speed and grade.

Better: Scrape the actual GAP data and investigate real-data relationship between SmoothGradeStream and (GradeAdjustedDistance, GradeAdjustedPace).
  - from the frontend
    - Heavyish lift possibly. So far I've only done this manually, but I'd only consider doing it for all activities if I got selenium/scrapy to do it. 
  - From the api
    - Streams not possible: no GAP stream provided
    - Summary data? I assume GAP is included if you pay, but even then, I'm not sure.

## Anticipated difficulties
- Authentication will be an issue. Once I'm logged in, I can scrape ANYONE'S public data though.
- I am just sure that something will pop up between successfully authenticating and successfully using selenium.
- Handling javascript within the request implies Selenium will be used (I have not done with scrapy before)

## Scraping

### Investigation

#### Login
- Go to https://strava.com/login
- Open inspector -> network tab
- Log in and see where the form data goes

**Result:**
POST https://www.strava.com/session w/ payload
  utf8: ✓
  authenticity_token: ...
  plan: 
  email: ${email}
  password: ${pw}

-> Seems like we need to send some of the login form's response data with our POST login request.

(success)

#### Activity Detail
- Go to a personal, private activity
- Data of interest is in javascript variable `pageview`
  - `pageView.streamsRequest.streams.streamData`
  - Probably others later
  
## Running the pipeline
I handle the login manually (in browser), inspect the headers for `_strava4_session`, add
the cookie directly to the Selenium webdriver, then scrape public activities by ID.

The reason: Strava likes to lock my account when I repeatedly log in 
(as happens when running the spider over and over during testing).
I bet there are other solutions, but this one is simple.

```
STRAVA_SESSION_COOKIE=${_strava4_session} python -m scrape.py
python -m plot_grade_factor.py
```

## References
[reddit account of a person claiming to be the author of the GAP algorithm](https://www.reddit.com/user/therealslloyd/)
