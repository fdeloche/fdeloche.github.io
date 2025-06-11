# -*- coding: utf-8 -*-
from datetime import datetime


class Event:

    def __init__(self, title, when):
        """An event.

        :param title: A String. The title of the event.
        :param when: A datetime object. The date and time of the event.
        """
        self.title = title
        self.when = when

    def change_time(self, new_time):
        """Change the time of the event.

        :param new_time: A datetime object. The new date and time.
        """
        self.when = new_time

lesson = Event("Swimming lesson", datetime(2016, 12, 15, 17, 00))
print(lesson.title)
lesson.change_time(datetime(2016, 12, 16, 17, 30))


class Appointment(Event):

    def __init__(self, title, when, with_whom):
        """An appointment.

        :param title: A String. The title of the event.
        :param when: A datetime object. The date and time of the event.
        :param with_whom: A String. The person with whom the appointment is.
        """
        super().__init__(title, when)
        self.with_whom = with_whom

lunch = Appointment(title="Restaurant", with_whom="Donald",
                    when=datetime(2015, 12, 25, 12, 0))
lunch.change_time(datetime(2015, 12, 25, 12, 30))


class Calendar:
    def __init__(self, event_list=None, owner=""):
        """A calendar.

        :param event_list: A list of Event objects.
        :param owner: A String. The owner of the agenda.
        """
        self.owner = owner
        if not event_list:
            self.event_list = []
        else:
            self.event_list = event_list

calendar = Calendar(owner="Daisy",
                    event_list=[lesson, lunch])
print("")
print(calendar.event_list[1].title)
print(calendar.event_list[1].when)
print(calendar.event_list[1].with_whom)