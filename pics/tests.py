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

    # Testing the delete method
    def test_delete_method(self):
        self.home.save_location()
        self.home.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)

    # Testing the update method
    def test_update_method(self):
        self.home.save_location()
        self.home.update_location()
        updated_location = Location.objects.filter(place = "Home").update(place = "Away")
        self.assertTrue(self.home.place != updated_location)
        self.assertNotEqual(self.home, updated_location)


class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.travel = Category(category = "Travel")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.travel, Category))

    # Testing the save method
    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # Testing the delete method
    def test_delete_method(self):
        self.travel.save_category()
        self.travel.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) < 1)

    # # Testing the update method
    # def test_update_method(self):
    #     self.home.save_location()
    #     self.home.update_location()
    #     updated_location = Location.objects.filter(place = "Home").update(place = "Away")
    #     self.assertTrue(self.home.place != updated_location)