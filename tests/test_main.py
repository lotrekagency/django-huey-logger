import pytest
import time
import huey
from huey_logger.decorators import log_db_periodic_task, log_db_task, log_task, log_periodic_task
from huey import crontab
from huey_logger.models import LastCronRun, CronError


@log_db_task()
def do_something():
    print("I'm saying hello :)")


@log_db_periodic_task(crontab(minute='0'))
def do_something_every_hour():
    print("I'm saying hello every hour :)")


@log_db_task()
def do_something_with_errors():
    print("I'm throwing errors :)")
    raise Exception('Fail')


@log_task()
def do_something_without_db():
    print("I'm saying hello :)")


@log_periodic_task(crontab(minute='0'))
def do_something_every_hour_without_db():
    print("I'm saying hello every hour :)")


@log_task()
def do_something_with_errors_without_db():
    print("I'm throwing errors :)")
    raise Exception('Fail')


@pytest.mark.django_db
def test_db_numbers_of_last_cron_log(settings, client):
    do_something()
    do_something_with_errors()
    do_something_every_hour()
    assert LastCronRun.objects.all().count() == 3


@pytest.mark.django_db
def test_db_errors(settings, client):
    do_something()
    do_something_with_errors()
    errors = CronError.objects.all()
    assert len(errors) == 1
    assert errors[0].name == 'do_something_with_errors'
    assert errors[0].error == 'Fail'


@pytest.mark.django_db
def test_numbers_of_last_cron_log(settings, client):
    do_something_without_db()
    do_something_with_errors_without_db()
    do_something_every_hour_without_db()
    assert LastCronRun.objects.all().count() == 3


@pytest.mark.django_db
def test_errors(settings, client):
    do_something_without_db()
    do_something_with_errors_without_db()
    errors = CronError.objects.all()
    assert len(errors) == 1
    assert errors[0].name == 'do_something_with_errors_without_db'
    assert errors[0].error == 'Fail'
