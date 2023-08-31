
from django.urls import path
# from accounts.views import login_page , register_page
from accounts import views


urlpatterns = [
    path('login/',views.login_page , name="login"),
    path('register/',views.register_page , name="register")


]