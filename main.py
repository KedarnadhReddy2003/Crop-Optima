from flask import Flask, render_template, request,flash,session
import pandas as pd
import numpy as np
import mysql.connector
from werkzeug.utils import secure_filename
import os
import io
import pickle
import base64
from werkzeug.utils import secure_filename
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
from keras.models import  load_model
import tensorflow
from prediction import img_prediction

from ANN import ann_evaluation

from CNN import cnn_evaluation

from LSTM import lstm_evaluation

#from chatbot import chat_msg


app = Flask(__name__)
app.secret_key = "1234"


ann_list=[]
ann_list.clear()
cnn_list=[]
cnn_list.clear()
lstm_list=[]
lstm_list.clear()

metrics=[]

@app.route('/')
def index():
    return render_template('index.html')

#ADMIN SECTION

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route("/admin_login_check",methods =["GET", "POST"])
def admin_login_check():
    uid = request.form.get("unm")
    pwd = request.form.get("pwd")
    if uid=="admin" and pwd=="admin":
        return render_template("admin_home.html")
    else:
        return render_template("admin.html",msg="Invalid Credentials")

@app.route("/evaluations")
def evaluations():

    return render_template("evaluations.html")

@app.route("/ahome")
def ahome():
    return render_template("admin_home.html")

#USER SECTION

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/user_reg",methods =["GET", "POST"])
def user_reg():
    name = request.form.get('name')
    uid = request.form.get('uid')
    pwd = request.form.get('pwd')
    email = request.form.get('mail')
    mno = request.form.get('mno')
    con, cur = database()
    sql = "select count(*) from users where userid='" + uid + "'"
    cur.execute(sql)
    res = cur.fetchone()[0]
    if res > 0:
        return render_template("signup.html", msg2="User Id already exists..!")
    else:
        sql = "insert into users values(%s,%s,%s,%s,%s)"
        values = (name, uid, pwd, email, mno)
        cur.execute(sql,values)
        con.commit()
        return render_template("user.html", msg1="Registered Successfully..! Login Here.")
    return ""

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/user_login_check",methods=['GET','POST'])
def user_login_check():
    uid=request.form.get('uid')
    pswd=request.form.get('pwd')
    con,cur=database()
    sql = "select count(*) from users where userid='" + uid + "' and password='" + pswd + "'"
    cur.execute(sql)
    res = cur.fetchone()[0]
    print("res",res)
    if res > 0:
        session['uid'] = uid
        qry = "select * from users where userid= '" + uid + " ' "
        cur.execute(qry)
        val = cur.fetchall()
        for values in val:
            name = values[0]
            print(name)

        return render_template("user_home.html", name=name)
    else:

        return render_template("user.html", msg="Invalid Credentials")
    return ""

@app.route("/uhome")
def uhome():
    con,cur=database()
    uid = session['uid']
    qry="select * from users where userid='"+uid+"'"
    cur.execute(qry)
    val = cur.fetchall()
    for values in val:
        name = values[0]
        print(name)

    return render_template("user_home.html",name=name)

@app.route("/detection")
def detection():
    return render_template("detection.html")

@app.route("/detection2",methods =["GET", "POST"])
def detection2():
    image = request.files['pic']
    imgdata = secure_filename(image.filename)
    filename = image.filename

    filelist = [f for f in os.listdir("testimg")]
    for f in filelist:
        os.remove(os.path.join("testimg", f))

    image.save(os.path.join("testimg", imgdata))

    image_path = "../AI_SAS/testimg/" + filename

    result = img_prediction(image_path)
    if result=="Invalid image, please select a valid image.":
        return render_template("detection.html",msg="invalid")
    print(result)

    con,cur=database()
    qry="select * from remidies where disease     " \
        "='"+result+"'"
    cur.execute(qry)
    res=cur.fetchall()
    print(res)

    return render_template("results.html",detailes=res)

@app.route("/fertilizers/<result>")
def fertilizers(result):
    con,cur=database()
    qry="select * from fertilizers where pest_name='"+result+"'"
    cur.execute(qry)
    res=cur.fetchall()
    print(res)

    return render_template("fertilizers.html",detailes=res)


@app.route("/crop_evaluations")
def crop_evaluations():
    accuracy_ann, precision_ann, recall_ann, fscore_ann = ann_evaluation()

    ann_list.append("ANN")
    ann_list.append(accuracy_ann)
    ann_list.append(precision_ann)
    ann_list.append(recall_ann)
    ann_list.append(fscore_ann)

    accuracy_cnn, precision_cnn, recall_cnn, fscore_cnn = cnn_evaluation()
    cnn_list.append("CNN")
    cnn_list.append(accuracy_cnn)
    cnn_list.append(precision_cnn)
    cnn_list.append(recall_cnn)
    cnn_list.append(fscore_cnn)

    accuracy_lstm, precision_lstm, recall_lstm, fscore_lstm = lstm_evaluation()


    lstm_list.append("LSTM")
    lstm_list.append(accuracy_lstm)
    lstm_list.append(precision_lstm)
    lstm_list.append(recall_lstm)
    lstm_list.append(fscore_lstm)

    metrics.clear()

    metrics.append(ann_list)
    metrics.append(cnn_list)
    metrics.append(lstm_list)





    accuracy_list=[accuracy_ann,accuracy_cnn,accuracy_lstm]

    bars = ('ANN', 'CNN', 'LSTM')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, accuracy_list, color=['red', 'green', 'blue'])
    plt.xticks(y_pos, bars)
    plt.xlabel('DL Algorithms')
    plt.ylabel('Accuracy')
    plt.title('Analysis between DL Accuracies')
    plt.savefig('static/accuracy.png')
    plt.clf()

    precision_list=[precision_ann,precision_cnn,precision_lstm]

    bars = ('ANN', 'CNN', 'LSTM')
    y_pos = np.arange(len(bars))
    plt2.bar(y_pos, precision_list, color=['green', 'brown', 'violet'])
    plt2.xticks(y_pos, bars)
    plt2.xlabel('DL Algorithms')
    plt2.ylabel('Precision')
    plt2.title('Analysis between DL Precisions')
    plt2.savefig('static/precision.png')
    plt2.clf()

    recall_list=[recall_ann,recall_cnn,recall_lstm]

    bars = ('ANN', 'CNN', 'LSTM')
    y_pos = np.arange(len(bars))
    plt3.bar(y_pos, recall_list, color=['orange', 'blue', 'gray'])
    plt3.xticks(y_pos, bars)
    plt3.xlabel('DL Algorithms')
    plt3.ylabel('Recall')
    plt3.title('Analysis between DL Recall')
    plt3.savefig('static/recall.png')
    plt3.clf()

    f1score_list=[fscore_ann,fscore_cnn,fscore_lstm]
    bars = ('ANN', 'CNN', 'LSTM')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, f1score_list, color=['brown', 'green', 'orange'])
    plt.xticks(y_pos, bars)
    plt.xlabel('DL Algorithms')
    plt.ylabel('F1-Score')
    plt.title('Analysis between DL F1-Score')
    plt4.savefig('static/f1score.png')
    plt4.clf()



    return render_template("crop_evaluations.html", evaluations=metrics)





@app.route("/crop_detection")
def crop_detection():
    return render_template("crop_detection.html")




@app.route("/crop_prediction",methods =["GET", "POST"])
def crop_prediction():

    temperature = request.form.get("temp")
    humidity = request.form.get("humd")
    ph = request.form.get("ph")
    rainfall = request.form.get("rainfall")


    X_test=[[float(temperature),float(humidity),float(ph),float(rainfall)]]
    print(X_test)

    model_path = 'lstm_model.h5'
    model = tensorflow.keras.models.load_model(model_path)
    prediction = model.predict(np.array(X_test, ndmin=0))
    #prediction = model.predict(X_test)
    lb = pickle.load(open('label_transform.pkl', 'rb'))
    prediction_result = lb.inverse_transform(prediction)[0]

    print(prediction_result)

    con, cur = database()
    qry = "select * from crop_fertilizers where crop_name='" + prediction_result + "' "
    cur.execute(qry)
    fertilizer = cur.fetchone()[1]
    print("fertilizer=", fertilizer)

    return render_template("crop_detection.html",result=prediction_result,fertilizer=fertilizer)


#DATABASE CONNECTION
def database():
    con = mysql.connector.connect(host="127.0.0.1", user='root', password="root", database="ai_sas")
    cur = con.cursor()
    return con, cur

if __name__ == '__main__':
    app.run(debug=True,port="2024")
