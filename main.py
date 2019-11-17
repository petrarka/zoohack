from flask import Flask
from flask import render_template
app = Flask(__name__)
a={"title":"Лес подгорает","level":"tomato", "disc":"лес сильно горит","adress":"bibins ul bubova d2","name":"Вася","lastName":"пупкин","phone":"880012345443","rep":-3,"good":10,"bad":2}
b={"title":"Кабаны умирают","level":"forestgreen", "disc":"кабаны заболели","adress":"bibins ul bobova d22","name":"Вася","lastName":"Куркин","phone":"65655445443","rep":5,"good":100,"bad":22}
events=[a,b,a]
@app.route('/')
def hello_world():
    return render_template("admin.html",events=events)

if __name__ == '__main__':
    app.run()
