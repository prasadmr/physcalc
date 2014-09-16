from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'calculator.views.homepage', name='home'),
    url(r'^resistance/', include('resistance.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
