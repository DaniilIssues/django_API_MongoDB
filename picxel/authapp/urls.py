from django.urls import path, include
import authapp.views as auth

app_name = 'authapp'

urlpatterns = [
    path('signup/', auth.SignUpView.as_view(), name='signup'),
    path('login/', auth.MyLoginView.as_view(), name='login'),
    # path('logout/', auth.logout, name='logout'),
]
