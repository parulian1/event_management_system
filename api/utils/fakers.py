from random import randint

import factory
from factory import fuzzy
from django.contrib.auth import get_user_model

from api.session_management.models import Event, Session
from api.track.models import Venue, Track
from api.users.models import Profile, Speaker


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('safe_email')
    password = factory.Faker('password')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = get_user_model()


class UserProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    birth_place = factory.Faker('city')
    birth_date = factory.Faker('date')
    gender = fuzzy.FuzzyChoice([x[0] for x in Profile.Gender.choices])
    occupation  = factory.Faker('job')
    marital_status = fuzzy.FuzzyChoice([x[0] for x in Profile.MaritalStatus.choices])

    class Meta:
        model = Profile


class VenueFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    location = factory.Faker('city')
    description = factory.Faker('text')
    is_available = True

    class Meta:
        model = Venue


class TrackFactory(factory.django.DjangoModelFactory):
    venue = factory.SubFactory(VenueFactory)
    name = factory.Faker('name')
    description = factory.Faker('text')
    is_available = True
    capacity = factory.Faker('random_int', min=10, max=100)

    class Meta:
        model = Track


class EventFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('text')
    track = factory.SubFactory(TrackFactory)
    date = factory.Faker('date')
    start_time = factory.Faker('time')
    end_time = factory.Faker('time')
    capacity = factory.LazyAttribute(lambda obj: obj.track.capacity - randint(0, 10))

    class Meta:
        model = Event


class SpeakerFactory(factory.django.DjangoModelFactory):
    profile = factory.SubFactory(UserProfileFactory)
    role = fuzzy.FuzzyChoice([x[0] for x in Speaker.Responsibility.choices])

    class Meta:
        model = Speaker


class SessionFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Session

    @factory.post_generation
    def create_events(self, create, extracted, **kwargs):
        if not create:
            return
        if not extracted:
            if not Event.objects.exists():
                self.events.add(EventFactory())
            else:
                for event in Event.objects.all()[0:randint(1, Event.objects.count())]:
                    self.events.add(event)
        else:
            for p in extracted:
                self.events.add(p)

    @factory.post_generation
    def create_speakers(self, create, extracted, **kwargs):
        if not create:
            return
        if not extracted:
            if not Speaker.objects.exists():
                self.speakers.add(SpeakerFactory())
            else:
                for speaker in Speaker.objects.all()[0:randint(1, Speaker.objects.count())]:
                    self.speakers.add(speaker)
        else:
            for p in extracted:
                self.speakers.add(p)
