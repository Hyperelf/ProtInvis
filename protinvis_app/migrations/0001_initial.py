# Generated by Django 2.2.6 on 2019-10-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProtInvis_Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniprot_id', models.CharField(max_length=1000)),
                ('the_dye', models.CharField(choices=[('Кумасси бриллиантовый синий', 'Кумасси бриллиантовый синий'), ('Окрашивание серебром', 'Окрашивание серебром'), ('Амидо черный', 'Амидо черный'), ('Бромфеноловый синий', 'Бромфеноловый синий'), ('Пирогаллоловый красный', 'Пирогаллоловый красный'), ('Sypro Ruby', 'Sypro Ruby'), ('Stain-free', 'Stain-free'), ('Zn-имидазольное негативное окрашивание', 'Zn-имидазольное негативное окрашивание')], max_length=50)),
                ('use_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
