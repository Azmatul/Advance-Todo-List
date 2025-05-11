"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import uuid


from TodoList.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", tasks_list, name='home'),  # map home to task list view
    path("add_list/", add_list, name='add_list'),
    path("achieve/<uuid:task_id>/", mark_achieved, name="mark_achieved"),
    path("unachieve/<uuid:task_id>/", unmark_achieved, name="unmark_achieved"),
    path("update/<uuid:task_id>/", update, name="update"),
    path("delete/<uuid:task_id>/", delete, name="delete"),
]
