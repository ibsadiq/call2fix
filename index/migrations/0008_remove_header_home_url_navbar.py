# Generated by Django 4.2.2 on 2023-06-24 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('index', '0007_alter_header_contact_alter_header_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='home_url',
        ),
        migrations.CreateModel(
            name='NavBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_url', models.URLField(null=True)),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
            ],
        ),
    ]