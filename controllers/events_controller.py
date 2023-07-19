from flask import Blueprint, render_template, request
from models.events_list import events, add_new_event, remove_event
from models.event import Event

events_blueprint = Blueprint('events', __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title="Events", events=events)

@events_blueprint.route('/events', methods=["POST"])
def add_event():
    event_name = request.form['name']
    event_date = request.form['date']
    event_guests = request.form['guests']
    event_room = request.form['room']
    event_description = request.form['description']
    is_recurring_checked = request.form.get('recurring')
    
    new_event = Event(event_date, event_name, event_guests, event_room, event_description, is_recurring_checked)
    add_new_event(new_event)
    return render_template('index.jinja', title="Events", events=events)


@events_blueprint.route('/events/<index>/delete', methods=["POST"])
def remove_event_from_list(index):
    remove_event(int(index))
    return render_template('index.jinja', title="Events", events=events)

