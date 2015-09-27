from django.conf.urls import url

from .views import page
import views


urlpatterns = (
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    url(r'^$', page, name='homepage'),
    url(r'^pdf_view/$', views.pdf_view , name="pdf_view"),
)
