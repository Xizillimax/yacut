import re
from string import ascii_letters, digits

STRING = "".join((ascii_letters, digits))
MATCH = re.compile(r"^[A-Za-z0-9]{1,16}$")
