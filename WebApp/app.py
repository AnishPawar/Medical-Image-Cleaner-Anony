from os import mkdir
from flask import Flask, request, render_template, jsonify, send_file
from flask_cors import CORS
import datetime,time
from anonymize import OCR,fuzzy_matching,NLP,batchAnonymize

app = Flask(__name__)
CORS(app)

final_coor = []
temp_list = []
new_text = []
image = []




@app.route('/', methods= ['GET', 'POST'])
def lander():

    if request.form:
            
        if request.form.getlist('foox'):
                indexVal= request.form.getlist('foox')
                print(indexVal)
                # send_file('receivedImages/WhatsApp Image 2022-03-19 at 7.39.54 PM.jpeg')

    return render_template("index.html",path = '')

@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
    global filePath
    print("Got request in static files")
    print(request.files)
    f = request.files['static_file']
    x = datetime.datetime.now()
    mkdir(f'static/receivedImages/{x}')

    # mkdir()

    f.save(f'static/receivedImages/{x}/'+f.filename)

    # print("OK")
    path = batchAnonymize(f'static/receivedImages/{x}',ocr)
    print("OK1")
    print(path)
    
    resp = {"success": True, "response": "file saved!"}
    # return jsonify(resp), 200

    # x = pd.read_csv(filePath)
    # dates = x['Date'].values.tolist()
    # closed = x['Volume'].values.tolist()
    return render_template("index.html",path = path)


if __name__ == "__main__":
    ocr = OCR()
    app.run()