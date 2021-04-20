from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.basepage, name='base'),
    path('sendmessage', views.basepage, name='sendmessage'),
    path('', include(('main_app.urls', 'home'), namespace='home')),
    path('summernote/', include('django_summernote.urls')),
    url(r'^download/(?P<path>.*)$',serve,{'document_root': settings.MEDIA_ROOT})

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
