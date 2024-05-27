#!/usr/bin/python3
"""
Flask app_view
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def api_status():
    """
    status
    """
    response = {'status': "OK"}
    return jsonify(response)


@app_views.route('/stats')
def get_stats():
    """
<<<<<<< HEAD
    get stats
=======
    gets stats
>>>>>>> ae29bec954e0be12bf07f8fe9e5ec00abb0cb362
    """
    stats = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'reviews': storage.count('Reviw'),
            'states': storage.count('State'),
            'users': storage.count('User'),
            }
    return jsonify(stats)
