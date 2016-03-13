import debugsettings as settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', 'suggest.views.home'),
    (r'^suggest/ajax/lat_lng/(?P<addr>[^/]*)/$', 'suggest.views.json_lat_lng'),
    (r'^suggest/ajax/find_venues/(?P<lat>[^,]*),(?P<lng>[^,/]*)/$', 'suggest.views.json_find_simple'),
    (r'^suggest/ajax/find_venues/(?P<lat>[^,]*),(?P<lng>[^,/]*)/(?P<country>[a-zA-Z ]*)/(?P<director>[a-zA-Z ]*)/$', 'suggest.views.json_find_venues'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^js/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.JS_ROOT}))
    urlpatterns += patterns('',
        (r'^images/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.IMAGES_ROOT}))
