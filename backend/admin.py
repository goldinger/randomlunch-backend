from django.contrib import admin
from backend.models import Person, Location, Session, Couple, Client, PossibleSession, PossibleCouple

admin.site.register(Person)
admin.site.register(Location)
admin.site.register(Session)
admin.site.register(Couple)
admin.site.register(Client)
admin.site.register(PossibleSession)
admin.site.register(PossibleCouple)
