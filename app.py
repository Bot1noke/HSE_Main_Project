from flask import Flask, render_template, request
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

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        start = int(request.form['start'])
        end = int(request.form['end'])
        df2 = pd.read_csv("steam.csv")
        mean_price = df2[start:end]['price'].mean()
        return render_template("result.html", result=mean_price)
    return render_template('main.html', head=col_names, rows=hd, result='')

@app.route('/Plots')
def index2():
    return render_template('main2.html', head=col_names, rows=hd)

if __name__ == '__main__':
    app.run(debug=True)