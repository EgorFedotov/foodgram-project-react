# Generated by Django 4.2.1 on 2023-06-07 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientamount',
            name='ingredient',
            field=models.ForeignKey(help_text='Ингредиент', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='recipes.ingredient', verbose_name='Ингредиент'),
        ),
        migrations.AlterField(
            model_name='ingredientamount',
            name='recipe',
            field=models.ForeignKey(help_text='Рецепт', on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
