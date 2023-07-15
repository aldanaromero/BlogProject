# Generated by Django 4.2.3 on 2023-07-14 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('description', models.TextField(blank=True, null=True)),
                ('link', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('subtitle', models.CharField(max_length=30)),
                ('body', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
