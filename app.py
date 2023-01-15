import dotenv
from cohere_wrapper import CohereWrapper
import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
c_api = CohereWrapper(os.environ["API_KEY"])

@app.route("/analyze", methods=["POST"])
def analyze():
    d = request.get_json(force=True)
    res = c_api.analyze_text(d["text"])
    return res[0].prediction