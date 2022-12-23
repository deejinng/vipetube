from pytube import YouTube
from flask import Flask, session, url_for, send_file, render_template, redirect, request
from io import BytesIO


app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"
 

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST":
        session["link"] = request.form.get("url")
        url = YouTube(session["link"])
        url.check_availability()
        return render_template("download.html", url=url)

    return render_template('index.html')
 
 
@app.route("/download",methods=["POST","GET"])
def download():
    if request.method == "POST":
        buffer = BytesIO()
        itag = request.form.get("itag")
        url = YouTube(session["link"])
        video = url.streams.get_by_itag(itag)
        
        #Buffer comes in
        video.stream_to_buffer(buffer)
        buffer.seek(0)
               
        return send_file(buffer, as_attachment=True, download_name=video.title, mimetype=video.mime_type)
        
    return redirect("/index")
     
if __name__ == '__main__':
    app.run(debug=True)
    # Happy Coding :-)
    

# A silly random project 
# [Afolabi David] - ©2021