"""lastVKR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,re_path
from forum.views import first_pages,forum_page,login_user,Addcomment1,registration,Article_comment,News,Photo,logout_user,registr_user,Photo_banay,Rooms_banay,Sport_banay,Pravila
from persons import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path( r'^$', first_pages),
    re_path( r'^forum/$', forum_page),
    re_path( r'^forum/(\d+)/$', forum_page),
    re_path( r'^login/$', login_user),
    re_path( r'^forum/forum_article/(?P<article_id>\d+)/?$', Article_comment),
    re_path( r'^forum/forum_article/addcomment/(?P<article_id>\d+)/?$', Addcomment1),
    re_path( r'^registrform/$', registr_user),
    re_path( r'^an_ms/$', views.an_message),
    re_path( r'^news/$', News),
    re_path( r'^photo/$', Photo),
    re_path( r'^photo/photo_banay/$', Photo_banay),
    re_path( r'^photo/rooms/$', Rooms_banay),
    re_path( r'^photo/sport/$', Sport_banay),
    re_path( r'^logout/$', logout_user),
    re_path( r'^pravila/$', Pravila),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
