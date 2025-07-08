from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
    return('Welcome to cc3')
if __name__=="__main__":
    app.run(debug=True) 
