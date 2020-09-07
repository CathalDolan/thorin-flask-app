import os
import json
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")  # Route to the page clicked. Fn below is bound to it. AKA a "view"
def index():  # Clicking a link to a page calls the function
    # return "<h1>Hello,</h1> <h2>World</h2>"    HTML can be added directly to the code
    return render_template("index.html") # Renders the html from index.html file


@app.route("/about")
def about(): # FN can be called anything but it's good convention to use page name
    data = []
    # Opens the json file in read only. "json_data" is arbitrary name
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # return "<h1>" + member["name"] + "</h1>"
    return render_template("member.html", member=member)


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("Hello") # SHows up in the terminal and proves successful submission
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__": # Indicates whether a fn runs directly or is an import
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # not sure why this and line below are required
        port=int(os.environ.get("PORT", "5000")),
        debug=True # Only True in dev mode. False for production
        )

