from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^$', 'src.core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
