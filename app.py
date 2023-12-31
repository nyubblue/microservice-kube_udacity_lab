"""
This module serves as the main Flask application for the machine learning microservice API.
It provides endpoints to make predictions about housing prices in Boston using a pre-trained model.

Author: Your Name
Date: Today's Date
"""
import logging
from flask import Flask, request, jsonify
from flask.logging import create_logger

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

APP = Flask(__name__)
LOG = create_logger(APP)
LOG.setLevel(logging.INFO)


def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: \n{payload}")
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict


@APP.route("/")
def home():
    """
    Home page
    """
    html = f"<h3>Sklearn Prediction Home</h3>"
    return html.format(format)


@APP.route("/predict", methods=["POST"])
def predict():
    """Performs an sklearn prediction

    input looks like:
    {
    "CHAS":{
    "0":0
    },
    "RM":{
    "0":6.575
    },
    "TAX":{
    "0":296.0
    },
    "PTRATIO":{
    "0":15.3
    },
    "B":{
    "0":396.9
    },
    "LSTAT":{
    "0":4.98
    }

    result looks like:
    { "prediction": [ <val> ] }

    """

    # Logging the input payload
    json_payload = request.json
    LOG.info("JSON payload: \n%s", json_payload)
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("Inference payload DataFrame: \n%s", inference_payload)
    # scale the input
    scaled_payload = scale(inference_payload)
    # get an output prediction from the pretrained model, clf
    prediction = list(CLF.predict(scaled_payload))
    LOG.info("Output Prediction: \n%s", prediction)
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    # load pretrained model as clf
    CLF = joblib.load("./model_data/boston_housing_prediction.joblib")
    APP.run(host="0.0.0.0", port=80, debug=True)  # specify port=80
