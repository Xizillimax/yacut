from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional, Regexp

MIN_LENGHT_CUSTOM_ID = 1
MAX_LENGHT_CUSTOM_ID = 16


class ShortURLForm(FlaskForm):
    original_link = URLField(
        "Вставьте URL",
        validators=(
            DataRequired(message="Обязательное поле"),
            URL(require_tld=True, message="Некорректная ссылка")
        )
    )
    custom_id = StringField(
        validators=(
            Length(MIN_LENGHT_CUSTOM_ID, MAX_LENGHT_CUSTOM_ID),
            Regexp(
                regex=r"[A-Za-z0-9]+",
                message="В сокращенние присутствуют недопустимые символы"
            ),
            Optional()
        )
    )
    submit = SubmitField("Создать")
