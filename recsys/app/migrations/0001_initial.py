# Generated by Django 2.2.5 on 2019-09-26 18:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('recommendation_index', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(default=2019)),
                ('synopsis', models.TextField(blank=True, null=True)),
                ('recommendation_index', models.DecimalField(decimal_places=3, default=0, max_digits=4)),
                ('showing_until', models.DateField(default=datetime.date.today)),
                ('genre', models.ManyToManyField(to='app.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, unique=True)),
                ('tags', models.ManyToManyField(to='app.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='OLifer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=40, unique=True)),
                ('answers', models.ManyToManyField(blank=True, null=True, to='app.Answer')),
                ('cluster', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.UserCluster')),
                ('saved_events', models.ManyToManyField(to='app.Event')),
                ('saved_movies', models.ManyToManyField(to='app.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.OLifer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
        ),
    ]
