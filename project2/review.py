
try:
    # when running `python app.py` the main module is named '__main__'
    # import the app object from __main__ so routes register on the running app
    from __main__ import app
except ImportError:
    # fallback to importing the app module (used when the module is imported as a package)
    from app import app
from flask import render_template, request, redirect

#reviewsでデータをリストで管理する
reviews =[]

@app.route("/")
def review_index():
    return render_template("index.html",reviews = reviews)

# methodsでかく
@app.route("/add", methods = ["POST"])
def add_review():
    content = request.form.get("content")
    reviews.append(content)
    return redirect("/")