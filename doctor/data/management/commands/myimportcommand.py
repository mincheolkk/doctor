from data.models import Condition, Death, Drug, Person, Visit
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        insert_count_condition = Condition.objects.from_csv('/Users/K/Downloads/synthea_cdm_csv/condition_occurrence.csv')
        print("{} records inserted".format(insert_count_condition))

        insert_count_death = Death.objects.from_csv('/Users/K/Downloads/synthea_cdm_csv 2/death.csv')
        print("{} records inserted".format(insert_count_death))

        insert_count_person = Person.objects.from_csv('/Users/K/Downloads/synthea_cdm_csv 2/person.csv')
        print("{} records inserted".format(insert_count_person))

        insert_count_drug = Drug.objects.from_csv('/Users/K/Downloads/synthea_cdm_csv 2/drug_exposure.csv')
        print("{} records inserted".format(insert_count_drug))

        insert_count_visit = Visit.objects.from_csv('/Users/K/Downloads/synthea_cdm_csv 2/visit_occurrence.csv')
        print("{} records inserted".format(insert_count_visit))
