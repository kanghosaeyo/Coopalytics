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

# Admin creates a user (student/employer/advisor)
@users.route('/users', methods=['POST'])
def create_user():
    current_app.logger.info('POST /users route')

    b = request.json or {}
    user_id = b['userId']
    first_name = b['firstName']
    last_name = b['lastName']
    email = b['email']
    phone = b.get('phone')
    major = b.get('major')
    minor = b.get('minor')
    college = b.get('college')
    grad_year = b.get('gradYear')
    grade = b.get('grade')
    company_profile_id = b.get('companyProfileId')   
    industry = b.get('industry')
    demographic_id = b.get('demographicId')        

    query = '''
        INSERT INTO users
            (userId, firstName, lastName, demographicId, email, phone,
             major, minor, college, gradYear, grade, companyProfileId, industry)
        VALUES
            (%s, %s, %s, %s, %s, %s,
             %s, %s, %s, %s, %s, %s, %s);
    '''
    data = (user_id, first_name, last_name, demographic_id, email, phone,major, minor, college, grad_year, grade, company_profile_id, industry)

    cur = db.get_db().cursor()
    cur.execute(query, data)
    db.get_db().commit()
    return 'user created!', 201
