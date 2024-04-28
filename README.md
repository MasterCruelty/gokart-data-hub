[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=MasterCruelty_gokart-data-hub&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=MasterCruelty_gokart-data-hub)
[![Quality Gate Pass](https://sonarcloud.io/api/project_badges/measure?project=MasterCruelty_gokart-data-hub&metric=alert_status)](https://sonarcloud.io/dashboard?id=MasterCruelty_gokart-data-hub)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=MasterCruelty_gokart-data-hub&metric=ncloc)](https://sonarcloud.io/dashboard?id=MasterCruelty_gokart-data-hub)
![License](https://img.shields.io/github/license/MasterCruelty/gokart-data-hub)
[![image](https://img.shields.io/github/stars/MasterCruelty/gokart-data-hub)](https://github.com/MasterCruelty/gokart-data-hub/stargazers)
[![image](https://img.shields.io/github/forks/MasterCruelty/gokart-data-hub)](https://github.com/MasterCruelty/gokart-data-hub/network/members)
![CodeSize](https://img.shields.io/github/languages/code-size/MasterCruelty/gokart-data-hub)
[![image](https://img.shields.io/github/issues/MasterCruelty/gokart-data-hub)](https://github.com/MasterCruelty/gokart-data-hub/issues)
![image](https://img.shields.io/github/languages/top/MasterCruelty/gokart-data-hub)
![image](https://img.shields.io/github/commit-activity/w/MasterCruelty/gokart-data-hub)
![image](https://img.shields.io/github/contributors/MasterCruelty/gokart-data-hub)

# gokart-data-hub
# What is it?
A simple tool made in python with pandas and matplotlib, which analyzes a csv containing gokart data about your races. Then it will plot a few graphs to show better your trend throught the years.

### Contribute
Feel free to contribute and improve the project. You can read the guidelines to contribute [here](https://github.com/MasterCruelty/gokart-data-hub/blob/main/CONTRIBUTING.md)

# Libraries used
* pandas
* matplotlib
* seaborn

# Data description
![image](https://github.com/MasterCruelty/gokart-data-hub/assets/72561502/43028072-b3cf-4ea0-8a01-9b2308c0b923)
* date: when the race was held
* kart-type: if is a fuel kart or an electric one.
* race-type: if it's a free laps session or a real race.
* position: Position Conquered.
* track-type: if it's indoor or outdoor track.
* condition: track condition(rained, standard or other)
* kart-type: motor power.
* avg-speed: average speed during the race.
* best-time: best of all times in that race.
* avg-time: average time during the race.
* best-time(TIME) and avg-time(TIME): just for cute visualization of times but terrific to manage in python.

The last info mentioned about data is a limit for the graphic visualization. That's because you're gonna see on the something like "54" or "54,2" instead of a more beautiful data such as "00:54:483".<br>
<i>Any hint or help is appreciated, read more about contributing below on this readme.</i>


# Usage
Launch the program by typing the following command.
```ruby
python kart-analytics.py
```
<br><b>The main menu looks like this:<br></b>

![image](https://github.com/MasterCruelty/gokart-data-hub/assets/72561502/266dc479-72e3-4372-8fe4-01dbcfb41a94)

<br><b>For example we choose option 4, the following chart is the output:</b><br>

![image](https://github.com/MasterCruelty/gokart-data-hub/assets/72561502/427f9f33-f9f6-4d56-9429-5667831adb9b)

<h3><b>This is the linear regression of all best time that I did in Dromokart track.</b></h3>
