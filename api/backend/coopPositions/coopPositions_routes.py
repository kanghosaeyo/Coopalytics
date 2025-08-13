
########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
coopPositions = Blueprint('coopPositions', __name__)

#------------------------------------------------------------
# Get all company profiles from the system
@coopPositions.route('/coopPositions', methods=['GET'])
def get_coopPosWageData():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT cp.name AS companyName,
       pos.title AS positionTitle,
       MIN(pos.hourlyPay) AS minSalary,
       MAX(pos.hourlyPay) AS maxSalary,
       AVG(w.companyRating) AS avgRating,
       COUNT(w.studentId) AS numPreviousCoops
FROM companyProfiles cp JOIN users u ON cp.companyProfileId = u.companyProfileId
    JOIN createsPos cr ON u.userId = cr.employerId
    JOIN coopPositions pos ON cr.coopPositionId = pos.coopPositionId
    LEFT JOIN workedAtPos w ON pos.coopPositionId = w.coopPositionId
GROUP BY cp.name, pos.title;
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
