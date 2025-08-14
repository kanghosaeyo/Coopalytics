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
        SELECT *
        FROM companyProfiles
        WHERE companyProfileId = %s
    '''.format(companyProfileId)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    theData = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Advisor views all company profiles sorted by their rating
@companyProfiles.route('/companyProfiles/rating', methods=['GET'])
def get_company_profiles_by_rating():
    query = '''
        SELECT *
        FROM companyProfiles
        ORDER BY rating DESC;
    '''
    
    # SELECT com.name AS companyName,
    #        AVG(wp.companyRating) AS avgCompanyRating
    # FROM workedAtPos wp
    # JOIN coopPositions cp ON wp.coopPositionId = cp.coopPositionId
    # JOIN createsPos cr ON cp.coopPositionId = cr.coopPositionId
    # JOIN users u ON cr.employerId = u.userId
    # JOIN companyProfiles com ON u.companyProfileId = com.companyProfileId
    # GROUP BY com.name
    # ORDER BY avgCompanyRating DESC;

    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    theData = [dict(zip(columns, row)) for row in cursor.fetchall()]
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Employer creates a company profile
@companyProfiles.route('/companyProfiles/create/<companyProfileId>', methods=['POST'])
def createCompanyProfile(companyProfileId):
    
    the_data = request.json
    current_app.logger.info(the_data)
    
    name = the_data['company_name']
    bio = the_data['company_bio']
    industry = the_data['company_industry']
    websiteLink = the_data['website_link']
        
    query = f'''
    INSERT INTO companyProfiles (name, bio, industry, websiteLink)
    VALUE( '{name}', '{bio}', '{industry}', '{websiteLink}')
    '''
    
    current_app.logger.info(query)
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Created company profile")
    response.status_code = 200
    return response

# Employer updates/edits company information
@companyProfiles.route('/companyProfiles/update/<companyProfileId>', methods=['PUT'])
def updateCompanyProfile(companyProfileId):
    current_app.logger.info('PUT /companyProfiles/update/<companyProfileId> route')
    
    company_info = request.json
    companyId = company_info['id']
    companyName = company_info['name']
    companyBio = company_info['bio']
    companyIndustry = company_info['industry']
    companyWebsite = company_info['website_link']
    
    query = '''
        UPDATE companyProfiles
        SET name = %s,
            bio = %s,
            industry = %s,
            websiteLink = %s
        WHERE companyProfileId = %s
    '''
    data = (companyName, companyBio, companyIndustry, companyWebsite, companyId)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Updated company profile!'