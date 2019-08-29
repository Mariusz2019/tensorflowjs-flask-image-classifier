from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np


# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    # Main page
    result = "TEST"
    return result



if __name__ == '__main__':
    app.run(port=5002, debug=True)

    # Serve the app with gevent
    #http_server = WSGIServer(('0.0.0.0', 5000), app)
    #http_server.serve_forever()
