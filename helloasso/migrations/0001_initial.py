# Generated by Django 2.0 on 2019-08-12 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=120, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=120, null=True)),
                ('option_label', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, null=True)),
                ('slug', models.SlugField()),
                ('type', models.CharField(max_length=120, null=True)),
                ('state', models.CharField(max_length=120, null=True)),
                ('funding', models.FloatField()),
                ('supporters', models.IntegerField()),
                ('url', models.URLField(null=True)),
                ('slug_organism', models.SlugField(null=True)),
                ('creation_date', models.DateField(null=True)),
                ('last_update', models.CharField(max_length=120, null=True)),
                ('place_name', models.CharField(max_length=120, null=True)),
                ('place_address', models.CharField(max_length=120, null=True)),
                ('place_city', models.CharField(max_length=120, null=True)),
                ('place_zipcode', models.CharField(max_length=120, null=True)),
                ('place_country', models.CharField(max_length=120, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=240)),
                ('value', models.CharField(max_length=240)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custominfo', to='helloasso.Action')),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('type', models.CharField(max_length=120)),
                ('funding', models.FloatField()),
                ('supporters', models.IntegerField()),
                ('logo', models.URLField()),
                ('thumbnail', models.URLField()),
                ('profile', models.CharField(max_length=120)),
                ('donate_form', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('mean', models.CharField(max_length=120)),
                ('payer_address', models.CharField(max_length=120)),
                ('payer_city', models.CharField(max_length=120)),
                ('payer_country', models.CharField(max_length=120)),
                ('payer_email', models.EmailField(max_length=254)),
                ('payer_first_name', models.CharField(max_length=120)),
                ('payer_is_society', models.CharField(max_length=120)),
                ('payer_last_name', models.CharField(max_length=120)),
                ('payer_society', models.CharField(max_length=120)),
                ('payer_zip_code', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
                ('type', models.CharField(max_length=120)),
                ('url_receipt', models.URLField()),
                ('url_tax_receipt', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='organism',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign', to='helloasso.Organism'),
        ),
        migrations.AddField(
            model_name='action',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='helloasso.Campaign'),
        ),
        migrations.AddField(
            model_name='action',
            name='organism',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='helloasso.Organism'),
        ),
        migrations.AddField(
            model_name='action',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='helloasso.Payment'),
        ),
        migrations.AlterUniqueTogether(
            name='custominfo',
            unique_together={('action', 'label', 'value')},
        ),
    ]