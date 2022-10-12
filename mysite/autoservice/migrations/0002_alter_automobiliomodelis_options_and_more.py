# Generated by Django 4.1.1 on 2022-10-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automobiliomodelis',
            options={'verbose_name': 'Automobilio modelis', 'verbose_name_plural': 'Automobilio modeliai'},
        ),
        migrations.AlterModelOptions(
            name='automobilis',
            options={'verbose_name': 'Automobilis', 'verbose_name_plural': 'Automobiliai'},
        ),
        migrations.AlterModelOptions(
            name='paslauga',
            options={'verbose_name': 'Paslauga', 'verbose_name_plural': 'Paslaugos'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymas',
            options={'verbose_name': 'Užsakymas', 'verbose_name_plural': 'Užsakymai'},
        ),
        migrations.AlterModelOptions(
            name='uzsakymoeilute',
            options={'verbose_name': 'Užsakyta paslauga', 'verbose_name_plural': 'Užsakytos paslaugos'},
        ),
        migrations.AddField(
            model_name='uzsakymas',
            name='statusas',
            field=models.CharField(choices=[('p', 'Patvirtinta'), ('v', 'Vykdoma'), ('i', 'Įvykdyta'), ('a', 'Atšaukta')], default='p', help_text='Statusas', max_length=1),
        ),
        migrations.AlterField(
            model_name='uzsakymas',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
    ]