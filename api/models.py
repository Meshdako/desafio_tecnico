from django.db import models

# Create your models here.
class Word(models.Model):
    # palabra ingresada y regla ocupada.
    input_word = models.CharField(max_length = 50)
    output_word = models.CharField(max_length = 50)
    the_rule = models.PositiveBigIntegerField()
    
class Rules(models.Model):
    rule_1 = models.PositiveBigIntegerField()
    rule_2 = models.PositiveBigIntegerField()
    rule_3 = models.PositiveBigIntegerField()
    rule_4 = models.PositiveBigIntegerField()