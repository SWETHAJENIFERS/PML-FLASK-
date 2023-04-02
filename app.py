from flask import Flask, render_template, request
import joblib

# load model
model = joblib.load('model1.pkl')

# initialize Flask app
app = Flask(__name__)

# define home page route
@app.route('/')
def home():
    return render_template('home.html')

# define prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # get input data from HTML form
    km_driven = float(request.form['km_driven'])
    # make prediction
    prediction = model.predict([[km_driven]])[0]
    # return predicted price as HTML
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
