from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def first_page():
#     return "<p>This is first page</p>"

@app.route("/")
def user_login():
    return render_template("user_login.html")
    # return "<p>This is user login page</p>"

@app.route("/")
def admin_login():
    return render_template("admin_login.html")
    # return "<p>This is admin login page</p>"

if __name__ == "__main__":
    app.run(debug=True)

