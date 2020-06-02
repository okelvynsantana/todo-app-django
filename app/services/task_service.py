from app.models import Task


def create_task(task):
    Task.objects.create(title=task.title, description=task.description,
                        expiration_date=task.expiration_date,
                        priority=task.priority, user=task.user)


def index_tasks(user):
    return Task.objects.filter(user=user).all


def search_task_id(id):
    return Task.objects.get(id=id)


def update_task(task, updated_task):
    task.title = updated_task.title
    task.description = updated_task.description
    task.expiration_date = updated_task.expiration_date
    task.priority = updated_task.priority
    task.save(force_update=True)


def delete_task(task):
    task.delete()
