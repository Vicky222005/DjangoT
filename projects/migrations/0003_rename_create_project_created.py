# Generated by Django 4.1.2 on 2022-11-10 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='create',
            new_name='created',
        ),
    ]
