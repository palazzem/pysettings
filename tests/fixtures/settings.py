from pysettings.base import BaseSettings
from pysettings.options import Option
from pysettings.validators import is_https_url

# Class definition
class TestSettings(BaseSettings):
    url = Option(validators=[is_https_url])
    description = Option()

# Use settings in your application
settings = TestSettings()
settings.url = "https://example.com"
settings.description = "A shiny Website!"
settings.is_valid()
