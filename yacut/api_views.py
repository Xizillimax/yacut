from flask import jsonify, request

from . import app, db
from .constants import MATCH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id, check_original


MESSAGE_NOT_ID = "Указанный id не найден"
MESSAGE_NOT_DATA = "Отсутствует тело запроса"
MESSAGE_NOT_URL = '"url" является обязательным полем!'
MESSAGE_NOT_CURRECT_SHORT = "Указано недопустимое имя для короткой ссылки"
MESSAGE_ERROR = "Предложенный вариант короткой ссылки уже существует."


@app.route("/api/id/<string:short_id>/", methods=("GET",))
def get_link(short_id):
    target = check_original(short_id)
    if not target:
        raise InvalidAPIUsage(MESSAGE_NOT_ID, 404)
    return jsonify({"url": target}), 200


@app.route("/api/id/", methods=("POST",))
def push_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(MESSAGE_NOT_DATA)
    elif "url" not in data:
        raise InvalidAPIUsage(MESSAGE_NOT_URL)
    elif not data.get("custom_id"):
        data.update({"custom_id": get_unique_short_id()})
    elif not MATCH.search(data["custom_id"]):
        raise InvalidAPIUsage(MESSAGE_NOT_CURRECT_SHORT)
    elif URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(MESSAGE_ERROR)
    short = URLMap()
    short.from_dict(data)
    db.session.add(short)
    db.session.commit()
    return jsonify(short.to_dict()), 201
