from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# New Blueprint for applications
applications = Blueprint('applications', __name__)


# student views status of submitted applications 
@applications.route('/applications/<id>', methods=['GET'])
def get_app_status(id):

    query = f'''SELECT a.applicationId,
                       cp.title AS positionTitle,
                       c.name AS companyName,
                       a.status,
                       a.dateTimeApplied
                FROM applications a
                JOIN appliesToApp ata ON a.applicationId = ata.applicationId
                JOIN coopPositions cp ON a.coopPositionId = cp.coopPositionId
                JOIN createsPos crp ON cp.coopPositionId = crp.coopPositionId
                JOIN users u ON crp.employerId = u.userId
                JOIN companyProfiles c ON u.companyProfileId = c.companyProfileId
                WHERE ata.studentId = {str(id)}
    '''

    current_app.logger.info(f'GET /applications/<id> query={query}')

    # db connection
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    current_app.logger.info(f'GET /applicaitons/<id> Result of query = {theData}')

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
    
