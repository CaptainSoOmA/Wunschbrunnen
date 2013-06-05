from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','Zettel.views.index'),
    url(r'^all','Zettel.views.all_zettel'),
    url(r'^new/create','Zettel.views.insert_zettel'),
    url(r'^new','Zettel.views.new_zettel'),
    url(r'^zettel/(?P<zettel_id>\d+)/','Zettel.views.zettel'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
