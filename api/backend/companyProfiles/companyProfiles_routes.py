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
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Employer creates a company profile
@companyProfiles.route('/companyProfiles', methods=['POST'])
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
    
    response = make_response("Successfully created company profile")
    response.status_code = 200
    return response

