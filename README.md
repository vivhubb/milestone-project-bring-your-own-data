## Table of Contents
<!-- TOC -->

- [Table of Contents](#table-of-contents)
- [Dataset Content](#dataset-content)
- [Business Requirements](#business-requirements)
- [Hypothesis and validation](#hypothesis-and-validation)
- [The rationale to map the business requirements to the Data Visualizations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualizations-and-ml-tasks)
- [ML Business Case](#ml-business-case)
- [Dashboard Design](#dashboard-design)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
- [Acknowledgements optional](#acknowledgements-optional)

<!-- /TOC -->

## Dataset Content
* This dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/nehalbirla/motorcycle-dataset) and contains information about 1061 used motorcycles.

* We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.

* The dataset has 7 features that could potentially affect their prices. The features are the following: name, selling price, year, seller type, owner, km driven, ex showroom price.

|Variable|Meaning|Units|
|:----|:----|:----|
|name|Motorcycle brand and model name|Text|
|selling_price|Price at which the motorcycle is being sold|5.000-760.000|
|year|Year in which the motorcycle was manufactured|Year from 1988 to 2020|
|seller_type|Type of seller who sold the motorcycle|Dealer or Individual
|owner|Count of owners of the motorcycle|1st, 2nd, 3rd, 4th owner
|km_driven|Number of kilometers driven with the motorcycle|350-880.000
|ex_showroom_price|Price of the motorcycle when it was new|30.490-1.278.000

[Back to TOP](#table-of-contents)

## Business Requirements
* The goal of this project is to develop a model that can predict the selling price of used motorcycles based on several features such as the year, seller type, number of previous owners, kilometers driven, and the ex-showroom price.

* This model can be useful for individuals who are looking to buy or sell a used motorcycle, as well as for dealerships who want to determine the fair market value of the motorcycles they have on their inventory. By accurately predicting the selling price of a used motorcycle, potential buyers and sellers can make more informed decisions and negotiate prices more effectively.

1. The client is interested to see how the motorcycle attributes correlate with the sale prices.
1. The client is interested to predict used motorcycle prices.

[Back to TOP](#table-of-contents)


## Hypothesis and validation
* We initially suspected that the 2 most important features would be the year and the Kms driven.

* The correlation study showed that another important feature is the ex showroom price. Based on these result we decided to create the price predictor based on these 3 most important features.

* To validate our hypothesis we performed: Data exploration and cleaning, Model selection and training, Model evaluation, Interpretation and visualization

[Back to TOP](#table-of-contents)


## The rationale to map the business requirements to the Data Visualizations and ML tasks
* Business Requirement 1: Data Visualization and Correlation study
    - The business requires data visualizations and a correlation study to better understand the relationships between the different features in the dataset and the selling price of a used motorcycle.
    - The use of scatterplots, heatmaps, or correlation matrices to visualize the relationships between the different features and the selling price.
    - Identifying any outliers or anomalies that may affect the accuracy of the model.
* Business requirement 2:
    - We are interested in predicting the selling price of a used motorcycle based on its features.
    - We want to build a regression model for price prediction
    - We want to build a feature that allows for multiple predictions

[Back to TOP](#table-of-contents)


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.

