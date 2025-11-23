from flask import Flask, render_template, request, redirect

app = Flask(__name__)

appPosts = []

# top page
@app.route("/")
def index():
    return render_template("index.html", posts= appPosts)

# add page
@app.route("/add", methods=["POST"])
def add():
    content = request.form.get("content")
    # contentをpostsリストに追加する
    appPosts.append(content) 
    return redirect("/")

if __name__ == "__main__":
    app.run(debug= True)
    
