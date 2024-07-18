from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd


app=Flask(__name__)
@app.route('/')
#cross_origin()
def home():
    return render_template("index.html")
'''
@app.route("/predict",methods=["GET", "POST"])
#cross_origin()
def predict():
    if request.method == "POST":
'''

if __name__=="__main__":
    app.run(debug=True)


