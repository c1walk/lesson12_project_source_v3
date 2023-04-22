from flask import request, render_template, Blueprint
from functions import loader_from_json

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route("/search")
def search_page():
    search_by = request.args.get("s")
    if search_by != "":
        posts = loader_from_json(search_by)
        return render_template('post_list.html', search_by=search_by, posts=posts)
    else:
        return render_template('./index.html')

