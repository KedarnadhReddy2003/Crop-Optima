from keras.models import Sequential
from keras.layers import Dense, Conv1D, Flatten, MaxPooling1D
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score
from numpy import unique
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer
import pickle
import os
from keras.models import load_model
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score
import tensorflow

def cnn_evaluation():

    x, y ,n_classes= training_features()

    x = np.array(x, dtype=np.float16)

    x = x.reshape(x.shape[0], x.shape[1], 1)

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.30)

    if os.path.exists("../AI_SAS/cnn_model.h5"):
        model_path = 'cnn_model.h5'
        cnn_model = tensorflow.keras.models.load_model(model_path)
        ytest = np.argmax(ytest, axis=1)
        y_pred = np.argmax(cnn_model.predict(xtest), axis=1)

        acc = accuracy_score(ytest, y_pred) * 100

        precsn = precision_score(ytest, y_pred, average="macro") * 100

        recall = recall_score(ytest, y_pred, average="macro") * 100

        f1score = f1_score(ytest, y_pred, average="macro") * 100

        print("CNN=", acc, precsn, recall, f1score)

    else:
        model = Sequential()
        model.add(Conv1D(32, 2, activation="relu", input_shape=(4, 1)))
        model.add(Dense(64, activation="relu"))
        model.add(MaxPooling1D())
        model.add(Flatten())
        model.add(Dense(n_classes, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer="adam",
                      metrics=['accuracy'])
        # model.summary()
        model.fit(xtrain, ytrain, batch_size=4, epochs=30, verbose=1)

        ytest = np.argmax(ytest, axis=1)
        y_pred = np.argmax(model.predict(xtest), axis=1)

        acc = accuracy_score(ytest, y_pred) * 100

        precsn = precision_score(ytest, y_pred, average="macro") * 100

        recall = recall_score(ytest, y_pred, average="macro") * 100

        f1score = f1_score(ytest, y_pred, average="macro") * 100

        print("CNN=", acc, precsn, recall, f1score)

        print("[INFO] Saving model...")

        model.save("cnn_model.h5")



    return acc, precsn, recall, f1score



def training_features():
    training_df =  pd.read_csv("../AI_SAS/cropdata/crop_dataset.csv", sep=',')

    x_train = training_df.iloc[:, :-1]
    y_train = training_df.iloc[:, -1]

    label_binarizer = LabelBinarizer()
    labels = label_binarizer.fit_transform(y_train)
    n_classes = len(label_binarizer.classes_)
    print("classes=", n_classes)


    return x_train,labels,n_classes



#cnn_evaluation()