# import os
# import time
# import glob
# from flask import Flask, redirect, render_template, request, send_file

# app = Flask(__name__)

# global filename
# global ftype

# @app.route("/")
# def home():
#     # Delete old files
#     # filelist = glob.glob('uploads/*')
#     # for f in filelist:
#     #     os.remove(f)
#     # filelist = glob.glob('downloads/*')
#     # for f in filelist:
#     #     os.remove(f)
#     return render_template("home.html")

# # Update this line to your Windows path
# app.config["FILE_UPLOADS"] = "D:\\Python programs\\Huffman Compressor\\uploads"
# # app.config["FILE_UPLOADS"] = "C:\\Users\\verma\\Downloads"

# @app.route("/compress", methods=["GET", "POST"])
# def compress():
#     if request.method == "GET":
#         return render_template("compress.html", check=0)
#     else:
#         up_file = request.files["file"]

#         if len(up_file.filename) > 0:
#             global filename
#             global ftype
#             filename = up_file.filename
#             print(up_file.filename)
#             up_file.save(os.path.join(app.config["FILE_UPLOADS"], filename))
#             os.system(f'python huffman_compress.py {os.path.join(app.config["FILE_UPLOADS"], filename)}')
#             filename = filename[:filename.index(".", 1)]
#             ftype = "-compressed.bin"
#             while True:
#                 if f'uploads/{filename}-compressed.bin' in glob.glob('uploads/*-compressed.bin'):
#                     os.system(f'move uploads\\{filename}-compressed.bin downloads\\')
#                     break

#             return render_template("compress.html", check=1)
#         else:
#             print("ERROR")
#             return render_template("compress.html", check=-1)

# @app.route("/decompress", methods=["GET", "POST"])
# def decompress():
#     if request.method == "GET":
#         return render_template("decompress.html", check=0)
#     else:
#         up_file = request.files["file"]

#         if len(up_file.filename) > 0:
#             global filename
#             global ftype
#             filename = up_file.filename
#             print(up_file.filename)
#             up_file.save(os.path.join(app.config["FILE_UPLOADS"], filename))
#             os.system(f'python huffman_decompress.py {os.path.join(app.config["FILE_UPLOADS"], filename)}')
#             with open(f'uploads\\{filename}', 'rb') as f:
#                 ftype = "-decompressed." + (f.read(int(f.read(1)))).decode("utf-8")
#             filename = filename[:filename.index("-", 1)]

#             while True:
#                 if f'uploads\\{filename}{ftype}' in glob.glob('uploads\\*-decompressed.*'):
#                     os.system(f'move uploads\\{filename}{ftype} downloads\\')
#                     break

#             return render_template("decompress.html", check=1)
#         else:
#             print("ERROR")
#             return render_template("decompress.html", check=-1)

# @app.route("/download")
# def download_file():
#     global filename
#     global ftype
#     path = "downloads\\" + filename + ftype
#     return send_file(path, as_attachment=True)

# if __name__ == "__main__":
#     app.run(debug=True)



# import os
# import glob
# from flask import Flask, redirect, render_template, request, send_file, session
# from werkzeug.utils import secure_filename
# from huffman_compressor import huffman_compress
# from huffman_decompressor import huffman_decompress  # Import your decompression function

# app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# # Update this line to your Windows path
# app.config["FILE_UPLOADS"] = "D:\\Python programs\\Huffman Compressor\\uploads"

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/compress", methods=["GET", "POST"])
# def compress():
#     if request.method == "GET":
#         return render_template("compress.html", check=0)
#     else:
#         up_file = request.files["file"]

#         if up_file.filename:
#             filename = secure_filename(up_file.filename)
#             up_file.save(os.path.join(app.config["FILE_UPLOADS"], filename))
            
#             input_path = os.path.join(app.config["FILE_UPLOADS"], filename)
#             output_path = os.path.join(app.config["FILE_UPLOADS"], f"{filename}-compressed.bin")
            
#             huffman_compress(input_path, output_path)
            
#             session['filename'] = f"{filename}-compressed.bin"
#             session['ftype'] = "-compressed.bin"

#             return render_template("compress.html", check=1)
#         else:
#             print("ERROR")
#             return render_template("compress.html", check=-1)

# @app.route("/decompress", methods=["GET", "POST"])
# def decompress():
#     if request.method == "GET":
#         return render_template("decompress.html", check=0)
#     else:
#         up_file = request.files["file"]

#         if up_file.filename:
#             filename = secure_filename(up_file.filename)
#             up_file.save(os.path.join(app.config["FILE_UPLOADS"], filename))
            
#             input_path = os.path.join(app.config["FILE_UPLOADS"], filename)
#             huffman_decompress(input_path)
            
#             session['filename'] = f"{filename}-decompressed"
            
#             return render_template("decompress.html", check=1)
#         else:
#             print("ERROR")
#             return render_template("decompress.html", check=-1)

# @app.route("/download")
# def download_file():
#     filename = session.get('filename')
#     ftype = session.get('ftype')

#     if filename and ftype:
#         path = os.path.join(app.config["FILE_UPLOADS"], filename)
#         return send_file(path, as_attachment=True)
#     else:
#         return "File not found", 404

# if __name__ == "__main__":
#     app.run(debug=True)


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


