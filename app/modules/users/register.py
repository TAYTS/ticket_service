from flask import request, jsonify, current_app
from werkzeug.security import generate_password_hash
import hashlib
from datetime import datetime
from sqlalchemy import exc

# Import database models
from models.db import db
from models.user import Users


def register():
    username = str(request.json.get("username"))
    password = str(request.json.get("password"))

    if not(username and password):
        return jsonify({"status": 0}), 400

    unhashed_user = "email: " + username + "ESC-Accenture"
    hashed_user = hashlib.sha512(unhashed_user.encode("UTF-8")).hexdigest()
    hashed_password = generate_password_hash(password)
    timestamp = datetime.utcnow()

    user = Users(
        id_user_hash=hashed_user,
        password=hashed_password,
        email=username,
        create_timestamp=timestamp
    )

    try:
        db.session.add(user)
        db.session.commit()
        status = 1
        return jsonify({"status": status}), 200
    except exc.IntegrityError:
        status = -1
        return jsonify({"status": status}), 409
    except Exception as e:
        current_app.logger.info('Failed to add new user: ' + str(e))
        status = 0
        return jsonify({"status": status}), 500