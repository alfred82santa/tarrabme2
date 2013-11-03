from django.db import models

# Create your models here.
class Sequence(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, validators=[ 
        MinLengthValidator(4), 
        RegexValidator( 
            regex="^[a-z0-9_]+$", 
            message=_("Sequence name must be a string with just letters and number without spaces") 
            ) 
        ])
    sequence_name = models.CharField(max_length=100, unique=True, 
        null=False, blank=False)
    min_value = models.PositiveIntegerField('Min value', null=False, default=1)
    min_value = models.PositiveIntegerField('Max value', null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Sequence, self).save(force_insert, force_update, using, update_fields)
        if (create):
            #create_sequence(self.sequence_name, self.min_value, self.max_value)
            pass
        else:
            #set_limits(self.name, self.min_value, self.max_value)

    def delete(self, using=None):
        super(Sequence, self).delete(using)
        #delete_sequence(self.name)
    def get_current(self):
        #return current_value(self.name):
        pass
    def get_next(self):
        #return next_value(self.name):
        pass
    def reset(self):
        #reset(self.name):
        #set_limits(self.name, self.min_value, self.max_value)
        pass
    def set_next_value(self, value):
        #set_next_value(self.name, value)
        pass
