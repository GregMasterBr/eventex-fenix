# Generated by Django 4.2.1 on 2023-10-24 01:04

from django.db import migrations, models
import eventex.subscriptions.validators


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="cpf",
            field=models.CharField(
                max_length=11,
                validators=[eventex.subscriptions.validators.validate_cpf],
                verbose_name="CPF",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="criado em"),
        ),
    ]
