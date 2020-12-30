from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suren', views.create_subject_file, name='file'),
    #path('saveFileName', views.save_file_name, name='save'),
    #path('getAllFiles', views.get_all_files, name='getallfile'),
    #path('createAccount', views.create_account, name="folder"),
    path('login', views.login_view, name='login'),
    path('rel', views.link, name='rel'),
    path('changeLink', views.change_link, name="changeLink"),
    path('rel/<str:file_path>/<str:file_name>', views.flights, name='flights'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('createAccount', views.create_account, name='createAccount')
]