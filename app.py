from flask import Flask, render_template, url_for, request
import chatbot_model


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = chatbot_model.run_model(output["name"])
    index = name.find('Question');
    ind = slice(index)
    return name[ind]
    # return render_template('index.html', name = name)
    

if __name__ == "__main__":
    app.run(debug=True, port = 5000)