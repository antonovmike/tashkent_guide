from django.db import models
# from django.urls import
from django.urls import reverse


class ShowplaceType(models.Model):
    name = models.CharField(max_length=20, help_text="Enter showplace type", verbose_name="Showplace type")

    def __str__(self):
        return self.name


class Museum(models.Model):
    name = models.CharField(max_length=30, help_text="Enter museum's name", verbose_name="Museum's name")
    showplace_type = models.ForeignKey("ShowplaceType", on_delete=models.CASCADE,
                                       help_text="Choose showplace type",
                                       verbose_name="Showplace type", null=True)
    summary = models.TextField(max_length=1000, help_text="Enter summary", verbose_name="Summary")
    address = models.CharField(max_length=30, help_text="Enter address", verbose_name="Address")
    telephone = models.CharField(max_length=13, help_text="Enter phone number", verbose_name="Phone number")
    price = models.CharField(max_length=10, help_text="Enter ticket's price", verbose_name="Ticket's price")
    schedule = models.CharField(max_length=11, help_text="Enter working hours in format 09:00-17:30", verbose_name="Working hours")
    dayoff = models.CharField(max_length=15, help_text="Enter dayoff", verbose_name="Dayoff")
    website = models.CharField(max_length=30, help_text="Enter web site address", verbose_name="Web site address")
    map_2gis = models.CharField(max_length=50, help_text="Enter 2gis map link", verbose_name="2gis")
    map_google = models.CharField(max_length=50, help_text="Enter Google map link", verbose_name="Google")
    latitude = models.CharField(max_length=20, help_text="Enter latitude", verbose_name="Latitude")
    longitude = models.CharField(max_length=20, help_text="Enter longitude", verbose_name="Longitude")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('museum-detail', args=[str(self.id)])
