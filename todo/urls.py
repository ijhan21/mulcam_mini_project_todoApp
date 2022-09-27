from django.urls import path
from . import views
urlpatterns = [    
    path('',views.todolist, name='todo'),
    path('addtodo/',views.addTodo, name='add'),
    path('todofinish/<int:id>',views.todofinish, name='finish'),
    path('todobackout/',views.todoback, name='backout'),
    path('updatetodo/<int:id>',views.updatetodo, name='update'),
    path('tododelete/<int:id>',views.tododelete, name='delete'),
]
