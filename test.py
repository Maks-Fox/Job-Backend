from celery import Celery


def test_task():
    celery_app = Celery('tasks')
    celery_app.conf.broker_url = 'redis://localhost:6379/0'
    celery_app.conf.result_backend = 'redis://localhost:6379/0'

    task = celery_app.send_task('KeyWordParseTask', ('отдых деньги девочки',))
    print(task.id)


if __name__ == '__main__':
    test_task()
