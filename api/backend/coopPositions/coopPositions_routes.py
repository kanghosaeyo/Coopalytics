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

# Admin reviews positions before they go live 
@coopPositions.route('/coopPositions/pending', methods=['GET'])
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
        WHERE cp.flagged = FALSE
        ORDER BY cp.deadline IS NULL, cp.deadline ASC, cp.coopPositionId DESC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Admin views number of co-ops posted by each employer
@coopPositions.route('/coopPositions/employerJobCounts', methods=['GET'])
def get_employer_job_counts():
    current_app.logger.info('GET /coopPositions/employerJobCounts route')

    query = '''
        SELECT
            u.userId AS employerId,
            u.firstName,
            u.lastName,
            cn AS companyName,
            COUNT(cr.coopPositionId) AS numJobs
        FROM users u
        JOIN companyProfiles com
          ON cn.companyProfileId = u.companyProfileId
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
        SET flagged = FALSE
        WHERE coopPositionId = %s AND flagged = TRUE
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
          AND flagged = TRUE
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