from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^battery/$', 'ld_recruitment_lb.battery.views.battery', name='battery'),
    url(r'^wifi/$', 'ld_recruitment_lb.wifi.views.wifi', name='wifi'),
    url(r'^$', 'ld_recruitment_lb.common.views.index', name='index'),

    # url(r'^battery_and_wifi/', include('battery_and_wifi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
