import json
import os
import vertexai
from flask import Flask, request, render_template
from vertexai.language_models import TextGenerationModel

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "GET":
        return 200

    if request.method == "POST":
        data = request.get_json()
        prompt = data["prompt"]

        vertexai.init(project="gbot-test-062", location="us-central1")

        parameters = {
            "temperature": 0.2,
            "max_output_tokens": 256,
            "top_p": 0.8,
            "top_k": 40,
        }
        model = TextGenerationModel.from_pretrained("text-bison@001")
        response = model.predict("Please answer the following question or comment in two sentences or less. Be concise: " + prompt, **parameters)

        result = {"content": response.text}
        return json.dumps(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
