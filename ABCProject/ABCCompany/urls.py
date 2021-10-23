from django.urls import path

from .views import home
from .views import register
from .views import logout_request
from .views import login_view
from .views import individual_employee
from .views import delete_employee
from .views import emp_login_view
from .views import num_to_word


urlpatterns = [
    path('', home, name='register'),
    path('emp-reg/', register, name='register'),
    path('delete/<int:id>', delete_employee, name='delete_employee'),
    path('view/<int:id>/', individual_employee, name='individual_employee'),
    path('num-word/', num_to_word, name='num_to_word'),
    path('admin-login/', login_view, name='login_view'),
    path('emp-login/', emp_login_view, name='emp_login_view'),
    path('logout/', logout_request, name='login_view'),
]

