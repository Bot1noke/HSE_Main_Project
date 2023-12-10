from flask import Flask, render_template
import pandas as pd
import streamlit as st

df = pd.read_csv("steam.csv")
hd = df[:20].values.tolist()
col_names = df.columns
col_names = list(col_names)

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
posts = [

]

@app.route('/')
def index():
    return render_template('main.html', head=col_names, rows=hd)

@app.route('/Anal')
def index2():
    return render_template('main_anal.html', head=col_names, rows=hd)

@app.route('/dora1')
def index3():
    return render_template('dora1.html', head=col_names, rows=hd)

@app.route('/dora2')
def index4():
    return render_template('dora2.html', head=col_names, rows=hd)

@app.route('/dora3')
def index5():
    return render_template('dora3.html', head=col_names, rows=hd)

if __name__ == '__main__':
    app.run(debug=True)