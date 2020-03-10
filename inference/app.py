from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import pickle 
import json


app = Flask(__name__)
@app.route("/predict", methods = ["GET", "POST"])
def get_predictions():
    input_json_ = json.loads(request.data)
    features_df = pd.DataFrame(input_json_)
    predicted_prob = dt.predict_proba(features_df)
    predicted_class = np.argmax(predicted_prob, axis = 1)
    return jsonify({"predictions" : str(list(predicted_class))})

if __name__ == "__main__":
    # READ MODEL 
    with open("src/model.pkl" , "rb") as f:
        dt = pickle.load(f)
    
    app.run(port=5000, host = '0.0.0.0', debug=True)