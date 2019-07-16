# Django Huey Logger

A simple Django app to let you know if huey cron are working without errors.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Django Huey Logger.

```bash
pip install git+https://github.com/bnznamco/django-huey-logger.git
```
## Requirements

Needs [huey](https://huey.readthedocs.io/en/0.4.9/django.html) installed and configured.


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
