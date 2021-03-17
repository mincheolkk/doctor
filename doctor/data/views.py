from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from collections import Counter

class PatientView(View):
    def get(self, request):

        total = Person.objects.count()
        female = Person.objects.filter(gender_source_value="F").count()
        male = total - female
        white = Person.objects.filter(race_source_value="white").count()
        asian = Person.objects.filter(race_source_value="asian").count()
        black = Person.objects.filter(race_source_value="black").count()
        other = Person.objects.filter(race_source_value="other").count()
        native = Person.objects.filter(race_source_value="native").count()
        non_hispanic = Person.objects.filter(ethnicity_source_value="nonhispanic").count()
        hispanic = total - non_hispanic
        death = Death.objects.count()

        race = {
            "asian":asian,
            "black":black,
            "native":native,
            "other":other,
            "white":white,

        }
        ethnicity = {
            "nonhispanic":non_hispanic,
            "hispanic":hispanic,
        }
        gender = {
            "male" :male,
            "female":female
        }
        answer = {"전체 환자 수":total,"성별 환자 수":gender,"인종별 환자 수":race , "민족별 환자 수":ethnicity, "사망 환자 수":death}
        return JsonResponse(answer)


class VisitView(View):
    def get(self,request):

        one = Visit.objects.filter(visit_concept_id=9201).count()
        two = Visit.objects.filter(visit_concept_id=9202).count()
        three = Visit.objects.filter(visit_concept_id=9203).count()

        all = Visit.objects.all()

        pre = []
        birth = []
        race = []
        ethnicity = []
        gender = []
        visit_g = []

        for row in all:
            row_person = row.person_id

            if row_person not in pre:
                row_person = row.person_id
                a = Person.objects.filter(person_id=row_person)
                c = a.values('race_source_value','year_of_birth','ethnicity_source_value','gender_source_value')
                race.append(c[0]['race_source_value'])
                birth.append(c[0]['year_of_birth'])
                ethnicity.append(c[0]['ethnicity_source_value'])
                gender.append(c[0]['gender_source_value'])
     
            pre.append(row_person)
            d = a.values('gender_source_value')
            visit_g.append(d[0]['gender_source_value'])
            visit_type = {"입원":one,"외래":two, "응급":three}

            answer = {"방문 유형별 방문 수:":visit_type,
                    "성별 방문수:":Counter(visit_g),
                    "인종별 환자 수:":Counter(race),
                    "민족별 환자 수:":Counter(ethnicity),
                    "연령별 환자 수:":Counter(birth)}

        return JsonResponse(answer)

