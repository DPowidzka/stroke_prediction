# Stroke Prediction

Stroke is ranked as the second leading cause of death and remains a significant public health burden despite the advancements in the understanding of the disease. Early prediction and intervention can help in reducing the severity of the disease and improving the quality of life for individuals.

This project aims to identify insights about stroke predictions based on input parameters such as age, gender, smoking status, comorbidities, and more. By analyzing and building models using these features, we can predict the likelihood of a stroke occurring in a given individual.

## Dataset

The dataset used in this project is related to stroke prediction. It contains various parameters such as:

- **Age**: The age of the individual.
- **Gender**: The gender of the individual.
- **Hypertension**: Whether the individual has hypertension or not.
- **Heart disease**: Whether the individual has heart disease or not.
- **Smoking status**: The smoking status of the individual (e.g., never smoked, formerly smoked, smokes).
- **BMI**: The body mass index of the individual.
- **Average glucose level**: The average glucose level of the individual.
- **Work type**: The type of work the individual does.
- **Residence type**: Whether the individual lives in an urban or rural area.
- **Stroke**: Whether the individual has had a stroke (target variable).

## Objective

The goal of this analysis is to explore the dataset, clean the data, and understand relationships between various features in predicting stroke risk. This can eventually be used to build a predictive model for stroke prediction.

## Importing Necessary Modules

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
