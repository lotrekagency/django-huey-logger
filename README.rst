Django Huey Logger
==================

A simple Django app to let you know if huey tasks are working without
errors.

Installation
------------

.. code:: bash

    pip install django-huey-logger

Requirements
------------

Needs `huey <https://huey.readthedocs.io/en/latest/contrib.html#django>`__
installed and configured.

Usage
-----

**In your settings.py**

.. code:: py

    INSTALLED_APPS = [
        'huey_logger',
        # Django modules
        ...
    ]

**Run migrations**

::

    python manage.py migrate huey_logger

**Using the decorators**

Keep track of your periodic tasks by adding a decorator to your
functions

.. code:: py

    from huey_logger.decorators import log_db_periodic_task, log_db_task
    from huey import crontab


    @log_db_periodic_task(crontab(hour='*/1', minute=0))
    def periodic_do_something():
        print("I'm saying hello every hour :)")

    @log_db_task
    def do_something_in_background():
        print("I'm saying hello under the hood")

