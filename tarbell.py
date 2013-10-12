# Short project name
NAME = "tarbell-searchable-map"

# Descriptive title of project
TITLE = "Searchable map demo"



# Default template variables
DEFAULT_CONTEXT = {'addrMarkerImage': u'images/blue-pushpin.png',
 'center_lat': 41.8781136,
 'center_lng': -87.6667785645,
 'defaultZoom': 11.0,
 'fusionTableId': u'1m4Ez9xyTGfY2CU6O-UgEcPzlS0rnzLU93e4Faa0',
 'googleApiKey': u'AIzaSyA3FQFrNr5W2OEVmuENqhb2MBB2JabdaOY',
 'locationColumn': u'geometry',
 'locationScope': u'chicago',
 'name': 'tarbell-searchable-map',
 'recordName': u'result',
 'recordNamePlural': u'results',
 'searchRadius': 805.0,
 'title': u'Searchable Map Template Demo'}

# S3 buckets
S3_BUCKETS = {
    "production": "s3://projects.recoveredfactory.net//tarbell-searchable-map/",
    "staging": "s3://projects.beta.recoveredfactory.net//tarbell-searchable-map/",
}


# Repository this project is based on (used for updates)
TEMPLATE_REPO_URL = "https://github.com/eads/tarbell-map-template"