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

# Akshat 
if __name__ == "__main__":
    app.run()


@app.route('/uploads/<filename>')
def upload(filename):
    return send_file(app.config['UPLOAD_PATH'], filename)

@app.route('/uploads/<filename>')
def upload(filename):
    return send_file(app.config['UPLOAD_PATH'], filename)

# import imghdr
# import os
# from flask import Flask, render_template, request, redirect, url_for, abort, \
#     send_from_directory
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
# app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
# app.config['UPLOAD_PATH'] = 'uploads'

# def validate_image(stream):
#     header = stream.read(512)  # 512 bytes should be enough for a header check
#     stream.seek(0)  # reset stream pointer
#     format = imghdr.what(None, header)
#     if not format:
#         return None
#     return '.' + (format if format != 'jpeg' else 'jpg')

# @app.route('/')
# def index():
#     files = os.listdir(app.config['UPLOAD_PATH'])
#     return render_template('index.html', files=files)

# @app.route('/', methods=['POST'])
# def upload_files():
#     uploaded_file = request.files['file']
#     filename = secure_filename(uploaded_file.filename)
#     if filename != '':
#         file_ext = os.path.splitext(filename)[1]
#         if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
#                 file_ext != validate_image(uploaded_file.stream):
#             abort(400)
#         uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
#     return redirect(url_for('index'))

# @app.route('/uploads/<filename>')
# def upload(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)