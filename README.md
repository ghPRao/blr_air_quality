# AIR_Qualaity Index

## Introduction
While we take it for granted every breath we take in our lifetime, we care about the air quality only when it is reported to be dangerous or hazardous. An air quality index (AQI) is used by government agencies to communicate to the public how polluted the air currently is or how polluted it is forecast to become. AQI warnings are an important public safety strategy because it has been observed that the public health risks increase in those communities where the AQI rises. For example, Bay Area AQI in recent years was dangerously low enough to close down schools and businesses impacting daily routines, especially when the forest fire.

There are many websites where you can find AQI historical data. In this exercise we will do data collection from en.titiempo.net by scrapping historical San Francisco AQI data for creating visuals and use it in machine learning models. As a first step, let us scrape data on the annual average climate data.

## Historical Climate Data Collection.
For the data relevant to San Francisco area, after opening the website en.titiempo.net, navigate to the continent ‘North America’, and select the country ‘United States’.

You can further navigate to San Francisco, San Francisco International Airport after clicking on the ‘California’ state.

## Get curious to uncover more data
When you carefully observe the weblink, it shows as https://en.tutiempo.net/climate/ws-724940.html. Here 724940 signifies the city of San Francisco. When you further explore by clicking the year 2020, and select January, you will uncover lot more features.

After clicking the year 2020 and the month January, when you explore the weblink, it looks like this https://en.tutiempo.net/climate/01-2020/ws-724940.html. Like before ws-724940 refers to San Francisco and 01–2020 refers to month (January) and year (2020).

## Using Python to perform Data Collection
When you run the python program, you will download San Francisco climate date for each month for the years 2011 through 2020. In the next story we can combine these data and also download Air Quality Index data from another source.

## Machine Learning Algorithms
We will run several supervised machine learning models. For traing the data, we will seperate it as a 70% training data and 30 percent test data.

### Linear Regression Model
Linear regression is the next step up after correlation. It is used when we want to predict the value of a variable based on the value of another variable. The variable we want to predict is called the dependent variable (or sometimes, the outcome variable).


### Lasso Regression
> The Mean absolute error represents the average of the absolute difference between the actual and predicted values in the dataset. It measures the average of the residuals in the dataset. The Mean absolute error represents the average of the absolute difference between the actual and predicted values in the dataset. It measures the average of the residuals in the dataset. MAE: 40.94026692671051.

> Mean Squared Error represents the average of the squared difference between the original and predicted values in the data set. It measures the variance of the residuals. MSE: 3037.578810224082

> Root Mean Squared Error is the square root of Mean Squared error. It measures the standard deviation of residuals. RMSE: 55.114234188856166
