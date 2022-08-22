from flask import Flask


app=Flask(__name__)
@app.route('/')
def welcome():
    return "hello pavani welcome to MT"

if __name__=='__main__':
    app.run(debug=True,port =4000,host='127.0.0.1')