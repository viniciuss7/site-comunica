# Generated by Django 4.1.7 on 2023-12-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicasite', '0002_comentario_aprovado_alter_comentario_comentario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='\templates\\site\\img\\logo_and_text_color.svg')),
            ],
        ),
    ]
