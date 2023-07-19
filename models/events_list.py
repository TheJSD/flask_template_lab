from models.event import Event
import datetime
# (date, name, guests, room_location, description)
event1 = Event(datetime.date(2023, 8, 28), "Good Party", 20, "room 1", "this is a good party", True)

event2 = Event(datetime.date(2023, 9, 12), "New Party", 25, "room 2", "this is another good party", False)


events = [event1, event2]

def add_new_event(event):
    events.append(event)

def remove_event(event_index):
    del events[event_index]