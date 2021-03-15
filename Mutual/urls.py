from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from App1 import views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('about',views.about, name="about"),
    path('board/members',views.member,name="member"),
    path('contact/us',views.contactus,name="contact"),
    path('feedback',views.feedback,name="feedback"),
    path('merchandising',views.mer,name="merchandising"),
    path('woven',include('App2.urls'),name="woven"),
    path('sweater',include('App2.urls'),name="sweater"),
    path('denim',include('App2.urls'),name="denim"),
    path('accessories',include('App2.urls'),name="accessories"),
    path('design',include('App2.urls'),name="design"),
    path('ancillary',include('App2.urls'),name="ancillary"),
    path('normalwash', include('App2.urls'), name="normalwash"),
    path('pigmentwash', include('App2.urls'), name="pigmentwash"),
    path('bleachwash', include('App2.urls'), name="bleachwash"),
    path('stonewash', include('App2.urls'), name="stonewash"),
    path('acidwash', include('App2.urls'), name="acidwash"),
    path('enzymewash', include('App2.urls'), name="enzymewash"),
    path('custicwash', include('App2.urls'), name="custicwash"),
    path('Garment/washand/over/dye', include('App2.urls'), name="garmentwash"),
    path('whitening', include('App2.urls'), name="whitening"),
    path("products/",include('product.urls'),name="products"),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
