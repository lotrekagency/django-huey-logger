import pytest
import time
import huey
from huey_logger.decorators import log_db_periodic_task, log_db_task
from huey import crontab
from huey_logger.models import LastCronRun, CronError


@log_db_task()
def do_something():
    print("I'm saying hello :)")


@log_db_task()
def do_something_with_errors():
    print("I'm throwing errors :)")
    raise Exception('Fail')


@log_db_periodic_task(crontab(minute='0'))
def do_something_every_hour():
    print("I'm saying hello every hour :)")


@pytest.mark.django_db
def test_numbers_of_last_cron_log(settings, client):
    do_something()
    do_something_with_errors()
    do_something_every_hour()
    assert LastCronRun.objects.all().count() == 3


@pytest.mark.django_db
def test_numbers_of_last_cron_log(settings, client):
    do_something()
    do_something_with_errors()
    assert CronError.objects.all().count() == 1
