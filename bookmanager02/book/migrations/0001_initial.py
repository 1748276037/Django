# Generated by Django 2.2.5 on 2020-08-15 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('pub_date', models.DateField(null=True)),
                ('readcount', models.IntegerField(default=0)),
                ('commentcount', models.IntegerField(default=0)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Admin站点里显示',
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.SmallIntegerField(choices=[(1, 'female'), (0, 'male')], default=0)),
                ('description', models.CharField(max_length=100)),
                ('is_delete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo')),
            ],
            options={
                'verbose_name': 'Admin站点里显示',
                'db_table': 'peopleinfo',
            },
        ),
    ]
