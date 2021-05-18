<h1 align="center">Covid-19 Global Dashboard 🦠 </h1>

## Motivation:
This Covid-19 dashboard was created from scratch to visuvalize the global trend of Corona Virus infections in the simplest way and to keep track of the spread of the virus during the pandemic. This dashboard was of a great support to spread awarness amoung the residents of my gated community.

## About the Application:
A web dashboard deployed on Heroku at https://dd-covid-dashboard.herokuapp.com/. Built in Python and Dash, with charts made in Plotly. The data is provided by Johns Hopkins Center for Systems Science and Engineering which is updated every day.

### App Layout:
[<img src='https://media.giphy.com/media/JiBNaric6Jecnd535A/giphy.gif' alt='CovidDashApp' height='400'>](https://dd-covid-dashboard.herokuapp.com/)

There are five main components in the covid dashboard,
1. <b>Indicators</b>: There are four indicators and they are: Confirmed, Deaths, Recovered and Active cases on the global scale.

[<img src='https://github.com/Praveen271195/Praveen271195/blob/main/Indicators.PNG' alt='Indicators' height='350'>](https://dd-covid-dashboard.herokuapp.com/)

- CONFIRMED is the running total of all cases tested and confirmed in the selected region.
- DEATHS measures the running total of all COVID-19-related deaths.
- RECOVERED indicates the number of cases in which the patient is deemed to have recovered from the illness.
- ACTIVE measures only the cases active today. (Active cases are calculated as ACTIVE = CONFIRMED - DEATHS - RECOVERED)
 
2. <b>Dropdown box</b>: Dropdown list box is for the user to select the country for which the Covid tracker has to be visuvalized. Absolute new infection numbers, new deaths reported, new recoveries and active cases in a day within the selected region in shown is the data card below.

[<img src='https://github.com/Praveen271195/Praveen271195/blob/main/Dropdown.png' alt='Dropdown' height='400'>](https://dd-covid-dashboard.herokuapp.com/)

3. <b>Donut Chart</b>: Division of total cases in a country is shown via Donut chart. It help us know teh adversity of the countries situation. Hovering on the chart will show the respective percentage of Deaths/Acive cases/Recoveries.

[<img src='https://github.com/Praveen271195/Praveen271195/blob/main/Donut_chart.png' alt='DonutChart' height='400'>](https://dd-covid-dashboard.herokuapp.com/)

4. <b>Line and bar chart</b>: Combination of line and bar chart will show the last 60 days, daily confirmed cases in the selected country. A rolling average of last 7 days is also shown with the help of a line chart to see the trend clealy. In the below snap shot, the trend of confirmed cases in India is reducing. Good news! :D

[<img src='https://github.com/Praveen271195/Praveen271195/blob/main/Line%26Bar_chart.png' alt='LineAndBarChart' height='400'>](https://dd-covid-dashboard.herokuapp.com/)

5. <b>Dynamic Map</b>: The infection map features a circular marker over each sub-region. The size of the marker is relative to the CONFIRMED cases of that region. When the mouse poiter is hovered over the country/location that is selected from the dropdown, NAME of the country, Cummilative CONFIRMED cases, DEATHS and RECOVERIES are displayed. The map is zoomable and dragable for ease of use.

[<img src='https://github.com/Praveen271195/Praveen271195/blob/main/Map.PNG' alt='Map' height='400'>](https://dd-covid-dashboard.herokuapp.com/)

## Libraries used:
- <a href="https://pandas.pydata.org/">Pandas</a>
- <a href="https://dash.plotly.com/dash-html-components">Dash HTML components</a>
- <a href="https://dash.plotly.com/dash-core-components">Dash core components</a>
- <a href="https://plotly.com/dash/">Dash</a>

## Resources for Covid dashboard:
- <a href="https://github.com/CSSEGISandData/COVID-19">Covid-19 datasets source</a>
- <a href="https://plotly.com/python/indicator/">Indicator</a>
- <a href="https://plotly.com/python/pie-charts/">Pie chart</a>
- <a href="https://plotly.com/python/line-charts/">Line Chart</a>
- <a href="https://plotly.com/python/bar-charts/">Bar Chart</a>
- <a href="https://plotly.com/python/scattermapbox/">Scatter mapbox</a>
- <a href="https://account.mapbox.com/auth/signin/">Mapbox Account</a>
- <a href="https://dash.plotly.com/dash-core-components/rangeslider">Range Slider</a>
- <a href="https://plotly.com/python/marker-style/">Marker Style</a>
- <a href="https://dash.plotly.com/datatable">Data Table</a>
- <a href="https://plotly.com/python/bubble-charts/">Bubble Chart</a>

## Description:
Transforming from wide to long format can be done quite simple with Pandas function "melt".

For more convenient analysis, the next step is to combine confirmed, deaths and recoveries tables into a single one.
The CSSE Covid-19 dataset consists of three tables about daily confirmed, deaths and recoveries cases per country/region. Each table presents the data in wide (crosstab) format, with each day in a column. This format is very difficult to work with. so the first major preprocessing step is to pivot the data in these columns into rows. Transforming from wide to long format can be done quite simple with Pandas function "melt".

Combining Tables

## Instructions to deploy Covid-19 Dash app on Heroku:

1. Sign up for account on Heroku
2. Create your App name (this will be part of the url)
3. Download and install Heroku CLI (allow you to create and manage your Heroku apps directly from the terminal)
4. Create new project in Pycharm (where your app code and files will be located)
a. Choose new environment using Virtualenv
b. Select a python Base interpreter (no need to check the boxes under interpreter)
5. Create a new .py file to start writing the code for your app. If you already created the code for your app, copy those files into your new project folder.
6. Inside your app’s file, under “app = dash.Dash(__name__)”, add this line: server = app.server
7. Open terminal, and cd into your project folder if necessary
8. Pip install any libraries and specific versions your app needs.
    a. pip install numpy
    b. pip install pandas
    c. pip install plotly
    d. pip install dash
    e. pip install gunicorn (needed to run app on heroku)
9. Create .gitignore file inside your project folder (tells Git which files or folders to ignore in a project) and add these lines into it:
    a. venv *.pyc .env .DS_Store (4 separate lines)
10. Create a Procfile inside same folder and add this line inside:
    a. web: gunicorn YourAppFileWithout.py:server
11. Create requirements. Go back to terminal, cd to project folder if necessary, and type:
    a. pip freeze &gt; requirements.txt
12. Inside terminal, type the following- heroku login
13. Then type- git init (don’t forget to ensure you have git installed)
14. heroku git:remote -a AppNameFromStep2
15. git add .
16. git commit -am &quot;initial launch&quot;
17. git push heroku master

## Link to Dash app:

https://dd-covid-dashboard.herokuapp.com/

## Credits:
- <a href="https://www.youtube.com/">YouTube</a> for tutorials
- <a href="https://github.com/CSSEGISandData/COVID-19">JHU CSSE COVID-19 Data</a> for data source

## Made with care in India by the Data Detective 
<img src='https://github.com/Praveen271195/Praveen271195/blob/main/Data%20Detective%20Logo.png' alt='DD_Logo' height='100'>
