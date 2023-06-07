import json
import requests
import joblib
import os
import numpy as np

def input_fn(request_body, request_content_type):
    if request_content_type == 'application/json':
        request_body = json.loads(request_body)
        inpVar = request_body['Input']
        inpVar = np.array(inpVar).reshape(1,-1)
        return inpVar
    else:
        raise ValueError("This model only supports application/json input")
        
def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model

def predict_fn(input_data, model):
    return model.predict(input_data)

def output_fn(prediction, content_type):
    res = prediction[0]
    respJSON = {'Output': res}
    return respJSON