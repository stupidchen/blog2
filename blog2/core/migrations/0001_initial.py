# Generated by Django 2.0.3 on 2018-04-14 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('context', models.TextField()),
                ('author', models.CharField(max_length=128)),
                ('pubTime', models.DateTimeField()),
                ('editTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=128)),
                ('pubTime', models.DateTimeField()),
                ('context', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=64)),
                ('information', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='archive',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comment'),
        ),
    ]
