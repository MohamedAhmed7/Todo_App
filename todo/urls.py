from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('addtodo/', views.addTodo, name='add_todo'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('incomplete/<todo_id>', views.incompleteTodo, name='incomplete'),
    path('delete_completed', views.deleteCompleted, name='delcompleted'),
    path('delete_all', views.deleteAll, name='delete_all')

]
