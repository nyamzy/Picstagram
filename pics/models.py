from django.db import models

# Create your models here.
class Location(models.Model):
    place = models.CharField(max_length = 30)

    def __str__(self):
        return self.place
    
    # Save location method
    def save_location(self):
        self.save()

    # Delete location method
    def delete_location(self):
        self.delete()

    # Update location method
    def update_location(self):
        updated_location = Location.objects.filter().update()
        return updated_location


class Category(models.Model):
    category = models.CharField(max_length = 20)

    def __str__(self):
        return self.category

    # Save category method
    def save_category(self):
        self.save()

    # Delete category method
    def delete_category(self):
        self.delete()

    # Update category method
    def update_category(self):
        updated_category = Category.objects.filter().update()
        return updated_category


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add = True)
    url = models.URLField(max_length = 200)

    def __str__(self):
        return self.image_name