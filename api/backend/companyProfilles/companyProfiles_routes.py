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
companyProfile = Blueprint('companyProfiles', __name__)


# ------------------------------------------------------------
# This is a POST route to add a new product.
# Remember, we are using POST routes to create new entries
# in the database. 
@companyProfile.route('/companyProfiles', methods=['POST'])
def createCompanyProfile():

#     INSERT INTO companyProfiles
# VALUE (20000, 'Google',
#      'We are google', 'IT',
#      'google.com');

# CREATE TABLE companyProfiles (
#     companyProfileId INT PRIMARY KEY,
#     name             VARCHAR(20) NOT NULL,
#     bio              LONGTEXT,
#     industry         VARCHAR(20) NOT NULL,
#     websiteLink      VARCHAR(50)
# );

    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    id = the_data['companyProfileId']
    name = the_data['product_name']
    bio = the_data['bio']
    industry = the_data['industry']
    websiteLink = the_data['websiteLink']
    
    query = f'''
        INSERT INTO companyProfiles (companyProfileId,
                                    name, bio, industry, websiteLink)
        VALUES ('{id}', '{name}', '{bio}', '{industry}', '{websiteLink}')
    '''
    # TODO: Make sure the version of the query above works properly
    # Constructing the query
    # query = 'insert into products (product_name, description, category, list_price) values ("'
    # query += name + '", "'
    # query += description + '", "'
    # query += category + '", '
    # query += str(price) + ')'
    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added company profile")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# This is a stubbed route to update a product in the catalog
# The SQL query would be an UPDATE. 
@companyProfile.route('/companyProfiles', methods = ['PUT'])
def update_companyProfile():
    companyProfile_info = request.json
    current_app.logger.info(companyProfile_info)
    return "Success"


#------------------------------------------------------------
# Get all company profiles from the system
@companyProfile.route('/companyProfiles', methods=['GET'])
def get_companyProfile():
    cursor = db.get_db().cursor()
    cursor.execute('''SELECT id, company, last_name,
                    first_name, job_title, business_phone FROM customers
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response
