from app import app
from flask import render_template


@app.route("/api/docs/")
def docs():
    return render_template("docs.html")