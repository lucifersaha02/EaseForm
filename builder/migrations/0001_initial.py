# Generated by Django 3.2.6 on 2021-08-26 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('character_field', models.BooleanField(default=False)),
                ('big_text_field', models.BooleanField(default=False)),
                ('integer_field', models.BooleanField(default=False)),
                ('file_field', models.BooleanField(default=False)),
                ('mcq_field', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FormObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MCQField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.TextField(blank=True)),
                ('field_data', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('type_of', models.CharField(default='Single', max_length=30)),
                ('form_design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formdesign')),
                ('form_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formobject')),
            ],
        ),
        migrations.CreateModel(
            name='FormParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('accept_responses', models.BooleanField(default=True)),
                ('banner_img', models.ImageField(blank=True, default='banner.png', null=True, upload_to='banners')),
                ('builder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.profile')),
            ],
        ),
        migrations.AddField(
            model_name='formobject',
            name='applicant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='builder.profile'),
        ),
        migrations.AddField(
            model_name='formobject',
            name='form_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formparent'),
        ),
        migrations.CreateModel(
            name='FormIntegerField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.TextField(blank=True)),
                ('field_data', models.BigIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('type_of', models.CharField(default='int', max_length=30)),
                ('form_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formobject')),
            ],
        ),
        migrations.CreateModel(
            name='FormFileField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.TextField(blank=True)),
                ('field_data', models.FileField(upload_to='fileData')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('type_of', models.CharField(default='file', max_length=30)),
                ('form_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formobject')),
            ],
        ),
        migrations.AddField(
            model_name='formdesign',
            name='form_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formparent'),
        ),
        migrations.CreateModel(
            name='FormCharacterField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.TextField(blank=True)),
                ('field_data', models.CharField(max_length=400)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('type_of', models.CharField(default='char', max_length=30)),
                ('form_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formobject')),
            ],
        ),
        migrations.CreateModel(
            name='FormBigTextField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_name', models.TextField(blank=True)),
                ('field_data', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('type_of', models.CharField(default='txt', max_length=30)),
                ('form_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formobject')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mcq_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.formdesign')),
            ],
        ),
    ]