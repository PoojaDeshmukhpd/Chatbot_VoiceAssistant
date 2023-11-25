from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from chat import calling_bot, wishMe, talk, engine
from voice_assistant import take_command,speak
import execjs
# choose a JavaScript runtime
runtime = execjs.get('Node')
# choose a JavaScript runtime

app = Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.route("/developers")
def developers():
    return render_template("developers.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response= calling_bot(text)
    javascript_code = """
    var message = 'Hello from JavaScript';
    console.log(message);
    """
    output = runtime.exec_(javascript_code)

    message = {"answer": response}
    # talk(response)
    return jsonify(message)

@app.get("/voice")
def voice():
    speak("hello pooja deshmukh")
    result = "Pooja Deshmukh" # replace this with your actual Python function
    return jsonify(result=result)

    # text = request.get_json().get("message")
    # response = calling_bot(text)
    # message = {"answer": response}
    # # talk(response)
    # return jsonify(message)

@app.get("/stud")
def stud_login():
    return render_template("stud_login.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0)
    # app.run(debug=True)
    # wishMe()
