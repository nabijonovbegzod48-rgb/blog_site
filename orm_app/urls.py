from django.urls import path
from .views import index_page, get_max_salary_employees, get_dependents
from .views import add_customer
urlpatterns = [
    path('', index_page, name='orm_list'),
    path('salary/<int:top>', get_max_salary_employees, name='employee-list'),
    path('deps/<int:employee_id>', get_dependents, name='deps-list'),
    path("add-customer/", add_customer, name="add_customer"),
]