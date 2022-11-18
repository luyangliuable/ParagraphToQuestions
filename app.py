from flask.cli import FlaskGroup
from flask import Flask
import os


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    app.config['DEBUG'] = True
    app.debug = True

    ###############################################################################
    #                                Upload folder                                #
    ###############################################################################
    app.config['UPLOAD_FOLDER'] = "./upload/files"

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    return app


if __name__ == "__main__":
    cli = FlaskGroup(create_app=create_app)
    cli()
