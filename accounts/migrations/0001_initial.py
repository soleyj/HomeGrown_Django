# Generated by Django 2.2.5 on 2019-10-01 11:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date', models.DateTimeField()),
                ('owner', models.ManyToManyField(related_name='test', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]