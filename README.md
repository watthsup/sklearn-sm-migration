# SKlearn to AWS Sagemaker Migration
This repository is created to be a guideline for migrating ML models that have been trained on SKlearn to serve as an endpoint for AWS Sagemaker. The ML task that we try to reproduce this time is Iris classification (Just want to keep it simple).
# Pre-requisite
- AWS Account
- ตัวกับใจ
- Shift+Enter keys :D
# How to run
1. Move all files to your sagemaker notebook workspace
2. Train Iris classification model (LR model) using **sklearn-iris.ipynb**
3. After finished step 2 you would get **model.joblib**. Btw, other format is valid e.g. pkl, pickle or any byte stream.
4. Deploy/Serve Iris classification service using AWS sagemaker **(migration-playground.ipynb)**. You can follow through my header to understrand what this block is trying to do. If you face any problem, feel free to contact me.

(Optional) To correctly validate the result from an endpoint. I suggest that you should explicitly split the Iris.csv into train.csv and test.csv.

(Optional) Maybe you could try with other weight format as you see fit. If it doesn't work, just let me know.
# Inference.py
- This one is the most important component that we have to learn about it. Here, we can write specific functions including model_fn, input_fn, predict_fn and output_fn to override the pre/post processing behaviour.

For more details, please refer to : https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_inferenece_script_mode.html

# Remark
- Currently, We support only Realtime and Serverless endpoint mode
- If you have any suggestion, feel free to raise it.
# What's next
- Catboost model is in progress. Hold on tight :D
