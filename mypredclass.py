# %%
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn import metrics as m
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.linear_model import LinearRegression as lr
import numpy as np

# %%

class predictclass :

    def __init__(self) :
        dataset = p.read_csv("train.csv")
        y = dataset['price_range']
        x = dataset.drop(['price_range','blue','wifi'], axis = 1)


        # %%
        xtrain,xtest,ytrain,ytest =  train_test_split(x,y, train_size= 0.5);

        # %%
        self.LR = lr()

        # %%
        self.LR.fit(xtrain, ytrain)