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
    return "Hello from Flask"