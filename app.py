from flask import Flask, render_template, request,send_file,send_from_directory, Response
from merger import main
from time import time
from os import makedirs,mkdir
app = Flask(__name__)


UPLOAD_DIR = "/temp/uploads/"

app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/", methods=['GET','POST'])
def index():
  return render_template("index.html")



@app.route("/merge",methods=['POST'])
def mergeFiles():
  upload_timestamp = int(time()) 
    
  # create dir 

  upload_path = f"{UPLOAD_DIR}/{upload_timestamp}/"
  makedirs(upload_path)
  
  files = request.files.getlist("file")   
  uploaded_files = []
  
  for file in files: 
    file_name = file.filename.replace(" ", "_")
    file_path = f"{UPLOAD_DIR}/{upload_timestamp}/{file_name}"
    file.save(file_path)
    uploaded_files.append(file_path) 
      # run merger
  
  main(uploaded_files, f"{upload_path}/output.html")
  file = send_file(f"{upload_path}/output.html")
  return file