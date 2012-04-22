from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('main.views',
    url(r'login/?$', 'login', name='login'),
    url(r'hackers/add/?$', 'add_hacker', name='add_hacker'),
    url(r'enterprises/add/?$', 'add_enterprise', name='add_enterprise'),
    url(r'enterprises/?$', 'list_enterprise', name='list_enterprise'),
    url(r'hacker/(?P<hacker_id>\d+)/services/?$', 'timeline_services', name='timeline_services'),
    url(r'hackers/?$', 'list_hackers', name='list_hackers'),
    url(r'services/add/?$', 'add_service', name='add_service'),
    url(r'service/(?P<service_id>\d+)/?$', 'service', name='service'),
)
