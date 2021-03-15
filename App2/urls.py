from django.contrib import admin
from django.urls import path
from App2 import views

urlpatterns = [
    path('',views.woven,name="woven"),
    path('',views.sweater,name="sweater"),
    path('',views.denim,name="denim"),
    path('',views.accessories,name="accessories"),
    path('',views.design,name="design"),
    path('',views.ancillary,name="ancillary"),
    path('',views.normalwash,name="normalwash"),
    path('',views.pigmentwash,name="pigmentwash"),
    path('',views.bleachwash,name="bleachwash"),
    path('',views.stonewash,name="stonewash"),
    path('',views.acidwash,name="acidwash"),
    path('',views.enzymewash,name="enzymewash"),
    path('',views.custicwash,name="custicwash"),
    path('',views.garmentwash,name="garmentwash"),
    path('',views.whitening,name="whitening"),

]
