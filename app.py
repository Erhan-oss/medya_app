from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Maksimum 500 MB olarak ayarla
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi', 'm4a', 'mp3', 'wav', 'ogg', 'webm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return "Dosya seçilmedi", 400

    files = request.files.getlist('files')
    saved_files = 0

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Her yüklemede farklı isim vermek için
            unique_name = f"{int(os.times()[4]*1000)}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_name))
            saved_files += 1

    return f"{saved_files} dosya başarıyla yüklendi!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
