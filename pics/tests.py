from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.home = Location(place = "Home")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.home, Location))

    # Testing the save method
    def test_save_method(self):
        self.home.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.home.save_location()
        self.home.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)