

# Create your models here.

from django.db import models

# Create your models here.
class Pokemon(models.Model):
	pokedex_num = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	type_1 = models.CharField(max_length=200)
	type_2 = models.CharField(max_length=200)
	total = models.IntegerField(default=0)
	hp = models.IntegerField(default=0)
	attack = models.IntegerField(default=0)
	defense = models.IntegerField(default=0)
	sp_attack = models.IntegerField(default=0)
	sp_defense = models.IntegerField(default=0)
	speed = models.IntegerField(default=0)
	generation = models.IntegerField(default=0)
	legendary = models.CharField(max_length=200)
	def __str__(self):
		return self.name

	"""

    def is_legendary(self):
    	return True if self.legendary else False
    	
    

    """
