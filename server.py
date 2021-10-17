import re
from flask import Flask,request,flash
from flask.json.tag import PassDict
from flask.templating import render_template
import requests

app = Flask(__name__)
base_url = "https://api.github.com/users/"
@app.route("/",methods=["GET","POST"]) # inddex.htmlimize hem get hem post request olabilir get request olduğu zaman index.html i göstericez post request te ise github users a get request atıp oradaki bilgidleri alacağız
def index():
    if request.method == "POST":
        githubname = request.form.get("githubname")
        response_user = requests.get(base_url + githubname) #kullanıcı adına göre githubdaki usersın response verisini 
        response_repos = requests.get(base_url + githubname + "/repos")
        user_info = response_user.json() #dönen response'u json verisine çevirdik
        repos = response_repos.json()
        if "message" in user_info:
            return render_template("index.html",error = "Kullanıcı adı bulunamadı")
        else:
            return render_template("index.html",profile = user_info,repos = repos) #github api işlemlerinden sonra gerekli verileri aldık ve index.html render edip aldığımız veriyi index.html e profile olarak gönderdik.
        
    else:
        return render_template("index.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)