from random import choices

from .constants import STRING
from .models import URLMap


NUMBER_OF_RANDOM_ELEMENTS = 6


def get_unique_short_id():
    while True:
        short_url = "".join(
            choices(population=STRING, k=NUMBER_OF_RANDOM_ELEMENTS))
        if not check_original(short_url):
            return short_url


def check_original(target):
    if URLMap.query.filter_by(short=target).first():
        return URLMap.query.filter_by(short=target).first().original
