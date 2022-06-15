# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     print('greeting world')
#     return 'hello world'


# app.run(use_reloader=True, debug=False)


from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


SWAGGER_URL = ''  # URL for exposing Swagger UI (without trailing '/')
# Our API url (can of course be a local resource)
API_URL = '/static/swagger.json'

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

app.run(use_reloader=True)

# Now point your browser to localhost:5000/api/docs/
