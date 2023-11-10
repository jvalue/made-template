# Project Plan

## Title
<!-- Give your project a short title. -->
Credit Card Fraud Detection

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Are there geographic or locational patterns for fraud?
2. How do transaction amounts differ between fraudulent and non-fraudulent transactions?
3. Is there a temporal pattern to fraudulent transactions?



## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
The aim of this project is to develop a robust system for the detection of fraudulent credit card transactions. Leveraging a dataset that includes anonymized transaction attributes and transaction amounts, the project focuses on building and training machine learning models to accurately classify transactions as either fraudulent or legitimate. 
The project aims to leverage machine learning techniques to build a reliable system capable of identifying potentially fraudulent credit card transactions, thereby contributing to enhanced security and fraud prevention in the financial sector.
This project involves a combination of data exploration, preprocessing, model development, and the deployment of machine learning models to address the critical issue of credit card fraud detection.




## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: ExampleSource
* Data URL: https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023
* Data Type: CSV

This dataset contains credit card transactions made by European cardholders in the year 2023. It comprises over 550,000 records, and the data has been anonymized to protect the cardholders' identities. The primary objective of this dataset is to facilitate the development of fraud detection algorithms and models to identify potentially fraudulent transactions.
Key Features
* id: Unique identifier for each transaction
* V1-V28: Anonymized features representing various transaction attributes (e.g., time, location, etc.)
* Amount: The transaction amount
* Class: Binary label indicating whether the transaction is fraudulent (1) or not (0)


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Clean the data by removing duplicates and handling missing values.
2. Conduct basic statistics, visualizations, and summary reports on the dataset to understand its characteristics.
3. Identify key features (e.g. amount, location) that are likely to influence salary predictions.
4. Decide on which regression algorithms (e.g., linear regression, random forest). Exploring other machine learning algorithms for the task.
5. Train the selected models on the training data and evaluate their performance using metrics like Mean Absolute Error (MAE), Mean Square Error(MSE).
6. Fine-tune model parameters (e.g., learning rate, max depth) to optimize performance.
7. Analyze which features have the most influence on fraud detections using techniques like permutation importance.
8. Analyze data to determine whether there are geographic or locational patterns for fraud or not,
9. Document the methodology, findings, and recommendations in a comprehensive report.
10. Deploy the trained model to make real-time predictions (Optional).


[i1]: https://github.com/jvalue/made-template/issues/1
