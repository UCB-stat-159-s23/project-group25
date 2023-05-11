[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LiaEl886)
# Predicting Diabetes

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-group25/HEAD?labpath=notebooks%2Fmain)

All the content in this repository is available as a static website [here](https://ucb-stat-159-s23.github.io/project-group25/)

Authors: Sam Tan, Bruce Xu, Duy Anh Dang, Donghoon Shin

## Introduction

This project is dedicated to identifying predictive factors for the development of diabetes. The raw dataset is accessible on [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset).

We evaluated the performance of several models, including OLS, Decision Tree, Random Forest Classification, and K Nearest Neighbor (KNN), to predict whether an individual would develop diabetes. Our findings showed that the Random Forest model provided the highest accuracy, at 0.866. The KNN model, in contrast, demonstrated notably lower accuracy than the other three classification models, reaching only an accuracy of 0.837 on the test set.

Given its superior performance, we decided to delve deeper into the Random Forest model in an attempt to optimize its accuracy. We explored the impact of removing duplicate records but found that this didn't enhance test accuracy. This finding aligns with our expectation, as the presence of duplicate data in the original dataset was not due to manual errors. Rather, repeated patterns of data indicated that certain records appeared more frequently in the dataset. 

Installation Instructions

To set up a new conda environment with the necessary dependencies, run make env. Activate the environment with conda activate diabetes_analysis. Use the diabetes-analysis kernel to run the Jupyter Notebook.

To utilize the custom functions designed specifically for this project, you'll need to install the diabetes_analysis_tools package. After setting the working directory to this repository using cd .., run pip install -e diabetes_analysis_pkg/. Note: please restart the kernel after installation. This is because the running kernel does not continuously monitor changes in the installed packages.


## Repository Structure

- `data/` contains different datasets in csv formats
  - `diabetes_012_health_indicators_BRFSS2015.csv`
  - `diabetes_binary_5050split_health_indicators_BRFSS2015.csv`
  - `diabetes_binary_health_indicators_BRFSS2015.csv`
  - `clean.csv` is the cleaned version of the data ready for analysis. 
  - `xtrain.csv` is the training dataset with features
  - `ytrain.csv` is the training dataset with labels
  - `xtest.csv` is the testing dataset with features
  - `ytest.csv` is the testing dataset with labels
- `figures/` contains generated figures from running the notebooks in `notebooks/` 
- `notebooks/` contains the jupyter notebooks for data analysis
  - `main.ipynb` summarizes and discusses the findings and outcomes of our analysis
  - `EDA.ipynb` conducts exploratory data analysis and data visualization 
- `diabetes_analysis_pkg` contains the package, which has all the tailor-made functions for this project
  - `diabetes_analysis_tools` is the name of the package
  - `setup.py` required to create python package
  - `pyproj.tml` required to create python package
  - `setup.cfg` required to create python package
- `_config.yml` required for JupyterBook
- `conf.py` required for JupyterBook
- `_toc.yml` is the table of contents for JupyterBook
- `environment-jupyterbook.txt` packages for the book build in Github Actions
- `environment.yml` is the conda environment for this repo.
- `Makefile` make commands for easy execution
- `LICENSE` contains the license used by the repo
- `README.md` current document

## Makefile Commands

`make`
- `env` creates and configures the environment
- `remove-env` remove the environment
- `update-env` update the environment
- `html` build the JupyterBook normally
- `html-hub` build the JupyterBook so that you can view it on the hub with the URL proxy trick: https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html
- `clean` clean up the generated figures and _build folders.
- `all` run all the notebooks (`*.ipynb` in `notebooks/` and `main.ipynb`)




