from flask import Flask
from flask import render_template
from datetime import datetime
import pyrebase
from math import log
config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "https://zoohack-bbff3.firebaseio.com",
  "storageBucket": ""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


app = Flask(__name__)
@app.route('/')
def hello_world():
    events=[]
    problems=db.child("problems").get().val()
    for problem in problems:
        pr = problems[problem]
        if type(pr)==type(1):
            continue
        print("fdfdfdffffffffffffffffffffffffff")
        print(pr)
        time=datetime.utcfromtimestamp(pr["time"]).strftime('%Y-%m-%d %H:%M:%S')
        users= db.child("users").get().val()
        for x in users: #very very bad code
            if users[x]['name'] == pr["author"]:
                user= users[x]
                break

        print("ffdfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        print(user)
        srt=1
        if pr["level"]=="gold":
            srt=2
        elif pr["level"]=="tomato":
            srt=3
        g=1
        if (pr["rate"]+1) * (user["karma"]+1) < 1:
            t=abs((pr["rate"]+1) * (user["karma"]+1))
            g=-1
        cf = g * srt * log((pr["rate"]+1) * (user["karma"]+1) )
        events.append({ "ts":pr["time"],"cf":cf, "srt":srt,"title":pr["name"], "dis":pr["dis"], "level":pr["level"], "adress":pr["place"], "name": pr["author"], "good":pr["rate"], "time":time,"phone":user["phone"],"rep":user["karma"]})

    return render_template("admin.html",events=events)

if __name__ == '__main__':
    app.run()
