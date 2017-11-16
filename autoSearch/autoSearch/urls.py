from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from carros import views, urls, urls, models
from carros.views import car_list, car_detail
urlpatterns = [
    # Examples:
    # url(r'^$', 'autoSearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',admin.site.urls),
    url(r'^carros/', include('carros.urls')),
    url(r'^',include('carros.urls', namespace = "templates")),
    url(r'^detalle/(?P<pk>[0-9]+)/$', car_detail.as_view(),name='CarDetail'),
    url(r'^lista$',car_list.as_view(), name='CarList'),

]
