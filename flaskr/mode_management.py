from flask import Blueprint, jsonify, request
from flaskr.db import get_db
import json
import sqlite3

bp = Blueprint('mode_management', __name__)


@bp.route('/modes/<string:name>', methods=['GET'])
def get_mode(name):
    db = get_db()
    modes = db.execute(
        'SELECT json FROM mode where name = ?', [name]).fetchall()
    if len(modes) > 0:
        return jsonify(modes[0][0])
    return "", 404


@bp.route('/modes', methods=['GET'])
def get_modes():
    db = get_db()
    modes = db.execute('SELECT name FROM mode', []).fetchall()
    modes_list = [mode[0] for mode in modes]
    return jsonify(modes_list)


@bp.route('/modes/<string:name>', methods=['POST'])
def post_mode(name):
    if type(request.get_json()) is list:
        try:
            db = get_db()
            db.execute('INSERT INTO mode (name, json) VALUES(?, ?)',
                       [name, json.dumps(request.get_json())])
            db.commit()
            return jsonify({'result': 'success'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'result': 'already_exists'}), 422
    return "", 400


@bp.route('/modes/<string:name>', methods=['PUT'])
def put_mode(name):
    print("HI")
    print(type(request.get_json()))
    if type(request.get_json()) is list:
        db = get_db()
        results = db.execute('UPDATE mode SET json = ? WHERE name = ?'
                             'RETURNING *',
                             [json.dumps(request.get_json()), name]).fetchall()
        if len(results) < 1:
            return "", 404
        db.commit()
        return jsonify({'result': 'success'}), 201
    return "", 400
