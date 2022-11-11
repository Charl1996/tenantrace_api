# Generated by Django 4.1.3 on 2022-11-11 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.JSONField()),
                ('is_template', models.BooleanField(default=False)),
                ('owner_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='FormQuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('display', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationFormResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.JSONField()),
                ('application_form_configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.applicationformconfiguration')),
            ],
        ),
    ]