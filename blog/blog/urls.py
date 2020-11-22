from django.contrib import admin
from django.conf.urls import url,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

app_name="blog"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/',include('account.urls')),
    url(r'^articles/',include('articles.urls')),
    url(r'^about/$',views.about,name="about"),
    url(r'^contact/$',views.contact,name="contact"),
    url(r'^$',article_views.article_list,name="home"),
    url(r'^search/$',views.search_view,name="search"),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
