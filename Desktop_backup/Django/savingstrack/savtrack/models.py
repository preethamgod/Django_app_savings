from django.db import models
from datetime import date

options = (('Yes', 'Yes'), ('No', 'No'))
year1 = date.today().strftime("%Y")


class my_savings(models.Model):
    sa_id = models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    transaction_amt = models.IntegerField(null=True)
    tran_type = models.CharField(max_length=10)
    transaction_date = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return u'%s %s' % (self.tran_type, self.name)

