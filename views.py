from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Response
import random
import numpy as np
import cv2

views = Blueprint(__name__, "views")

@views.route('/') # return html
def home():
    return render_template('index.html', name = "Tim", age= 20)

@views.route('/objects3d', methods=["GET"])
def generate_objects(num_objects=1):
    objects = []
    for _ in range(num_objects):
        shape = np.random.choice(["sphere", "cube"])
        size = np.random.uniform(0.1, 1.0)
        x = np.random.uniform(-1.0, 1.0)
        y = np.random.uniform(-1.0, 1.0)
        z = np.random.uniform(-1.0, 1.0)
        color = np.random.rand(3) * 255
        obj = {
            "shape": shape,
            "size": size,
            "x": x,
            "y": y,
            "z": z,
            "color": color.tolist()
        }
        objects.append(obj)
    return jsonify(objects)
