from flask import Flask, render_template
import pandas as pd

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

@app.route('/Streamlit')
def index2():
    return render_template('streamlit.html', head=col_names, rows=hd)

if __name__ == '__main__':
    app.run(debug=True)