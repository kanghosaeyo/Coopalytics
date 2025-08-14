from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coopPositions = Blueprint('coopPositions', __name__)

#Student views a co-op position
@coopPositions.route('/coopPositions', methods = ['GET'])
def get_position_info():
    current_app.logger.info('GET /coopPositions/industryAveragePay route')
    query = '''
        SELECT cp(*)
        FROM coopPositions cp
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


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
            JOIN users u ON u.userId = %s
        WHERE (vp.preference IS NULL OR vp.preference = TRUE)
            AND cp.desiredSkillsId IN (SELECT skillId
                                        FROM skillDetails
                                        WHERE studentId = %s)
            AND (cp.desiredGPA IS NULL OR cp.desiredGPA <= u.grade)
    '''

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
            JOIN users u ON u.userId = %s
        WHERE (vp.preference IS NULL OR vp.preference = TRUE)
            AND cp.requiredSkillsId IN (SELECT skillId
                                        FROM skillDetails
                                        WHERE studentId = %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


# Employer posts co-op position
@coopPositions.route('/createsPos/coopPosition', methods=['POST'])
def create_position():
    current_app.logger.info('POST /createsPos/coopPosition')
    pos_info = request.json
    coop_position_id = pos_info['coopPositionId'],
    title = pos_info['title'],
    location = pos_info['location'],
    description = pos_info['description'],
    hourly_pay = pos_info['hourlyPay'],
    required_skills = pos_info.get('requiredSkillsId'),
    desired_skills = pos_info.get('desiredSkillsId'),
    desired_gpa = pos_info.get('desiredGPA'),
    deadline = pos_info.get('deadline'),
    start_date = pos_info['startDate'],
    end_date = pos_info['endDate'],
    flag = pos_info.get('flagged', False),
    industry = pos_info['industry']

    query = '''
        INSERT INTO coopPositions
            (coopPositionId, title, location, description, hourlyPay, requiredSkillsId,
             desiredSkillsId, desiredGPA, deadline, startDate, endDate, flagged, industry)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    data = (coop_position_id, title, location, description, hourly_pay,
            required_skills, desired_skills, desired_gpa, deadline,start_date,
            end_date, flag, industry)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    return make_response(jsonify({"message": "Position created!"}), 201)



# Admin reviews positions before they go live 
@coopPositions.route('/pending', methods=['GET'])
def get_pending_positions():
    current_app.logger.info('GET /coopPositions/pending route')

    query = '''
        SELECT
            cp.coopPositionId,
            cp.title,
            cp.location,
            cp.description,
            cp.hourlyPay,
            cp.deadline,
            cp.startDate,
            cp.endDate,
            cp.industry,
            com.name AS companyName
        FROM coopPositions cp
        LEFT JOIN createsPos cr  ON cr.coopPositionId = cp.coopPositionId
        LEFT JOIN users u        ON u.userId = cr.employerId
        LEFT JOIN companyProfiles com ON com.companyProfileId = u.companyProfileId
        WHERE cp.flag = FALSE
        ORDER BY cp.deadline IS NULL, cp.deadline ASC, cp.coopPositionId DESC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Admin views number of co-ops posted by each employer
@coopPositions.route('/employerJobCounts', methods=['GET'])
def get_employer_job_counts():
    current_app.logger.info('GET /coopPositions/employerJobCounts route')

    query = '''
        SELECT
            u.userId AS employerId,
            u.firstName,
            u.lastName,
            com.name AS companyName,
            COUNT(cr.coopPositionId) AS numJobs
        FROM users u
        JOIN companyProfiles com
            ON com.companyProfileId = u.companyProfileId
        LEFT JOIN createsPos cr
            ON cr.employerId = u.userId
        WHERE u.companyProfileId IS NOT NULL 
        GROUP BY u.userId, u.firstName, u.lastName, com.name
        ORDER BY numJobs DESC, u.lastName ASC, u.firstName ASC;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Admin approves a co-op position 
@coopPositions.route('/coopPositions/<int:pos_id>/approve', methods=['PUT'])
def approve_position(pos_id):
    current_app.logger.info('PUT /coopPositions/%s/approve route', pos_id)

    query = '''
        UPDATE coopPositions
        SET flag = FALSE
        WHERE coopPositionId = %s AND flag = TRUE
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (pos_id,))
    if cursor.rowcount == 0:
        the_response = make_response(jsonify({"ok": False, "error": "not found or already approved"}))
        the_response.status_code = 409
        return the_response

    db.get_db().commit()
    the_response = make_response(jsonify({"ok": True, "positionId": pos_id, "status": "approved"}))
    the_response.status_code = 200
    return the_response

# Admin deletes an unapproved/invalid posting 
@coopPositions.route('/coopPositions/<int:pos_id>', methods=['DELETE'])
def delete_unapproved_position(pos_id):
    current_app.logger.info('DELETE /coopPositions/%s route', pos_id)

    query = '''
        DELETE FROM coopPositions
        WHERE coopPositionId = %s
          AND flag = TRUE
    '''

    cursor = db.get_db().cursor()
    try:
        cursor.execute(query, (pos_id,))
        if cursor.rowcount == 0:
            the_response = make_response(jsonify({
                "ok": False,
                "error": "not found or already approved"
            }))
            the_response.status_code = 409
            return the_response

        db.get_db().commit()
        the_response = make_response(jsonify({"ok": True, "positionId": pos_id, "deleted": True}))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        the_response = make_response(jsonify({
            "ok": False,
            "error": "cannot delete due to related records"
        }))
        the_response.status_code = 409
        return the_response
    
# Admin flags a position 
@coopPositions.route('/coopPositions/<int:pos_id>/flag/<int:value>', methods=['PUT'])
def set_position_flag(pos_id, value):
    current_app.logger.info('PUT /coopPositions/%s/flag/%s route', pos_id, value)

    query = '''
        UPDATE coopPositions
        SET flag = %s
        WHERE coopPositionId = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (value, pos_id))
    db.get_db().commit()

    the_response = make_response(jsonify({'message': 'flag updated!'}))
    the_response.status_code = 200
    return the_response

# Admin removes a flag from a position
@coopPositions.route('/coopPositions/<int:pos_id>/unflag', methods=['PUT'])
def unflag_position(pos_id):
    current_app.logger.info('PUT /coopPositions/%s/unflag route', pos_id)

    query = '''
        UPDATE coopPositions
        SET flag = FALSE
        WHERE coopPositionId = %s;
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (pos_id,))
    db.get_db().commit()

    the_response = make_response(jsonify({'message': 'flag removed!'}))
    the_response.status_code = 200
    return the_response

