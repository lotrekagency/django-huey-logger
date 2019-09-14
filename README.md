# Django Huey Logger

<p align="center">
<a href="https://travis-ci.org/lotrekagency/django-huey-logger" target="blank"><img src="https://travis-ci.org/lotrekagency/django-huey-logger.svg?branch=master"></a>
<a href="https://pypi.python.org/pypi/django-huey-logger/" target="blank"><img src="https://img.shields.io/pypi/v/django-huey-logger.svg"></a>
<a href="https://codecov.io/gh/lotrekagency/django-huey-logger" target="blank"><img src="https://codecov.io/gh/lotrekagency/django-huey-logger/branch/master/graph/badge.svg"></a>
</p>

A simple Django app to let you know if huey tasks are working without errors.

## Installation

```bash
pip install django-huey-logger
```

## Requirements

Needs [huey](https://huey.readthedocs.io/en/latest/contrib.html#django) installed and configured.

## Usage

**In your settings.py**

```py
INSTALLED_APPS = [
    'huey_logger',
    # Django modules
    ...
]
```

**Run migrations**

```
python manage.py migrate huey_logger
```

**Using the decorators**

Keep track of your periodic tasks by adding a decorator to your functions

```py
from huey_logger.decorators import log_db_periodic_task, log_db_task
from huey import crontab


@log_db_periodic_task(crontab(hour='*/1', minute=0))
def periodic_do_something():
    print("I'm saying hello every hour :)")

@log_db_task
def do_something_in_background():
    print("I'm saying hello under the hood")

```
