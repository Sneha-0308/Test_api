import json
from flask import Flask,jsonify,request,Response
from googletrans import Translator
import ngrok
from flask_ngrok import run_with_ngrok
app = Flask(__name__)

run_with_ngrok(app)

translator = Translator()


@app.route("/translate", methods=['GET','POST'])
def translateKN():
    # if request.method=='POST':
    content = request.get_json()
    value=content.get('content')
    result=translator.translate(value, src='en', dest='kn')
    result=result.text
        # result.text 
    return result
        # return Response(json.dumps(result))
        

if __name__ == "__main__":
    app.run()


