# Generated by Django 3.1 on 2020-08-23 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rms_core', '0002_recipes_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(blank=True, null=True, verbose_name='date added')),
                ('instructions', models.CharField(blank=True, default='', max_length=200)),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('serves', models.IntegerField()),
                ('prep_time', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('seasonality', models.CharField(blank=True, default='', max_length=200)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RecipeInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_date', models.DateTimeField(blank=True, null=True, verbose_name='date made')),
                ('comments', models.CharField(blank=True, default='', max_length=200)),
                ('changes', models.CharField(blank=True, default='todo', max_length=200)),
                ('rating', models.IntegerField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rms_core.recipe')),
            ],
        ),
        migrations.RenameModel(
            old_name='Supplies',
            new_name='Supply',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='pantry',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date expires'),
        ),
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.DeleteModel(
            name='RecipeInstances',
        ),
        migrations.DeleteModel(
            name='Recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='rms_core.Ingredient'),
        ),
    ]
