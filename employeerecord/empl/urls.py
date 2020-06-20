from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_employees,name='allEmp'),
    path('addEmployee/', views.add_employees,name='addEmp'),
    path('editEmployee/<int:id>', views.edit_employees,name='editEmp'),
    path('viewEmployee/<int:id>', views.one_employee,name='oneEmp'),
    path('deleteEmployee/<int:id>', views.delete_employee,name='deleteEmp'),
]
