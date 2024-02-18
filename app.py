from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template('homepage.html')


@app.route("/predict")
def predict():
    return render_template('predictionpage.html')



if __name__ == '__main__':
    app.run(debug=True)