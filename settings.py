# MONGO_URI = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"
# RESOURCE_METHODS = ['GET','POST','DELETE']
# X_DOMAINS = '*'
# X_HEADERS = ['Authorization','If-Match','Access-Control-Expose-Headers','Content-Type','Pragma','Cache-Control']
# X_EXPOSE_HEADERS = ['Origin', 'X-Requested-With', 'Content-Type', 'Accept']
#
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# Skip this block if your db has no auth. But it really should.
# MONGO_USERNAME = 'cgadmin'
# MONGO_PASSWORD = ''
# Name of the database on which the user can be authenticated,
# needed if --auth mode is enabled.
MONGO_AUTH_SOURCE = 'godfather'
MONGO_DBNAME = 'godfather'

RESOURCE_METHODS = ['POST']

godfather_schema= {
        '_id':  {
                'type': 'string'
                },
        'name': {
                'type': 'string'
                }
}

godfather = {
    'item_title': 'godfather',

    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],

    'schema': godfather_schema
}


DOMAIN = {
    "godfather": godfather
    }




# Let's just use the local mongod instance. Edit as needed.
# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.



