from django.conf.urls import url

from System import views

urlpatterns = [
    url(r'userRegist/', views.userRegist, name='userRegist'),
    url(r'userLogin/', views.userLogin, name='userLogin'),
    url(r'^userList/', views.userList, name='userList'),
    url(r'userAdd/', views.userAdd, name='userAdd'),
    url(r'userDelete/', views.userDelete, name='userDelete'),
    url(r'userUpdate/', views.userUpdate, name='userUpdate'),

    # url(r'fenye/', views.fenye, name='page'),
]
