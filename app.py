from flask import Flask

# Импорт блюпринотов
from main_page.main_page import main_blueprint
from post_form.functions import loader_blueprint
from search.functions import search_blueprint
from post_uploaded.post_uploaded import post_uploaded_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Поддержка кириллицы
app.config['JSON_AS_ASCII'] = False

# Регистрация блюпринта
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(post_uploaded_blueprint)


if __name__ == "__main__":
    app.run()
