from django.conf.urls import include, url
from django.contrib import admin
from views import getDisplay, getChatting, IndexView
urlpatterns = [
    # Examples:
    # url(r'^$', 'MagicMirror.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/getDisplay', getDisplay),
    url(r'^api/chattingDisplay', getChatting),
    url(r'^$', IndexView.as_view()),    
]
