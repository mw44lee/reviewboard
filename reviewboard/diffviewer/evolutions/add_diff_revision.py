from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    AddField('FileDiff', 'diff_revision', models.CharField, initial='', max_length=512),
]
