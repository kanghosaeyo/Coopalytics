from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

companyProfiles = Blueprint('companyProfiles', __name__)

# Student/Advisor views a company profile
@companyProfiles.route('/companyProfiles/<companyProfileId>', methods=['GET'])
def get_company_profile(companyProfileId):
    query = '''
        SELECT companyProfileId, name, bio, industry, websiteLink
        FROM companyProfiles
        WHERE companyProfileId = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (companyProfileId,))
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Advisor views all company profiles
@companyProfiles.route('/companyProfiles', methods=['GET'])
def get_all_company_profiles():
    query = '''
        SELECT companyProfileId, name, bio, industry, websiteLink
        FROM companyProfiles
        ORDER BY name
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# # Advisor views all company profiles sorted by their rating
# @companyProfiles.route('/companyProfiles/rating', methods=['GET'])
# def get_company_profiles_by_rating():
#     query = '''
#             SELECT com.name AS companyName,
#                    com.industry AS companyIndustry,
#                    com.websiteLink AS companyWebsite,
#                    AVG(wp.companyRating) AS avgCompanyRating,
#                    COUNT(wp.companyRating) AS ratingCount
#             FROM workedAtPos wp
#             JOIN coopPositions cp ON wp.coopPositionId = cp.coopPositionId
#             JOIN createsPos cr ON cp.coopPositionId = cr.coopPositionId
#             JOIN users u ON cr.employerId = u.userId
#             JOIN companyProfiles com ON u.companyProfileId = com.companyProfileId
#             WHERE wp.companyRating IS NOT NULL
#             GROUP BY com.name, com.industry, com.websiteLink
#             HAVING COUNT(wp.companyRating) > 0
#             ORDER BY avgCompanyRating DESC;
#     '''    
    
#     #  SELECT com.name AS companyName,
#     #        AVG(wp.companyRating) AS avgCompanyRating
#     # FROM workedAtPos wp
#     # JOIN coopPositions cp ON wp.coopPositionId = cp.coopPositionId
#     # JOIN createsPos cr ON cp.coopPositionId = cr.coopPositionId
#     # JOIN users u ON cr.employerId = u.userId
#     # JOIN companyProfiles com ON u.companyProfileId = com.companyProfileId
#     # GROUP BY com.name
#     # ORDER BY avgCompanyRating DESC;

#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     columns = [col[0] for col in cursor.description]
#     theData = [dict(zip(columns, row)) for row in cursor.fetchall()]
#     the_response = make_response(jsonify(theData))
#     the_response.status_code = 200
#     return the_response