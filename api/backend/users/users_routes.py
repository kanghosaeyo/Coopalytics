from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

users = Blueprint('users', __name__)

# Update student profiles to include additional info
@users.route('/users', methods=['PUT'])
def update_users():
    current_app.logger.info('PUT /users route')
    user_info = request.json
    user_id = user_info['userId']
    first_name = user_info['firstName']
    last_name = user_info['lastName']
    email = user_info['email']
    phone = user_info['phone']
    major = user_info['major']
    minor = user_info['minor']
    college = user_info['college']
    grad_year = user_info['gradYear']
    grade = user_info['grade']
    gender = user_info['gender']
    race = user_info['race']
    nationality = user_info['nationality']
    sexuality = user_info['sexuality']
    disability = user_info['disability']

    query = '''
        UPDATE users u
        JOIN demographics d ON u.userId = d.demographicId
        SET u.firstName = %s,
            u.lastName = %s,
            u.email = %s,
            u.phone = %s,
            u.major = %s,
            u.minor = %s,
            u.college = %s,
            u.gradYear = %s,
            u.grade = %s,
            d.gender = %s,
            d.race = %s,
            d.nationality = %s,
            d.sexuality = %s,
            d.disability = %s
        WHERE u.userId = %s;'''
    data = (first_name, last_name, email, phone, major, minor, college, grad_year, grade, gender, race, nationality, sexuality, disability, user_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'user updated!'
