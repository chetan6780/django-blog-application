# Generated by Django 3.1.7 on 2021-03-31 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_auther'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
    ]
