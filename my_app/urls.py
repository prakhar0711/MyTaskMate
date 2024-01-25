from django.urls import path

from my_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('add-todo', views.add_todo, name='add-todo'),
    path('delete-todo/<int:id>', views.delete_todo, name='delete-todo'),
    path('update-status/<int:id>/<str:status>', views.update_status, name='update-status'),
]
