from django.db import models

# Create your models here.

from postgres_copy import CopyManager

class Condition(models.Model):
    condition_occurrence_id = models.IntegerField(null=True)
    person_id = models.IntegerField(null=True)
    condition_concept_id = models.BigIntegerField(null=True)
    condition_start_date = models.DateField(max_length=30,null=True)
    condition_start_datetime = models.DateTimeField(max_length=30,null=True)
    condition_end_date = models.DateField(max_length=30,null=True)
    condition_end_datetime = models.DateTimeField(max_length=30, null=True)
    condition_type_concept_id = models.IntegerField(null=True)
    stop_reason = models.CharField(max_length=30, null=True)
    provider_id = models.IntegerField(null=True)
    visit_occurrence_id = models.BigIntegerField(null=True)
    visit_detail_id = models.IntegerField(null=True)
    condition_source_value = models.BigIntegerField(null=True)
    condition_source_concept_id = models.BigIntegerField(null=True)
    condition_status_source_value = models.BigIntegerField(null=True)
    condition_status_concept_id = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        db_table = 'conditions'


class Death(models.Model):
    person_id = models.BigIntegerField(null=True)
    death_date = models.DateField(null=True)
    death_datetime = models.DateTimeField(null=True)
    death_type_concept_id = models.IntegerField(null=True)
    cause_concept_id = models.IntegerField(null=True)
    cause_source_value = models.BigIntegerField(null=True)
    cause_source_concept_id = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        db_table = 'deaths'


class Person(models.Model):
    person_id = models.BigIntegerField(null=True)
    gender_concept_id = models.IntegerField(null=True)
    year_of_birth = models.IntegerField(null=True)
    month_of_birth = models.IntegerField(null=True)
    day_of_birth = models.IntegerField(null=True)
    birth_datetime = models.DateTimeField(null=True)
    race_concept_id = models.IntegerField(null=True)
    ethnicity_concept_id = models.IntegerField(null=True)
    location_id = models.IntegerField(null=True)
    provider_id = models.IntegerField(null=True)
    care_site_id = models.IntegerField(null=True)
    person_source_value = models.CharField(max_length=50, null=True)
    gender_source_value = models.CharField(max_length=10, null=True)
    gender_source_concept_id = models.IntegerField(null=True)
    race_source_value = models.CharField(max_length=20, null=True)
    race_source_concept_id = models.IntegerField(null=True)
    ethnicity_source_value = models.CharField(max_length=20, null=True)
    ethnicity_source_concept_id = models.IntegerField(null=True)
    objects = CopyManager()

    class Meta:
        db_table = 'persons'


class Drug(models.Model):
    drug_exposure_id = models.BigIntegerField(null=True)
    person_id = models.BigIntegerField(null=True)
    drug_concept_id = models.BigIntegerField(null=True)
    drug_exposure_start_date = models.DateField(null=True)
    drug_exposure_start_datetime = models.DateTimeField(null=True)
    drug_exposure_end_date = models.DateField(null=True)
    drug_exposure_end_datetime = models.DateTimeField(null=True)
    verbatim_end_date = models.DateField(null=True)
    drug_type_concept_id = models.BigIntegerField(null=True)
    stop_reason = models.CharField(max_length=50,null=True)
    refills = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    days_supply = models.BigIntegerField(null=True)
    sig = models.IntegerField(null=True)
    route_concept_id = models.IntegerField(null=True)
    lot_number = models.IntegerField(null=True)
    provider_id = models.IntegerField(null=True)
    visit_occurrence_id = models.BigIntegerField(null=True)
    visit_detail_id = models.IntegerField(null=True)
    drug_source_value = models.BigIntegerField(null=True)
    drug_source_concept_id = models.BigIntegerField(null=True)
    route_source_value = models.CharField(max_length=50,null=True)
    dose_unit_source_value = models.CharField(max_length=50, null=True)
    objects = CopyManager()

    class Meta:
        db_table = 'drugs'


class Visit(models.Model):
    visit_occurrence_id = models.BigIntegerField(null=True)
    person_id = models.BigIntegerField(null=True)
    visit_concept_id = models.BigIntegerField(null=True)
    visit_start_date = models.DateField(null=True)
    visit_start_datetime = models.DateTimeField(null=True)
    visit_end_date = models.DateField(null=True)
    visit_end_datetime = models.DateTimeField(null=True)
    visit_type_concept_id = models.BigIntegerField(null=True)
    provider_id = models.BigIntegerField(null=True)
    care_site_id = models.BigIntegerField(null=True)
    visit_source_value = models.CharField(max_length=50, null=True)
    visit_source_concept_id = models.BigIntegerField(null=True)
    admitting_source_concept_id = models.BigIntegerField(null=True)
    admitting_source_value = models.CharField(max_length=50, null=True)
    discharge_to_concept_id = models.BigIntegerField(null=True)
    discharge_to_source_value = models.CharField(max_length=50, null=True)
    preceding_visit_occurrence_id = models.BigIntegerField(null=True)
    objects = CopyManager()

    class Meta:
        db_table = 'visits'
