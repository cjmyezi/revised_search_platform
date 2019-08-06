from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views
import user_system
import task_manager
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'annotation_platform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user_system.urls')),
    url(r'^task/', include('task_manager.urls')),
    url(r'^search_api/', include('search_api.urls')),
    url(r'^exp_domain_expertise/', include('exp_domain_expertise.urls')),
    url(r'^chromeext_ajax/', include('chromeext_ajax.urls')),
    url(r'^processed/', include('processed.urls')),
    url(r'^html_pos/', include('html_pos.urls')),
    url(r'^$', views.index)
]
