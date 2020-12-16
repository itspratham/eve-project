from eve import Eve

# MONGO_URI = "mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"
#
# DOMAIN = {
#     "godfather": {}
# }

if __name__ =="__main__":
    app = Eve(settings="settings.py")
    app.run(debug=True)