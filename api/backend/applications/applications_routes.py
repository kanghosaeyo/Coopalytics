from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

applications = Blueprint('applications', __name__)

# Advisor views application statuses for students
@applications.route('/applications', methods=['GET'])
def get_applications():
    advisor_id = request.args.get('advisorId')
    query = '''
        SELECT u.userId,
               u.firstName,
               u.lastName,
               a.applicationId,
               a.status    AS applicationStatus,
               cp.title    AS positionTitle,
               cp.deadline AS applicationDeadline,
               com.name    AS companyName
        FROM advisor_advisee aa
                 JOIN users u ON aa.studentId = u.userId
                 JOIN appliesToApp ata ON u.userId = ata.studentId
                 JOIN applications a ON ata.applicationId = a.applicationId
                 JOIN coopPositions cp ON a.coopPositionId = cp.coopPositionId
                 JOIN companyProfiles com ON cp.companyProfileId = com.companyProfileId
                 LEFT JOIN workedAtPos wp ON u.userId = wp.studentId AND wp.coopPositionId = cp.coopPositionId
        WHERE aa.advisorId = %s
        ORDER BY u.userId
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response