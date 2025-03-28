from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]