from flask import Blueprint, render_template, request
from functions import check_format_file, download_to_json
from logger import *


UPLOAD_FOLDER = "uploads/images"

post_uploaded_blueprint = Blueprint(
    'post_uploaded_blueprint',
    __name__,
    template_folder='templates')


@post_uploaded_blueprint.route("/post_uploaded", methods=["POST"])
def send_post():
    picture = request.files.get('picture')
    content = request.form.get('content')
    filename = picture.filename

    url_for_download = f"./{UPLOAD_FOLDER}/{filename}"

    if content and picture:
        if check_format_file(filename):
            picture.save(url_for_download)
            download_to_json(url_for_download, content)
            return render_template('post_uploaded.html', picture=picture, content=content, filename=filename)
        else:
            new_logger.error("Incorrect format file or content does not exist")
            return render_template('file_not_image.html')