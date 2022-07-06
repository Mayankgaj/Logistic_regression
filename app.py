import pickle, bz2
from flask import Flask, request, render_template
import numpy as np
from logger import log
import data_convert

app = Flask(__name__)

# Import Regression model file
log.debug("Loading Model")
pickle_in = bz2.BZ2File('logistic_regression.pkl', 'rb')
model_R = pickle.load(pickle_in)
log.debug("Successfully Model Loaded")


@app.route('/')
def home():
    log.debug('Home page loaded successfully')
    return render_template('Women_Affairs.html')


@app.route("/predict", methods=['POST'])
def predict():
    try:
        for x in request.form.values():
            if type(x) == str() or x == "":
                log.error('Input is Empty')
                return render_template('Women_Affairs.html', prediction_text1="Check the Input again!!!")
            elif len([x for x in request.form.values()]) < 8:
                log.error(f"Given input is {len([float(x) for x in request.form.values()])} ,Expecting 8 values")
                return render_template('Women_Affairs.html', prediction_text1="Check the Input again!!!")
            else:
                data = [float(x) for x in request.form.values()]
                log.debug("Spliting Categorical Columns")
                final_data = data_convert.data_convert(data)
                log.debug("Resizing data into 2D array")
                final_features = [np.array(final_data)]
                log.info(final_features)
                log.debug("Data in proper Shape ")
                output = model_R.predict(final_features)
                log.debug('Prediction done for Regression model')
                return render_template('Women_Affairs.html', prediction_text1="{}".format(output))
    except Exception as e:
        log.error('Input error, check input', e)
        return render_template('Women_Affairs.html', prediction_text1="Check the Input again!!!")


# Run APP in Debug mode
if __name__ == "__main__":
    app.run(debug=True)