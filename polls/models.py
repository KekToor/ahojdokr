from django.db import models

class Rodice(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    jmeno = models.CharField(max_length=20, help_text='Zadej jméno rodiče')
    prijmeni = models.CharField(max_length=20, help_text='Zadej příjmení rodiče')

    # Metadata
    class Meta:
        ordering = ['-prijmeni']

    # Methods
    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of MyModelName."""
    #     return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.prijmeni

class Dite(models.Model):
    parent = models.ForeignKey(Rodice, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
