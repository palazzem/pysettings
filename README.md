# pysettings

[![CircleCI](https://circleci.com/gh/palazzem/pysettings/tree/master.svg?style=svg)](https://circleci.com/gh/palazzem/pysettings/tree/master)
[![codecov](https://codecov.io/gh/palazzem/pysettings/branch/master/graph/badge.svg)](https://codecov.io/gh/palazzem/pysettings)

Pysettings is a Python package to store your application settings. Compared to some
settings managers, this package has been inspired by [Django Rest Frameworks validators][1]
where you can validate the user input beforehand.

That simplifies your code because settings don't need to be validated in your application
logic. Available features are:
* Store your application settings without using global objects.
* Extend your settings using a `BaseSettings` class. The resulting class can be validated
  using a `settings.is_valid()` method.
* Fields are represented with an `Option` field that takes `validators` as parameter.
  It's possible to set a `default` value if the option is not set by users.
* Out of the box validators: `not_null`, `is_https_url`.
* It's possible to add custom validators as functions.

[1]: https://www.django-rest-framework.org/api-guide/validators/

## Requirements

* Python 3.5+

## Getting Started

`pysettings` is available on PyPI:

```bash
$ pip install pysettings-validator
```

### Create your Settings

```python
from pysettings.base import BaseSettings
from pysettings.options import Option
from pysettings.validators import is_https_url

# Class definition
class Settings(BaseSettings):
    url = Option(validators=[is_https_url])
    description = Option()

# Use settings in your application
settings = Settings()
settings.url = "https://example.com"
settings.description = "A shiny Website!"
settings.is_valid()  # returns (True, [])
```

### Settings API

`settings` instance doesn't allow to set attributes not defined as `Option`. If you
try to set a setting that is not defined, a `OptionNotAvailable` exception is raised:

```python
class Settings(BaseSettings):
    description = Option()

# Use settings in your application
settings = Settings()
settings.url = "https://example.com"  # raise `OptionNotAvailable`
```

`is_valid()` exposes a `raise_exception=True` kwarg in case you prefer to not raise
exceptions in your code:

```python
class Settings(BaseSettings):
    url = Option(validators=[is_https_url])

# Use settings in your application
settings = Settings()
settings.url = "http://example.com"
settings.is_valid()                       # raise ConfigNotValid exception
settings.is_valid(raise_exception=False)  # return (False, [{'url': [{'is_https_url': 'The schema must be HTTPS'}]}])
```

### Create a Custom Validator

```python
# app/validators.py
from pysettings.exceptions import ValidationError

def is_a_boolean(value):
    if isinstance(value, bool):
        return True
    else:
        raise ValidationError("The value must a Boolean")

# app/settings.py
from .validators import is_a_boolean

class Settings(BaseSettings):
    dry_run = Option(validators=[is_a_boolean])
    description = Option()

# app/main.py
settings = Settings()
settings.dry_run = "Yes"
settings.description = "Dry run mode!"
settings.is_valid()  # raises ConfigNotValid exception
```

## Development

We accept external contributions even though the project is mostly designed for personal
needs. If you think some parts can be exposed with a more generic interface, feel free
to open a GitHub issue and to discuss your suggestion.

### Coding Guidelines

We use [flake8][1] as a style guide enforcement. That said, we also use [black][2] to
reformat our code, keeping a well defined style even for quotes, multi-lines blocks and other.
Before submitting your code, be sure to launch `black` to reformat your PR.

[1]: https://pypi.org/project/flake8/
[2]: https://github.com/ambv/black

### Testing

`tox` is used to execute the following test matrix:
* `lint`: launches `flake8` and `black --check` to be sure the code honors our style guideline
* `py{35,36,37,38}`: launches `py.test` to execute all tests under Python 3.5, 3.6 and 3.7.

To launch the full test matrix, just:

```bash
$ tox
```
