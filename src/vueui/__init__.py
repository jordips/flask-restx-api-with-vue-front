from flask import Blueprint, render_template

vue_bp = Blueprint("vue_bp", __name__, # 'Client Blueprint'
    template_folder="templates", # Required for our purposes
    static_folder="static", # Again, this is required
    static_url_path="/vueui/static" # Flask will be confused if you don't do this
)

@vue_bp.route("/")
def index():
    return render_template("index.html")