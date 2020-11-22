from django.conf.urls import url
from . import views

app_name ='account'

urlpatterns =[
    #url(r'^selection/$',views.selection_view,name="selection"),
    url(r'^signup/$',views.signup_view,name="signup"),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^profile/(?P<user>[\w-]+)/$',views.profile_view,name="profile"),
    url(r'^profile_edit/',views.profile_edit_view,name="profile_edit"),
    url(r'profile_view/(?P<user>[\w-]+)/$',views.profile_search_result,name="profile_view")

]