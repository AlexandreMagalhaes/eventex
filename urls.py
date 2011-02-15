from django.contrib import admin
from django.conf.urls.defaults import *
from core.views import *
from django.conf import settings

admin.autodiscover()
urlpatterns = patterns('',
    (r'^$', homepage),
	(r'^admin/', include(admin.site.urls)),
)	

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
    )