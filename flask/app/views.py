from app import app
import os
from flask import Flask, request
import numpy as np
import joblib
from flasgger import Swagger

classifier = joblib.load('./app/model.pkl')

def senior_simplifier(title):
    if title == "Senior":
        return 1
    else:
        return 2
    
def job_type_simplifier(role):
    if role == "data scientist":
        return 3
    elif role == "data engineer":
        return 2
    elif role == "analyst":
        return 1
    elif role == "director":
        return 4
    elif role == "manager":
        return 5
    elif role == "mle":
        return 6
    elif role == "na":
        return 7
    elif role == "research":
        return 8
    elif role == "sw":
        return 9
    
@app.route("/")
def index():
    """Glassdoor Job Salary Predictor.
    
    ---
    parameters:
        - name: rating
          in: query
          type: number
          enum: [1, 2, 3, 4, 5]
          required: true
          default: 3
        - name: jobhq
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: age
          in: query
          type: number
          required: true
          default: 5
        - name: num_comp
          in: query
          type: number
          required: true
          default: 5
        - name: python
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: r
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: aws
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: spark
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: hadoop
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: docker
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: sql
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: linux
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: flask
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: django
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: tensorflow
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: keras
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: pytorch
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: tableau
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: algo
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: stats
          in: query
          type: number
          enum: [0, 1]
          required: true
          default: 0
        - name: job_type
          in: query
          type: string
          enum: ["analyst", "data engineer", "data scientist", "director", "manager", "mle", "na", "research", "sw"]
          required: true
          default: data scientist
        - name: seniority
          in: query
          type: string
          enum: ["Senior", "Junior"]
          required: true
          default: Junior
        - name: len_desc
          in: query
          type: number
          required: true
          default: 250
    responses:
        200:
            description: The output values
          
    """

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        rating = request.args.get('rating')
        jobhq = request.args.get('jobhq')
        age = request.args.get('age')
        num_comp = request.args.get('num_comp')
        python = request.args.get('python')
        r = request.args.get('r')
        aws = request.args.get('aws')
        spark = request.args.get('spark')
        hadoop = request.args.get('hadoop')
        docker = request.args.get('docker')
        sql = request.args.get('sql')
        linux = request.args.get('linux')
        flask = request.args.get('flask')
        django = request.args.get('django')
        tensorflow = request.args.get('tensorflow')
        keras = request.args.get('keras')
        pytorch = request.args.get('pytorch')
        tableau = request.args.get('tableau')
        algo = request.args.get('algo')
        stats = request.args.get('stats')
        job_type = job_type_simplifier(request.args.get('job_type'))
        seniority = senior_simplifier(request.args.get('seniority'))
        len_desc = request.args.get('len_desc')
        
        features = [rating, jobhq,  age, num_comp,  python, r, aws, spark, hadoop,
                docker, sql, linux, flask, django, tensorflow, keras,
                pytorch, tableau, algo, stats, job_type, seniority, len_desc]
        final_features = np.array(features).reshape(1, -1)
        
        print(final_features)
    
        prediction = classifier.predict(final_features)
        return 'The predicted value is: '  + str(prediction) 
    
    return "Hello from Flask"