# Predicting Diabetes

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-group25/HEAD?labpath=notebooks%2Fmain)
All the content in this repository is available as a static website [here](https://ucb-stat-159-s23.github.io/project-group25/)

Authors: Sam Tan, Bruce Xu, Duy Anh, Donghoon Shin

## Introduction

This project aims to understand the predictive factors for becoming diabadic. The raw dataset can be downloaded here from[Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

We compared the performance of different models to predict if a person developed diabetes. Specifically, we compared the performance of OLS,  Decision Tree, Random Forest Classification and K Nearest Neighbor (KNN) model, and we found that the Random Forest model has the highest accuracy, 0.866. The KNN model generated a very low accuracy compared to other three classification models. However, It only achieved an accuracy of 0.837 in on the test set. 

Since the Random Forest model gave the highest accuracy, we decide to further investigate the random forest model and try to optimize the accuracy of the random forest model. We attemped dropping duplicated records, but it didn't improve testing accuracy. This is reasonable because the duplicated data appeared in the original dataset was not manually added by mistake. Instead, if duplicated data appeared, it means this specific "pattern of data" just appear more frequently than other records in the dataset. We can just return to our original dataset and try another way of optimizing the model.

TODO: explain the "balance" and "Analysis of weights to get intuition" section. 


## Installation

Run `make env` will setup a new conda environment with the name with the required dependencies. To activate?? To install the tailor-made functions spcific to this project, please install the package `diabetes_analysis_tools` using  `pip install diabetes_analysis_pkg/.` after from this diirectory. Use `diabetes-analysis` kernel to execute the Jupyter Notebook. 

## Repository Structure

- `data/` contains different datasets in csv formats
  - `diabetes_012_health_indicators_BRFSS2015.csv` is XXX
  - `diabetes_binary_5050split_health_indicators_BRFSS2015.csv` is XXX 
  - `diabetes_binary_health_indicators_BRFSS2015.csv` is XXX
  - `clean.csv` is the cleaned version of `raw_data.csv` (TODO)
  - `train.csv` is the training dataset (TODO)
  - `val.csv` is the validation dataset (TODO)
  - `test.csv` is the testing dataset (TODO)
- `figures/` contains generated figures from running the notebooks in `notebooks/` (TODO)
- `notebooks/` contains the jupyter notebooks for data analysis
  - `main.ipynb` summarizes and discusses the findings and outcomes of our analysis
  - `cleaning.ipynb` prepares the data for later analysis (TODO)
  - `EDA.ipynb` conducts data visualization 
- `diabetes_analysis_pkg` contains the package, which has all the tailor-made functions for this project
  - `diabetes_analysis_tools` is the name of the package
   -  `functions.py` contains the functions (TODO)
    - `tests/` is the folder for the tests for the functions
     -  `tests_functions.py` for testing the function (TODO)
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
- `hw07-description.ipynb` Stat 159 assignment desctiption

## Makefile Commands

`make`
- `env` creates and configures the environment
- `remove-env` remove the environment
- `update-env` update the environment
- `html` build the JupyterBook normally
- `html-hub` build the JupyterBook so that you can view it on the hub with the URL proxy trick: https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html
- `clean` clean up the generated figures, data, and _build folders.
- `all` run all the notebooks (`*.ipynb` in `notebooks/` and `main.ipynb`)




