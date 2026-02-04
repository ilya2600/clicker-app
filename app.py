from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


db = sqlite3.connect("data.db")
db.execute("CREATE TABLE IF NOT EXISTS clicks (count INTEGER)")

rows = db.execute("SELECT * FROM clicks").fetchall()

if len(rows) == 0:
    db.execute("INSERT INTO clicks (count) VALUES (0)")
# rows = db.execute("SELECT * FROM clicks").fetchall()
# print(rows)
db.commit()
db.close()


@app.route("/", methods=['GET','POST'])
def index():
    db = sqlite3.connect("data.db")
    
    if request.method == "POST":
        db.execute("UPDATE clicks SET count = count + 1")
        
    rows = db.execute("SELECT * FROM clicks").fetchall()
    db.commit()
    db.close()
    return render_template("index.html", rows=rows) 
    


if __name__=="__main__":
    app.run()
