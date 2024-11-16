# Generated by Django 3.1.3 on 2024-10-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=159)),
                ('name', models.CharField(max_length=159)),
                ('email', models.CharField(max_length=159)),
                ('category', models.CharField(choices=[('Technical', 'Technical'), ('Behavioral', 'Behavioral')], max_length=50)),
                ('subject', models.CharField(max_length=159)),
                ('date_time', models.CharField(max_length=159)),
                ('result', models.CharField(max_length=159)),
            ],
        ),
        migrations.CreateModel(
            name='examdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=159)),
                ('qid', models.CharField(max_length=159)),
                ('question', models.TextField()),
                ('faceexp', models.CharField(max_length=159)),
                ('sc1', models.CharField(max_length=159)),
                ('answer', models.CharField(max_length=159)),
                ('sc2_g', models.CharField(max_length=159)),
                ('sc3_m', models.CharField(max_length=159)),
            ],
        ),
        migrations.CreateModel(
            name='q_a_dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Technical', 'Technical'), ('Behavioral', 'Behavioral')], default='Technical', max_length=20)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=159)),
                ('email', models.CharField(max_length=159)),
                ('pass_word', models.CharField(max_length=159)),
                ('phone', models.CharField(max_length=159)),
                ('city', models.CharField(max_length=159)),
                ('gender', models.CharField(max_length=159)),
                ('age', models.CharField(max_length=159)),
            ],
        ),
    ]