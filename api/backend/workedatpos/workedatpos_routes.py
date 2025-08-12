from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

workedatpos = Blueprint('workedatpos', __name__)

# Advisor views historical placement data for all students (filter by major/industry in frontend)
@workedatpos.route('/workedatpos/placement-data', methods=['GET'])
def get_scatter_plot_data():
    current_app.logger.info('GET /workedatpos/placement-data route')
    
    query = '''
        SELECT u.major,
               cp.industry,
               a.gpa,
               cp.hourlyPay,
               wp.studentId AS wasHired,
               u.firstName,
               u.lastName,
               cp.title AS positionTitle,
               comp.name AS companyName,
               u.college,
               u.gradYear,
               cp.location
        FROM users u
                 JOIN appliesToApp ata ON u.userId = ata.studentId
                 JOIN applications a ON ata.applicationId = a.applicationId
                 JOIN coopPositions cp ON a.coopPositionId = cp.coopPositionId
                 JOIN companyProfiles comp ON cp.industry = comp.industry
                 LEFT JOIN workedAtPos wp ON u.userId = wp.studentId AND wp.coopPositionId = cp.coopPositionId
        WHERE a.gpa IS NOT NULL 
          AND cp.hourlyPay IS NOT NULL
        ORDER BY u.major, cp.industry, a.gpa DESC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Advisor and student views company rating data rated by past co-ops
@workedatpos.route('/workedatpos/company-ratings', methods=['GET'])
def get_company_ratings():
    current_app.logger.info('GET /workedatpos/company-ratings route')
    
    query = '''
        SELECT comp.name AS companyName, 
            comp.companyProfileId,
            AVG(wp.companyRating) AS avgRating,
            COUNT(wp.companyRating) AS totalRatings,
            MIN(wp.companyRating) AS minRating,
            MAX(wp.companyRating) AS maxRating,
            COUNT(DISTINCT wp.studentId) AS studentsWhoRated
        FROM companyProfiles comp
            JOIN users employer ON comp.companyProfileId = employer.companyProfileId
            JOIN createsPos cp_link ON employer.userId = cp_link.employerId
            JOIN coopPositions cp ON cp_link.coopPositionId = cp.coopPositionId
            JOIN workedAtPos wp ON cp.coopPositionId = wp.coopPositionId
        WHERE wp.companyRating IS NOT NULL
        GROUP BY comp.companyProfileId, comp.name
        ORDER BY avgRating DESC;
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


