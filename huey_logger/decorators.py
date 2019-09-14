import functools
from django.utils import timezone
from .models import LastCronRun, CronError
from huey.contrib.djhuey import db_periodic_task, db_task, task, periodic_task


def _log_task(cron_name, func, *args, **kwargs):
        try:
            cron_obj, created = LastCronRun.objects.get_or_create(name=cron_name)
            cron_obj.started_at = timezone.now()
            print('RUNNING %s' % cron_name)
            func(*args, **kwargs)
            cron_obj.save()
        except Exception as ex:
            error_obj, _ = CronError.objects.get_or_create(
                name=cron_name,
                error=str(ex)
            )


def log_db_periodic_task(*args, **kwargs):
    def decorator(func):
        @db_periodic_task(*args, **kwargs)
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            cron_name = func.__name__
            _log_task(cron_name, func, *args, **kwargs)
        return wrapped_func
    return decorator


def log_db_task(*args, **kwargs):
    def decorator(func):
        @db_task(*args, **kwargs)
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            cron_name = func.__name__
            _log_task(cron_name, func, *args, **kwargs)
        return wrapped_func
    return decorator


def log_periodic_task(*args, **kwargs):
    def decorator(func):
        @periodic_task(*args, **kwargs)
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            cron_name = func.__name__
            _log_task(cron_name, func, *args, **kwargs)
        return wrapped_func
    return decorator


def log_task(*args, **kwargs):
    def decorator(func):
        @task(*args, **kwargs)
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            cron_name = func.__name__
            _log_task(cron_name, func, *args, **kwargs)
        return wrapped_func
    return decorator
