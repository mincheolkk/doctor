from django.urls import path
from data.views import *

urlpatterns = [
    path('/patient', PatientView.as_view()),
    path('/visit', VisitView.as_view())

]
