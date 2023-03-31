# Generated by Django 4.1.7 on 2023-03-31 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_cor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(default=0, null=True)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garagem.categoria')),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garagem.cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garagem.marca')),
            ],
        ),
        migrations.DeleteModel(
            name='Acessorios',
        ),
    ]
