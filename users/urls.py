from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from config import settings
from users.apps import UsersConfig
from users.views import email_verification, reset_password, ProfileView, UserRegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),    # вход
    path('logout/', LogoutView.as_view(), name='logout'),                           # выход
    path('register/', UserRegisterView.as_view(), name='register'),                   # регистрация
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),   # верификация почты
    path('reset_password/', reset_password, name='reset_password'),                 # сброс и восстановление пароля
    path('profile/', ProfileView.as_view(), name='profile'),                        # редактирование профиля

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
