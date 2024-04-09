from flask import flash, render_template, redirect, url_for

from . import app, db
from .forms import ShortURLForm
from .models import URLMap
from .utils import get_unique_short_id, check_original


MESSAGE_ERROR = "Предложенный вариант короткой ссылки уже существует."


@app.route('/', methods=("GET", "POST"))
def generate_url_page():
    form = ShortURLForm()
    if form.validate_on_submit():
        url = form.custom_id.data
        if not url or not len(url) or url is None:
            url = get_unique_short_id()
        if check_original(url):
            flash(MESSAGE_ERROR, "fail")
        else:
            short_url = URLMap(
                original=form.original_link.data,
                short=url
            )
            db.session.add(short_url)
            db.session.commit()
            flash(url_for("short_url", short=url, _external=True), "link")
    return render_template('index.html', form=form)


@app.route('/<string:short>', methods=("GET",))
def short_url(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
