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
        WHERE u.userId = %s
        ORDER BY a.dateApplied DESC, cp.deadline ASC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# student sees how many positions they have applied to
@applications.route('/student/<studentID>/applications/summary', methods=['GET'])
def get_numb_apps(studentID):
    current_app.logger.info('GET /student/<studentID>/applications route')
    
    query = '''
        SELECT a.status, 
            COUNT(*) AS ApplicationCount
        FROM applications a
            JOIN appliesToApp ata ON a.applicationId = ata.applicationId
        WHERE ata.studentId = %s
        GROUP BY a.status

    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (studentID,))
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

# Employer views all applications of a posting
@applications.route('/applications/<int:coopPositionId>', methods=['GET'])
def get_applications(coopPositionId):
    current_app.logger.info('GET /applications/%s', coopPositionId)

    query = '''
        SELECT a.dateTimeApplied, a.status, a.resume, a.gpa, a.coverLetter,
               a.coopPositionId, a.applicationId
        FROM applications a
        JOIN coopPositions cp ON a.coopPositionId = cp.coopPositionId
        WHERE a.coopPositionId = %s
        ORDER BY a.dateTimeApplied DESC;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (coopPositionId,))
    theData = cursor.fetchall()

    return make_response(jsonify(theData), 200)

# NEW ENDPOINT: Employer views all applications with student details for a specific position
@applications.route('/applications/<int:coopPositionId>/with-students', methods=['GET'])
def get_applications_with_students(coopPositionId):
    current_app.logger.info('GET /applications/%s/with-students', coopPositionId)

    query = '''
        SELECT a.dateTimeApplied, a.status, a.resume, a.gpa, a.coverLetter,
               a.coopPositionId, a.applicationId,
               u.userId as studentId, u.firstName, u.lastName, u.email,
               u.major, u.minor, u.college, u.gradYear, u.grade
        FROM applications a
        JOIN appliesToApp ata ON a.applicationId = ata.applicationId
        JOIN users u ON ata.studentId = u.userId
        JOIN coopPositions cp ON a.coopPositionId = cp.coopPositionId
        WHERE a.coopPositionId = %s
        ORDER BY a.dateTimeApplied DESC;
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (coopPositionId,))
    theData = cursor.fetchall()

    return make_response(jsonify(theData), 200)

# NEW ENDPOINT: Update application status (for employers)
@applications.route('/applications/<int:applicationId>/status', methods=['PUT'])
def update_application_status(applicationId):
    current_app.logger.info('PUT /applications/%s/status', applicationId)

    try:
        request_data = request.json
        new_status = request_data.get('status')

        if not new_status:
            return make_response(jsonify({"error": "Status is required"}), 400)

        # Validate status values
        valid_statuses = ['Draft', 'Submitted', 'Under Review', 'Accepted', 'Rejected']
        if new_status not in valid_statuses:
            return make_response(jsonify({"error": "Invalid status"}), 400)

        query = '''
            UPDATE applications
            SET status = %s
            WHERE applicationId = %s
        '''

        cursor = db.get_db().cursor()
        cursor.execute(query, (new_status, applicationId))

        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Application not found"}), 404)

        db.get_db().commit()

        return make_response(jsonify({
            "success": True,
            "applicationId": applicationId,
            "newStatus": new_status
        }), 200)

    except Exception as e:
        current_app.logger.error(f"Error updating application status: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)

# Student applies to a position
@applications.route('/users/appliesToApp/applications', methods=['POST'])
def create_application():
     current_app.logger.info('GET /applications')
     application_info = request.json
     datetime_applied = application_info['dateTimeApplied']
     status = application_info['status']
     resume = application_info['resume']
     gpa = application_info['gpa']
     cover_letter = application_info['coverLetter']
     coop_position_id = application_info['coopPositionId']
     application_id = application_info['applicationId']


     query = '''
INSERT INTO applications
VALUES (dateTimeApplied = %s,
        status = %s,
        resume = %s,
        gpa = %s,
        coverLetter = %s,
        coopPositionId = %s,
        applicationId = %s);
        '''
     data = (datetime_applied, status, resume, gpa, cover_letter,
             coop_position_id, application_id)
     
     cursor = db.get_db().cursor()
     r = cursor.execute(query, data)
     db.get_db().commit()
     return 'application submitted!'

