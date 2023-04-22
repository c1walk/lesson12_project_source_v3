from flask import send_from_directory
from flask import Blueprint, render_template

main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/uploads/<path:path>')
def send_image_from_uploads(path):
    return send_from_directory("uploads", path)
