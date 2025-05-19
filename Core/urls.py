
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
import uuid


from TodoList.views import *
from account import views
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', admin.site.urls),
    path('schema-viewer/', include('schema_viewer.urls')),

    # ************To Do list App*************
    path("", tasks_list, name='home'),
    path("add_list/", add_list, name='add_list'),
    path("achieve/<uuid:task_id>/", mark_achieved, name="mark_achieved"),
    path("unachieve/<uuid:task_id>/", unmark_achieved, name="unmark_achieved"),
    path("update/<uuid:task_id>/", update, name="update"),
    path("delete/<uuid:task_id>/", delete, name="delete"),



    # ************Account App*************
    path("login_page", login_page, name = "login_page"),
    path('logout/', views.login_page, name='logout'),
    path("registration_page", registration_page, name = "registration_page"),


]
