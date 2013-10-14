from flask import Flask,render_template
app_fl = Flask(__name__)

@app_fl.route('/index')
def index_pg():
    with open("tentitles.txt","r") as f:
        sugg = f.read()
    return render_template('titles.html',title=sugg)

if __name__ == '__main__':
    app_fl.run(debug=True)
