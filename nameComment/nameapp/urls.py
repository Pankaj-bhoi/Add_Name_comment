from django.conf.urls import url
from nameapp import views

app_name = 'nameapp'

urlpatterns = [
    url('^$',views.makeentry,name='makeentry')
]