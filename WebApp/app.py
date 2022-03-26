from flask import Flask, request, render_template, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods= ['GET', 'POST'])
def lander():

    if request.form:
            
        if request.form.getlist('foox'):
                indexVal= request.form.getlist('foox')
                print(indexVal)
                send_file('receivedImages/WhatsApp Image 2022-03-19 at 7.39.54 PM.jpeg')

    return render_template("index.html")

@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
    global filePath
    print("Got request in static files")
    print(request.files)
    f = request.files['static_file']
    f.save('receivedImages/'+f.filename)

    filePath = 'receivedImages/'+f.filename

    resp = {"success": True, "response": "file saved!"}
    # return jsonify(resp), 200

    # x = pd.read_csv(filePath)
    # dates = x['Date'].values.tolist()
    # closed = x['Volume'].values.tolist()
    return render_template("index.html")


if __name__ == "__main__":
    app.run()