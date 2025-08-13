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
advisorAdvisee = Blueprint('advisoradvisee', __name__)

# ------------------------------------------------------------
# This is a stubbed route to update a product in the catalog
# The SQL query would be an UPDATE. 
@advisorAdvisee.route('/advisoradvisee', methods = ['PUT'])
def reassignAdvisor():
    advisor_info = request.json
    current_app.logger.info(advisor_info)

    return "Success"
