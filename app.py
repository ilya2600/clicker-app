from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


db = sqlite3.connect("data.db")
db.execute("CREATE TABLE IF NOT EXISTS clicks (count INTEGER)")
db.execute("INSERT INTO clicks (count) VALUES (0)")
rows = db.execute("SELECT * FROM clicks").fetchall()
print(rows)

count = 0

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        global count
        count += 1
    return render_template("index.html", count=count) 
    


if __name__=="__main__":
    app.run()
