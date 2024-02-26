### CROP HARVEST SEASON PREDICTION
#### Introduction
This project is aim to predict the harvesting season of some crop in some part of Africa countries
The data set comprises of  seven columns including the target variable
In the dataset we have four quantitative or numerical variable and three categorical variable
The numerical columns include Temperature, Humidity, Water availability, pH, while the categorical columns are Country, Crops or plant and the target which is the harvesting season
#### Data Assessing
The dataset is only concerned with four countries which includes Nigeria, Kenya, South Africa and Sudan
The plant grown in this areas are Maize, Rice Cotton, blackgram,chickpea,jute,kidneybeans,lentil, mothbeans, mungbean, muskmelon,pigeonpeas, watermelon
and the harvest seasons include rainy, winter, summer, spring.
#### Exploratory data analysis
According to report, it was indicated that Rice, jute, pigeonpeas required lot of water for their cultivation and they are mostly harvested during rainy period
while maize can have two harvesting season which are rain and winter. cotton, chicken pea, blackgram are mostly harvested during winter.
mothbeans, muskmelon and watermelon are harvested in summer, finally kidneybeans is harvested during spring
Also Sudan hardly plant crop that require alot of water for their cultivation
#### Model training
The dataset is splitted into train and test with 80 to 20 percent respectively, using decision tree classifier for the training.
The training accuracy is 98% while the test accuracy is 90% but after hyperparameter tunning the test accuracy improved by 1%.
#### Model deployment
The model is deployed for user interaction using streamlit
#### Summary
The dataset provided is a bit imbalance, suggested to get add more data to the minority classes to improve the model performance or balance the classes
### Conclusion
In conclusion water availability and Humidity play a vital role in the performance of the model.
Although I suggest improvement or conduct more research that can foster the performance of the model

