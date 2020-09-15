from flask import current_app
import os
import secrets

def save_file(form_file):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_file.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/files', picture_fn)
    form_file.save(picture_path)
    return picture_fn



