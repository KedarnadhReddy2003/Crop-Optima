# first neural network with keras tutorial
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score
#from DBConfig import DBConnection
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from keras.models import load_model
import pickle
import numpy as np
import tensorflow

def ann_evaluation():

    # load the dataset
    x, y,n_classes= training_features()

    x = np.array(x, dtype=np.float16)

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=0.7,test_size=0.3,random_state=23,stratify=y)

    if os.path.exists("../AI_SAS/ann_model.h5"):

        model_path = 'ann_model.h5'

        ann_model = tensorflow.keras.models.load_model(model_path)

        ytest = np.argmax(ytest, axis=1)
        y_pred = np.argmax(ann_model.predict(xtest), axis=1)

        acc = accuracy_score(ytest, y_pred) * 100

        precsn = precision_score(ytest, y_pred, average="macro") * 100

        recall = recall_score(ytest, y_pred, average="macro") * 100

        f1score = f1_score(ytest, y_pred, average="macro") * 100

        print("ANN=", acc, precsn, recall, f1score)
    else:
        model = Sequential()
        model.add(Dense(32, input_shape=(4,), activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(n_classes, activation='softmax'))
        # compile the keras model
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # fit the keras model on the dataset
        model.fit(xtrain, ytrain, epochs=20, batch_size=4)

        model.save("ann_model.h5")

        ytest = np.argmax(ytest, axis=1)
        y_pred = np.argmax(model.predict(xtest), axis=1)

        acc = accuracy_score(ytest, y_pred) * 100

        precsn = precision_score(ytest, y_pred, average="macro") * 100

        recall = recall_score(ytest, y_pred, average="macro") * 100

        f1score = f1_score(ytest, y_pred, average="macro") * 100

        print("ANN=", acc, precsn, recall, f1score)

        print(acc)
        print(precsn)
        print(recall)
        print(f1score)



    return acc,precsn,recall,f1score


def training_features():

    training_df = pd.read_csv("../AI_SAS/cropdata/crop_dataset.csv", sep=',')


    #le = LabelEncoder()
    #le.fit(training_df.iloc[:, -1])
    x_train = training_df.iloc[:, :-1]
    y_train = training_df.iloc[:, -1]

    label_binarizer = LabelBinarizer()
    labels = label_binarizer.fit_transform(y_train)
    n_classes = len(label_binarizer.classes_)
    print("classes=",n_classes)

    return x_train,labels,n_classes




#ann_evaluation()