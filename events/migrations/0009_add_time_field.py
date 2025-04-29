from django.db import migrations, models
from datetime import time

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_event_campus_alter_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=time(12, 0)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ] 