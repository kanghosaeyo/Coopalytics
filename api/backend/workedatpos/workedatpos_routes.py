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
workedAtPos = Blueprint('workedAtPos', __name__)

#------------------------------------------------------------
# Get all company profiles from the system
@workedAtPos.route('/workedatpos', methods=['GET'])
def get_companyRatings():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT com.name              AS companyName,
       AVG(cp.hourlyPay)     AS avgPay,
       AVG(wp.companyRating) AS avgCompanyRating,
       COUNT(*)              AS numPlacements
FROM workedAtPos wp
         JOIN coopPositions cp ON wp.coopPositionId = cp.coopPositionId
         JOIN companyProfiles com
              ON cp.coopPositionId IN (SELECT coopPositionId FROM createsPos WHERE employerId = com.companyProfileId)
GROUP BY com.name
HAVING avgCompanyRating >= 4
   AND avgPay >= 20
ORDER BY avgCompanyRating DESC, avgPay DESC;

    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response