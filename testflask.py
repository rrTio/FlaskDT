from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
<meta http-equiv="refresh" content="1" /> 
The current time is {}.""".format(datetime.strftime(datetime.now(), "%d %B %Y %X"))

if __name__ == "__main__":
    app.run()