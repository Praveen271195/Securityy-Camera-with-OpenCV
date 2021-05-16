<h1 align="center">Covid-19 Global Dashboard 🦠 </h1>

## Motivation:
This Covid-19 dashboard was created from scratch to visuvalize the global trend of infections and to keep track of the spread of the virus during the pandemic. This dashboard was of a great support to spread awarness amoung the residents of my gated community. 

## Libraries used:
-
Thi

## Synopsis:
Motion detetion is one of the best applications of OpenCV and this is has been used to build acan be 

## Instructions:
Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. We are using face classifier in this project. You can experiment with other classifiers as well. 

- You need to download the trained classifier XML file (haarcascade_frontalface_default.xml), which is available in OpenCv’s GitHub repository.
- The detection works only on grayscale images/frames from video. So it is important to convert the color image to grayscale.
- detectMultiScale function is used to detect the faces. It takes 3 arguments — the input image, scaleFactor and minNeighbours. 
- scaleFactor specifies how much the image/frame size is reduced with each scale. minNeighbours specifies how many neighbors each candidate rectangle should have to retain it. 
- You may have to tweak these values to get the best results.
- Faces contains a list of coordinates for the rectangular regions where faces were found. We use these coordinates to draw the rectangles over the detected face.

## Libraries used:
- <a href="https://opencv.org/">OpenCV</a>
- <a href="https://docs.python.org/3/library/winsound.html">winsound</a>

## Credits:
- <a href="https://www.youtube.com/">YouTube</a> for tutorials
