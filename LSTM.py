
import pandas as pd
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
import numpy as np
from tensorflow.keras.layers import Input, Dense, LSTM
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.layers import Embedding
import os
from sklearn.preprocessing import LabelBinarizer
import pickle
from keras.models import load_model
import tensorflow

def lstm_evaluation():
    training_df = pd.read_csv("../AI_SAS/cropdata/crop_dataset.csv", sep=',')

    x_train = training_df.iloc[:, :-1]
    y_train = training_df.iloc[:, -1]

    label_binarizer = LabelBinarizer()
    labels = label_binarizer.fit_transform(y_train)

    pickle.dump(label_binarizer, open('label_transform.pkl', 'wb'))
    n_classes = len(label_binarizer.classes_)


    # split the training and test data
    train_features, test_features, train_targets, test_targets = train_test_split(x_train, labels,
                                                                                  train_size=0.7,
                                                                                  test_size=0.3,
                                                                                  random_state=23,
                                                                                  stratify=labels
                                                                                  )

    if os.path.exists("../AI_SAS/lstm_model.h5"):
        model_path = 'lstm_model.h5'
        lstm_model = tensorflow.keras.models.load_model(model_path)

        ytest = np.argmax(test_targets, axis=1)

        y_pred = np.argmax(lstm_model.predict(test_features), axis=1)

        acc = accuracy_score(ytest, y_pred) * 100

        precsn = precision_score(ytest, y_pred, average="macro") * 100

        recall = recall_score(ytest, y_pred, average="macro") * 100

        f1score = f1_score(ytest, y_pred, average="macro") * 100
    else:
        model = Sequential()
        model.add(Embedding(5000, 32, input_length=4))
        model.add(LSTM(150))
        model.add(Dense(n_classes, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        # print(model.summary())
        model.fit(train_features, train_targets, epochs=30, batch_size=4)

        model.save("lstm_model.h5")

        ytest = np.argmax(test_targets, axis=1)

        y_pred = np.argmax(model.predict(test_features), axis=1)

        acc = accuracy_score(ytest, y_pred) * 100

        precsn = precision_score(ytest, y_pred, average="macro") * 100

        recall = recall_score(ytest, y_pred, average="macro") * 100

        f1score = f1_score(ytest, y_pred, average="macro") * 100



    print(acc)
    print(precsn)
    print(recall)
    print(f1score)


    return acc,precsn,recall,f1score


#lstm_evaluation()


