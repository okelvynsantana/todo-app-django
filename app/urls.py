from django.urls import path
from .views.task_views import index_tasks, create_task, update_task, delete_task, home
from .views.users_views import create_user, user_login, user_logout

urlpatterns = [
    path('tasks/', index_tasks, name='index_tasks'),
    path('tasks/create', create_task, name='create_task'),
    path('tasks/<int:id>/edit', update_task, name='update_task'),
    path('tasks/<int:id>/delete', delete_task, name='delete_task'),
    path('create_account/', create_user, name='create_account'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', home)

]
