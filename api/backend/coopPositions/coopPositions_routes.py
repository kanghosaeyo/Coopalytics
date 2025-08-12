from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

coopPositions = Blueprint('coopPositions', __name__)

# Student/Advisor views the average pay for each industry
@coopPositions.route('/coopPositions/<industryAveragePay>', methods=['GET'])
def get_industry_average_pay(industryAveragePay):
    query = '''
        SELECT cp.industry, AVG(cp.hourlyPay) AS industryAvgHourlyPay
        FROM coopPositions cp
        GROUP BY cp.industry;
        '''.format(industryAveragePay)
    
    current_app.logger.info('GET /coopPositions/<industryAveragePay> route')

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response