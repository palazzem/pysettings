from pysettings.base import BaseSettings
from pysettings.options import Option
from pysettings.validators import is_https_url


# Class definition
class TestValidSettings(BaseSettings):
    url = Option(default="https://example.com", validators=[is_https_url])
    description = Option(default="A shiny Website!")
