import csv, os, string, uuid, json
import urllib.request
from app import app
import json
from flask import Flask, request, redirect, jsonify, send_file, render_template, make_response, Response
from werkzeug.utils import secure_filename
from flask import abort, send_from_directory

api = Flask(__name__)

UPLOAD_DIRECTORY = 'D:/uploads'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


with open('detail.csv', 'w', newline='') as outcsv:
    writer = csv.DictWriter(outcsv, fieldnames=["id", "filename"])
    writer.writeheader()
    outcsv.close()


@app.route('/files', methods=['PUT'])
def upload_file():
    file = request.files['file']
    flag = 0
    if file:
        filename = file.filename
        with open('detail.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == filename:
                    flag = 1
                    f.close()
                    break
        if flag == 0:
            k = uuid.uuid1()
            k=k.int
            with open('detail.csv', 'a', newline='') as f:
                write = csv.writer(f)
                write.writerow([k, filename])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify(filename)
            resp.status_code = 200
            f.close()
            return Response(filename, status=200)
        else:
            return Response('File Already Exists', status=409)


@app.route("/files/list", methods=['GET'])
def list_files():
    files = []
    with open('detail.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            a = {
                "file_name": row[1],
                "id":row[1]
            }
            files.append(a)
    return jsonify(files)

@app.route("/files/<path:path>", methods=["DELETE"])
def del_file(path):
    flag = '1'
    with open('detail.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] == path:
                flag = '0'
                f.close()
                break
    if flag == '1':
        res = "requested object "+path+" is not found"
        return Response(res, status=404)
    else:
        lines = list()
        with open('detail.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == path:
                        lines.remove(row)

        with open('detail.csv', 'w', newline='') as writeFile:
            write = csv.writer(writeFile)
            write.writerows(lines)
        os.remove(os.path.join(UPLOAD_DIRECTORY, path))
        res = "object "+path+" deleted successfully"
        return Response(res, status=200)


@app.route("/files/<path:p>", methods=["GET"])
def download_file(p):
    if os.path.exists(os.path.join(UPLOAD_DIRECTORY, p)):
        p = os.path.join(UPLOAD_DIRECTORY, p)
        return send_file(p, as_attachment=True)
    res="requested object "+p+" is not found"
    return Response(res, status=404)

app.run(debug = True)
