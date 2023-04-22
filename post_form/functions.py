from flask import Blueprint, render_template, request


UPLOAD_FOLDER = "uploads/images"

loader_blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    template_folder='templates')


@loader_blueprint.route("/post_form")
def send_post():
    return render_template('post_form.html')

