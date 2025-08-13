from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

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

# Employer views student profile
@users.route('/applications/appliesToApp/<studentId>/users', methods=['GET'])
def view_users():
    current_app.logger.info('GET /applications/appliesToApp/<studentId>/users')
    user_info = request.json
    application_info = request.json
    user_id = user_info['userId']
    first_name = user_info['firstName']
    last_name = user_info['lastName']
    email = user_info['email']
    major = user_info['major']
    minor = user_info['minor']
    college = user_info['college']
    grade = user_info['grade']
    grad_year = user_info['gradYear']
    gpa = application_info['gpa']
    resume = application_info['resume']
    cover_letter = application_info['coverLetter']


    query = '''
        SELECT u.userId, u.firstName, u.lastName, u.email, u.major,
       u.minor, u.college, u.grade, u.gradYear, a.gpa,
       a.resume, a.coverLetter
       FROM users u JOIN applications a;'''
    data = (first_name, last_name, email, major, minor, college, grad_year, grade, user_id,
            gpa, resume, cover_letter)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()


    theData = cursor.fetchall()
   
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Employer filters student profiles
@users.route('/applications/appliesToApp/<studentId>/users', methods=['GET'])
def view_users():
    current_app.logger.info('GET /applications/appliesToApp/<studentId>/users')
    user_info = request.json
    skill_info = request.json
    user_id = user_info['userId']
    first_name = user_info['firstName']
    last_name = user_info['lastName']
    name = skill_info['name']

    query = '''
        SELECT u.userId, u.firstName, u.lastName
        FROM users u JOIN skillDetails sd
        ON u.userId = sd.studentId
        JOIN skills s
        ON sd.skillId = s.skillId
        WHERE s.name = %s
        OR s.name = %s
        OR s.name = %s
        AND u.gradYear = %s
        AND u.major = %s;'''
    data = (first_name, last_name, name, name, name)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()

    theData = cursor.fetchall()
   
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response