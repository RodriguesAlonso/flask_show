from flask  import Blueprint, render_template, request

bp = Blueprint("site", __name__)

@bp.route("/hello")
def hello():
    return "Hello"

@bp.route("/")
def index2():
    return render_template(
        "index.html",
         name=request.args['name'])