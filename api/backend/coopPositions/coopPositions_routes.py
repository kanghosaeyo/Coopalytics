from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coopPositions = Blueprint('coopPositions', __name__)

# Student/Advisor views the average pay for each industry
@coopPositions.route('/coopPositions/industryAveragePay', methods=['GET'])
def get_industry_average_pay():
    query = '''
        SELECT cp.industry, AVG(cp.hourlyPay) AS industryAvgHourlyPay
        FROM coopPositions cp
        GROUP BY cp.industry;
        '''
    
    current_app.logger.info('GET /coopPositions/industryAveragePay route')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


# Student view positions with desired skills that match their skills
@coopPositions.route('/<int:studentID>/coopPositions/desiredSkills', methods=['GET'])
def get_desired_skills(studentID):
    current_app.logger.info('GET /coopPositions/desiredSkills route')

    query = '''
        SELECT cp.coopPositionId,
            cp.title,
            cp.location,
            cp.description
        FROM coopPositions cp
            LEFT JOIN viewsPos vp ON cp.coopPositionId = vp.coopPositionId
            JOIN users u ON u.userId = {0}
        WHERE (vp.preference IS NULL OR vp.preference = TRUE)
            AND cp.desiredSkillsId IN (SELECT skillId
                                        FROM skillDetails
                                        WHERE studentId = {0})
            AND (cp.desiredGPA IS NULL OR cp.desiredGPA <= u.grade)
    '''.format(studentID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


# students view positions with required skills that match their skills 
@coopPositions.route('/<int:studentID>/coopPositions/requiredSkills', methods=['GET'])
def get_required_skills(studentID):
    current_app.logger.info('GET /coopPositions/requiredSkills route')

    query = '''
        SELECT cp.coopPositionId,
            cp.title,
            cp.location,
            cp.description
        FROM coopPositions cp
            LEFT JOIN viewsPos vp ON cp.coopPositionId = vp.coopPositionId
            JOIN users u ON u.userId = {0}
        WHERE (vp.preference IS NULL OR vp.preference = TRUE)
            AND cp.requiredSkillsId IN (SELECT skillId
                                        FROM skillDetails
                                        WHERE studentId = {0})
    '''.format(studentID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Employer posts co-op position
@coopPositions.route('/createsPos/coopPosition', methods=['POST'])
def create_position():
    current_app.logger.info('GET /createsPos/coopPosition')
    pos_info = request.json
    coop_position_id = pos_info['coopPositionId']
    title = pos_info['title']
    location = pos_info['locatoin']
    description = pos_info['description']
    hourly_pay = pos_info['hourlyPay']
    required_skills = pos_info['requiredSkills']
    desired_skills = pos_info['desiredSkills']
    desired_gpa = pos_info['desiredGPA']
    deadline = pos_info['deadline']
    start_date = pos_info['startDate']
    end_date = pos_info['endDate']
    flag = pos_info['flag']
    industry = pos_info['industry']

    query = '''
        INSERT INTO coopPositions
        VALUES (coopPositionId = %s,
        title = %s,
        location = %s,
        description = %s,
        hourlyPay = %s,
        requiredSkills = %s,
        desiredSkills = %s,
        desiredGPA = %s,
        deadline = %s,
        startDate = %s,
        endDate = %s,
        flag = %s,
        industry = %s,;

    '''
    data = (coop_position_id, title, location, description, hourly_pay,
            required_skills, desired_skills, desired_gpa, deadline,
            start_date, end_date, flag, industry)

    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'position created!'

