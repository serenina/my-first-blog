from django.shortcuts import render
from django.db import models
import csv

class Image(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title

def image_list(request):
    images = read_csv()
    return render(request, 'elements/image_list.html', {'images' : images})


def read_csv():
    with open('test_application_data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        image_list = []
        for row in readCSV:
            image = Image()
            image.title = row[0]
            image.description = row[1]
            image.image = row[2]
            image_list.append(image)
        return image_list