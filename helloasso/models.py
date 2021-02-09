from django.db import models


class Organism(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    type = models.CharField(max_length=120)
    funding = models.FloatField()
    supporters = models.IntegerField()
    logo = models.URLField()
    thumbnail = models.URLField()
    profile = models.CharField(max_length=120)
    donate_form = models.CharField(max_length=120, null=True)
    def __str__(self):
        return '%s' % (self.name)

class Campaign(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120, null=True)
    slug = models.SlugField()
    type = models.CharField(max_length=120, null=True)
    state = models.CharField(max_length=120, null=True)
    funding = models.FloatField()
    supporters = models.IntegerField()
    url = models.URLField(null=True)
    organism = models.ForeignKey(
        Organism, on_delete=models.CASCADE, related_name="campaign", null=True)
    slug_organism = models.SlugField(null=True)
    creation_date = models.DateField(null=True)
    last_update = models.CharField(max_length=120, null=True)
    place_name = models.CharField(max_length=120, null=True)
    place_address = models.CharField(max_length=120, null=True)
    place_city = models.CharField(max_length=120, null=True)
    place_zipcode = models.CharField(max_length=120, null=True)
    place_country = models.CharField(max_length=120, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return '%s [%s] ---- %s' % (self.name,self.type,self.organism)

class Payment(models.Model):
    amount = models.FloatField()
    date = models.DateField()
    id = models.IntegerField(primary_key=True)
    mean = models.CharField(max_length=120)
    payer_address = models.CharField(max_length=120)
    payer_city = models.CharField(max_length=120)
    payer_country = models.CharField(max_length=120)
    payer_email = models.EmailField()
    payer_first_name = models.CharField(max_length=120)
    payer_is_society = models.CharField(max_length=120)
    payer_last_name = models.CharField(max_length=120)
    payer_society = models.CharField(max_length=120)
    payer_zip_code = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    url_receipt = models.URLField()
    url_tax_receipt = models.URLField()


class Action(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    email = models.EmailField()
    amount = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name='actions', null=True)
    organism = models.ForeignKey(
        Organism, on_delete=models.CASCADE, related_name='actions', null=True)
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name='actions', null=True)
    option_label = models.CharField(max_length=120)

    def __str__(self):
        return '%s,%s,%s,%s [%s : %s] ---- %s ' %  (self.first_name, self.last_name, str(self.email), str(self.date),str(self.status), self.type, str(self.campaign))


class CustomInfo(models.Model):
    label = models.CharField(max_length=240)
    value = models.CharField(max_length=240)
    action = models.ForeignKey(
        Action, on_delete=models.CASCADE, related_name='custominfo')

    def __str__(self):
        return '%s : %s --- %s' % (self.label,self.value,self.action)

    class Meta:
        unique_together = (("action", "label", "value"),)
