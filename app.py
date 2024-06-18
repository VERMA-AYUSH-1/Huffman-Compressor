
import os
from flask import Flask, render_template, request, send_file, session
from werkzeug.utils import secure_filename
from huffman_compressor import huffman_compress
from huffman_decompressor import huffman_decompress

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Update this line to your preferred path
app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "uploads")
app.config["DOWNLOAD_FOLDER"] = os.path.join(os.getcwd(), "downloads")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/compress", methods=["GET", "POST"])
def compress():
    if request.method == "GET":
        return render_template("compress.html", check=0)
    else:
        up_file = request.files["file"]

        if up_file.filename:
            filename = secure_filename(up_file.filename)
            input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            output_path = os.path.join(app.config["DOWNLOAD_FOLDER"], f"{filename}-compressed.bin")
            
            up_file.save(input_path)
            huffman_compress(input_path, output_path)
            
            session['filename'] = f"{filename}-compressed.bin"
            session['ftype'] = "-compressed.bin"

            return render_template("compress.html", check=1)
        else:
            print("ERROR")
            return render_template("compress.html", check=-1)

@app.route("/decompress", methods=["GET", "POST"])
def decompress():
    if request.method == "GET":
        return render_template("decompress.html", check=0)
    else:
        up_file = request.files["file"]

        if up_file.filename:
            filename = secure_filename(up_file.filename)
            input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            up_file.save(input_path)
            
            huffman_decompress(input_path.encode('utf-8'))
            
            session['filename'] = f"{filename.decode('utf-8')}-decompressed"
            
            return render_template("decompress.html", check=1)
        else:
            print("ERROR")
            return render_template("decompress.html", check=-1)

@app.route("/download")
def download_file():
    filename = session.get('filename')
    ftype = session.get('ftype')

    if filename and ftype:
        path = os.path.join(app.config["DOWNLOAD_FOLDER"], filename)
        return send_file(path, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)


