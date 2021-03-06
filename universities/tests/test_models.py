import datetime

import pytz
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase

from ..models import Major, University


class TestUniversity(TestCase):
    def test_create_delete(self):
        now_naive = datetime.datetime.now()
        timezone = pytz.timezone("UTC")
        now_aware = timezone.localize(now_naive)

        # test create
        university = University.objects.create()
        self.assertIsInstance(university, University)
        self.assertEqual(university.pk, 1)
        self.assertLessEqual(now_aware, university.created_at)
        self.assertLessEqual(now_aware, university.updated_at)

        # test delete
        university.delete()
        self.assertFalse(University.objects.exists())

    def test_fields(self):
        university = University.objects.create()

        name = "Test University"
        cnpj = "XX.XXX.XXX/0001-XX"
        university.name = name
        university.cnpj = cnpj
        university.save()

        self.assertEqual(university.name, name)
        self.assertEqual(university.cnpj, cnpj)

        # testing cpnj unique constrain
        with transaction.atomic():
            self.assertRaises(IntegrityError, University.objects.create, cnpj=cnpj)

    def test_ordering(self):
        university01 = University.objects.create(name="aTest University", cnpj="aaa")
        university03 = University.objects.create(name="cTest University", cnpj="bbb")
        university02 = University.objects.create(name="bTest University", cnpj="ccc")
        university05 = University.objects.create(name="eTest University", cnpj="ddd")
        university04 = University.objects.create(name="dTest University", cnpj="eee")

        self.assertEqual(
            list(University.objects.all()), [university01, university02, university03, university04, university05]
        )

    def test_str(self):
        university = University.objects.create()
        self.assertEqual(str(university), university.name)


class TestMajor(TestCase):
    def test_create_delete(self):
        # test create
        major = Major.objects.create()
        self.assertIsInstance(major, Major)
        self.assertEqual(major.pk, 1)

        # test delete
        major.delete()
        self.assertFalse(Major.objects.exists())

    def test_fields(self):
        major = Major.objects.create()

        name = "Computer Engeneering"
        major.name = name
        major.save()

        self.assertEqual(major.name, name)

        # testing name unique constrain
        with transaction.atomic():
            self.assertRaises(IntegrityError, Major.objects.create, name=name)

    def test_ordering(self):
        major01 = Major.objects.create(name="major a")
        major03 = Major.objects.create(name="major c")
        major02 = Major.objects.create(name="major b")
        major05 = Major.objects.create(name="major e")
        major04 = Major.objects.create(name="major d")

        self.assertEqual(list(Major.objects.all()), [major01, major02, major03, major04, major05])

    def test_str(self):
        major = Major.objects.create(name="Economics")
        self.assertEqual(str(major), major.name)
