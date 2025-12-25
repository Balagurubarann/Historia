from src.models import Event
from flask import request, Blueprint, jsonify
from src.extension import db


# Setting blueprint for handling event route
event_bp = Blueprint("event", __name__, url_prefix="/api/event")

# Following code handles the event creation
@event_bp.route('/create', methods=['POST'])
def create_event():

    try:

        data = request.get_json()

        name = data["name"]
        description = data["description"]
        era=data["era"]

        if not name or not description or not era:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400

        # Check for any existing event with same name
        existingEvent = Event.query.filter_by(name=name).first()

        if existingEvent:

            return jsonify({
                "message": f"Event: {existingEvent.name} - Already Exists!",
                "success": False
            }), 409

        # Creating and saving new event
        event = Event(
            name=name,
            description=description,
            era=era
        )

        db.session.add(event)
        db.session.commit()

        return jsonify({
            "message": "Event added successfully",
            "success": True,
            "event": event.to_dict()
        }), 201

    except Exception as Ex:

        print("Error happened while creation: ", Ex)
        return jsonify({ "message": "Error happened while creation", "success": False }), 500
    

# Handling the event removal logic
@event_bp.route('/remove/<string:id>', methods=['DELETE'])
def remove_event(id: str):
    
    try:

        if not id:

            return jsonify({
                "message": "No ID found",
                "success": False
            }), 400

        event = Event.query.get(id)

        if not event:

            return jsonify({
                "message": "No event found",
                "success": False
            }), 404

        # Event Deletion
        db.session.delete(event)
        db.session.commit()

        return jsonify({
            "message": "Event deleted successfully",
            "success": True
        }), 200

    except Exception as Ex:

        print("Error happened while removing: ", Ex)
        return jsonify({ "message": "Error happened while removing", "success": False }), 500
    
    
# Fetching all events at once
@event_bp.route('/show-all', methods=['GET'])
def show_all_events():

    try:

        events = Event.query.all()

        if not events:

            return jsonify({
                "message": "No Events found",
                "success": False
            }), 404
        
        return jsonify({
            "message": "Events Fetched",
            "success": True,
            "events": [event.to_dict() for event in events]
        }), 200

    except Exception as Ex:

        print("Error happened while fetching: ", Ex)
        return jsonify({ "message": "Error happened while fetching", "success": False }), 500


# Fetching Event By ID 
@event_bp.route('/show-event/<string:id>', methods=['GET'])
def show_event_by_id(id: str):

    try:

        if not id:

            return jsonify({
                "message": "No ID found",
                "success": False
            }), 400

        event = Event.query.get(id)

        if not event:

            return jsonify({
                "message": "No event found",
                "success": False
            }), 404
        
        return jsonify({
            "message": "Event Fetched",
            "success": True,
            "events": event.to_dict()
        }), 200


    except Exception as Ex:

        print("Error happened while fetching: ", Ex)
        return jsonify({ "message": "Error happened while fetching", "success": False }), 500


# Handling logic to update event
@event_bp.route('/update/<string:id>', methods=['PUT'])
def update_event(id: str):

    try:

        data = request.get_json()

        name = data["name"]
        description = data["description"]
        era=data["era"]

        if not name or not description or not era:

            return jsonify({
                "message": "All fields are required",
                "success": False
            }), 400
        
        if not id:

            return jsonify({
                "message": "No ID found",
                "success": False
            }), 400

        event = Event.query.get(id)

        if not event:

            return jsonify({
                "message": "No event found",
                "success": False
            }), 404
        
        # Updating and Saving Event
        event.name = name
        event.description = description
        event.era = era

        db.session.commit()

        return jsonify({
            "message": "Event updated successfully",
            "success": True,
            "event": event.to_dict()
        }), 200

    except Exception as Ex:

        print("Error happened while fetching: ", Ex)
        return jsonify({ "message": "Error happened while fetching", "success": False }), 500