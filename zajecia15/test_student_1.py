from unittest import TestCase
from student_1 import Student


class TestStudent(TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('teardownclass')

    def setUp(self):
        print('setUp')
        self.obj_anna = Student('ana', 'kowalska', 4.6, None)
        self.obj_arek = Student('arkadiusz', 'nowak', 3.8, None)

    def tearDown(self):
        print('TearDown')

    def test_email(self):
        self.assertEqual(self.obj_anna.email, 'ana.kowalska@university.com')
        self.obj_anna.name = 'anna'
        self.assertEqual(self.obj_anna.email, 'anna.kowalska@university.com')

        self.assertEqual(self.obj_arek.email, 'arkadiusz.nowak@university.com')
        self.obj_arek.name = 'arek'
        self.assertEqual(self.obj_arek.email, 'arek.nowak@university.com')

    def test_fullname(self):
        self.assertEqual(self.obj_anna.fullname, 'Ana Kowalska')
        self.obj_anna.last = 'Zamezna'
        self.assertEqual(self.obj_anna.fullname, 'Ana Zamezna')

        self.assertEqual(self.obj_arek.fullname, 'Arkadiusz Nowak')
        self.obj_arek.last = 'Kowal'
        self.assertEqual(self.obj_arek.fullname, 'Arkadiusz Kowal')

    def test_scholarship(self):
        self.obj_anna.grant_scholarship()
        self.assertEqual(self.obj_anna.scholarship, True)
        # self.assertEqual(self.obj_anna.scholarship, False)

        self.obj_arek.grant_scholarship()
        self.assertEqual(self.obj_arek.scholarship, False)
        # self.assertEqual(self.obj_arek.scholarship, True)
