from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# New Blueprint for applications
applications = Blueprint('applications', __name__)


# Student viewing their own application statuses
@applications.route('/student/<studentID>/applications', methods=['GET'])
def get_student_applications(studentID):
    current_app.logger.info('GET /student/<userID>/applications route')
    
    query = '''
        SELECT u.userId,
               u.firstName,
               u.lastName,
               a.applicationId,
               a.status    AS applicationStatus,
               cp.title    AS positionTitle,
               cp.deadline AS applicationDeadline,
               com.name    AS companyName,
               a.dateApplied,
               cp.description AS positionDescription
        FROM users u
                 JOIN appliesToApp ata ON u.userId = ata.studentId
                 JOIN applications a ON ata.applicationId = a.applicationId
                 JOIN coopPositions cp ON a.coopPositionId = cp.coopPositionId
                 JOIN companyProfiles com ON cp.companyProfileId = com.companyProfileId
        WHERE u.userId = {0}
        ORDER BY a.dateApplied DESC, cp.deadline ASC
    '''.format(studentID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# student sees how many positions they have applied to
@applications.route('/student/<studentID>/applications/summary', methods=['GET'])
def get_student_applications(studentID):
    current_app.logger.info('GET /student/<studentID>/applications route')
    
    query = '''
        SELECT a.status, 
            COUNT(*) AS ApplicationCount
        FROM applications a
            JOIN appliesToApp ata ON a.applicationId = ata.applicationId
        WHERE ata.studentId = {0}
        GROUP BY a.status

    '''.format(studentID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response



# Advisor viewing all their advisees' application statuses
@applications.route('/advisor/<advisorID>/students/applications', methods=['GET'])
def get_advisor_student_applications(advisorID):
    current_app.logger.info('GET /advisor/<advisorID>/students/applications route')
    
    query = '''
        SELECT aa.advisorId,
               u.userId,
               u.firstName,
               u.lastName,
               a.applicationId,
               a.status    AS applicationStatus,
               cp.title    AS positionTitle,
               cp.deadline AS applicationDeadline,
               com.name    AS companyName,
               a.dateApplied
        FROM advisor_advisee aa
                 JOIN users u ON aa.studentId = u.userId
                 JOIN appliesToApp ata ON u.userId = ata.studentId
                 JOIN applications a ON ata.applicationId = a.applicationId
                 JOIN coopPositions cp ON a.coopPositionId = cp.coopPositionId
                 JOIN companyProfiles com ON cp.companyProfileId = com.companyProfileId
                 LEFT JOIN workedAtPos wp ON u.userId = wp.studentId AND wp.coopPositionId = cp.coopPositionId
        WHERE aa.advisorId = {0}
        ORDER BY u.lastName, u.firstName, a.dateApplied DESC
    '''.format(advisorID)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response