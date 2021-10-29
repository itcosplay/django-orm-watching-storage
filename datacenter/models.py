from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format (
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

    def get_duration(self):
        entered_at = localtime(self.entered_at)
        
        if self.leaved_at == None:
            now = localtime()
        else:
            now = self.leaved_at

        delta = now - entered_at
        tot_seconds = delta.total_seconds()

        return tot_seconds

    def format_duration(self):
        duration = self.get_duration()

        hours = int(duration // 3600)
        minutes = int(duration % 3600 // 60)
        seconds = int(duration % 3600 % 60)

        return f'{hours}:{minutes}:{seconds}'

    def is_visit_long(self):
        duration = self.get_duration()

        return duration > 3600
