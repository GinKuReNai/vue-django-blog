# Generated by Django 2.2.28 on 2022-06-23 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=True, related_name='children', to='blog.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'parent')},
        ),
    ]
