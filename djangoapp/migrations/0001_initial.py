# Generated by Django 3.1 on 2022-02-10 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regNo', models.IntegerField()),
                ('firstName', models.CharField(max_length=30)),
                ('middleName', models.CharField(max_length=30)),
                ('sirName', models.CharField(max_length=30)),
                ('profileImage', models.ImageField(default=0, upload_to='images/')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
