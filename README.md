<h1 align="center">Covid-19 Global Dashboard 🦠 </h1>

## Motivation:
This Covid-19 dashboard was created from scratch to visuvalize the global trend of infections and to keep track of the spread of the virus during the pandemic. This dashboard was of a great support to spread awarness amoung the residents of my gated community. 

## Resources for the Covid dashboard:
- <a href="https://github.com/CSSEGISandData/COVID-19">Covid-19 datasets source</a>
- <a href="https://plotly.com/python/indicator/">Indicator</a>
- <a href="https://plotly.com/python/pie-charts/">pie chart</a>
- <a href="https://plotly.com/python/line-charts/">Line Chart</a>
- <a href="https://plotly.com/python/bar-charts/">Bar Chart</a>
- <a href="https://plotly.com/python/scattermapbox/">Scatter mapbox</a>
- <a href="https://account.mapbox.com/auth/signin/">Mapbox Account</a>
- <a href="https://dash.plotly.com/dash-core-components/rangeslider">Range Slider</a>
- <a href="https://plotly.com/python/marker-style/">Marker Style</a>
- <a href="https://dash.plotly.com/datatable">Data Table</a>
- <a href="https://plotly.com/python/bubble-charts/">Bubble Chart</a>

## Libraries used:
- <a href="https://pandas.pydata.org/">Pandas</a>
- <a href="https://dash.plotly.com/dash-html-components">Dash HTML components</a>
- <a href="https://dash.plotly.com/dash-core-components">Dash core components</a>
- <a href="https://plotly.com/dash/">Dash</a>

## Description:
Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. We are using face classifier in this project. You can experiment with other classifiers as well. 

- You need to download the trained classifier XML file (haarcascade_frontalface_default.xml), which is available in OpenCv’s GitHub repository.
- The detection works only on grayscale images/frames from video. So it is important to convert the color image to grayscale.
- detectMultiScale function is used to detect the faces. It takes 3 arguments — the input image, scaleFactor and minNeighbours. 
- scaleFactor specifies how much the image/frame size is reduced with each scale. minNeighbours specifies how many neighbors each candidate rectangle should have to retain it. 
- You may have to tweak these values to get the best results.
- Faces contains a list of coordinates for the rectangular regions where faces were found. We use these coordinates to draw the rectangles over the detected face.

## Steps used to deploy Covid-19 Dash app on Heroku:

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
