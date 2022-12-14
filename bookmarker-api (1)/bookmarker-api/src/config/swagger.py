


template={
    "swageer":2.0,
    "info":{
        "title":{
            "title":"Bookmark api",
            "dscription":"API for bookmarks",
            "contact":{
                "responsibleOrganisation":"",
                "responsibleDeveloper":"",
                "email":"deve@gmail.com",
                "url":"www.facebook.com/deve"
            },
            "TermsOfService":"www.facebook.com/deve",
            "version":"1.0"
        },
        "basePath":"api/v1",
        "schemes":[
            "http",
            "https"
        ],
        "SecurityDefinations":{
            "type":"apikey",
            "name":"authorization",
            "in":"header",
            "description":"Jwt AUTHORIZATION HEADERusing the bearer schemes"
        }
    },
    "specs":[
        {
            "endpoint":"apispec",
            "route":"/apispec.json",
            "rule_filter":lambda rule:True,
            "model_filter":lambda rule:True
        }
    ],
    "static_url_path":"/flasgger_static",
    "swagger_ui":True,
    "specs_route":"/"
}