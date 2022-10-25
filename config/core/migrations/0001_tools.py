# Generated by Django 4.1.2 on 2022-10-25 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('code_box', models.CharField(max_length=24, unique=True, verbose_name='code')),
                ('description', models.TextField(max_length=64, verbose_name='description')),
                ('is_empty', models.BooleanField(default=False, verbose_name='empty')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('code_material', models.CharField(max_length=64, unique=True, verbose_name='code')),
                ('description', models.TextField(max_length=64, verbose_name='description')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Appontment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='log_box', to='core.box', verbose_name='box')),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='log_material', to='core.material', verbose_name='material')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
