from django.conf.urls import url, include
from django.contrib.auth import views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'flashcards'

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
