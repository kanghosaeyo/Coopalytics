from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# New Blueprint for applications
views_position = Blueprint('views_position', __name__)

# student flags positions they like/do not like 
@views_position.route('/views_position', methods=['POST'])
def set_job_preference():
    the_data = request.json
    current_app.logger.info(the_data)
    
    student_id = the_data['studentId']
    coop_position_id = the_data['coopPositionId']
    preference = the_data['preference']  
    
    query = f'''
        INSERT INTO viewsPos (studentId, coopPositionId, preference)
        VALUES ({student_id}, {coop_position_id}, {int(preference)})
        ON DUPLICATE KEY UPDATE preference = VALUES(preference)
    '''
    current_app.logger.info(query)
    
    # Execute query and commit
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    # Return success response
    response = make_response("Preference saved successfully")
    response.status_code = 200
    return response


# Student views deadlines for positions
@views_position.route('/views_position/<studentID>/deadlines', methods=['GET'])
def get_deadlines(studentID):
    current_app.logger.info('GET /views_position/deadlines route')

    query = '''
        SELECT cp.title,
            cp.deadline
        FROM viewsPos vp
            JOIN coopPositions cp ON vp.coopPositionId = cp.coopPositionId
        WHERE vp.studentId = {0} AND vp.preference = TRUE;
    '''.format(studentID)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
    

    