import os

from flask import Flask, flash, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = { 'jpg', 'jpeg'}
app = Flask(__name__)

app.config['UPLOAD_FOLDER']='C:/Users/pavania/Desktop/pavani-flask training/flask task5 pavani'
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        if 'the_file' not in request.files:
            flash('not selected!')
            return redirect(url_for('upload_file'))
        elif file.filename == '':
            return ("<script>alert('file not found!')</script>")
        elif file:
            file_name = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file_name))

            flash('successfully!')
            return redirect(url_for('upload_file'))
        else:
            flash('Invalid file type!')
            return redirect(request.url)
    return render_template('files.html')

if __name__ == '__main__':

    app.run(debug=True)