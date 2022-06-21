from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base/',BASE,name='base'),
    path('login/',Login.as_view(),name='login'),
    path('',INDEX,name='home'),
    path('/<int:page>',INDEX,name='home'),
    path('register/',Register.as_view(),name='register'),
    # path('single/',Single.as_view(),name='single'),
    path('blog/<int:pk>',Single.as_view(),name='blog'),
    path('addPost/',addPost,name='add_post'),    
    path('addTopic/',AddTopic.as_view(),name='add_topic'),
    path('editPost/<int:pk>',editPost,name='edit_post'),
    path('deletePost/<int:pk>',deletePost,name='delete_post'),
    path('addUser/',AddUser.as_view(),name='add_user'),
    path('logout/',LOGOUT,name='logout'),
    path('mtopic/',ManageTopic.as_view(),name="manage_topic"),
    path('mpost/',ManagePost.as_view(),name="manage_post"),
    path('muser/',ManageUser.as_view(),name="manage_user"),
    path('topic/<int:pk>/',TopicView.as_view(),name='topic'),
    path('topic/<int:pk>/<int:page>/',TopicView.as_view(),name='topic'),
    path('search/',Search.as_view(),name='search'),
    path('search/<int:page>',Search.as_view(),name='search'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('addTopic/',addTopic,name='add_topic'),
    path('editTopic/<int:pk>',editTopic,name='edit_topic'),
    path('deleteTopic/<int:pk>',deleteTopic,name='delete_topic'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)