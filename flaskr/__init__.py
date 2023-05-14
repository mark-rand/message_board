import os
from flask import Flask, send_from_directory, jsonify


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DefaultConfig')
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    if not app.config['TESTING']:
        app.config['DATABASE'] = os.environ.get("DATABASE")
        if not app.config['DATABASE']:
            raise ValueError("No DATABASE set for Flask application")

    if not ('FONT_OVERRIDE' in app.config and app.config['FONT_OVERRIDE']):
        from flaskr import font_definitions
        app.config['FONTS'] = font_definitions.FONTS

    # register the database commands
    from flaskr import db

    db.init_app(app)

    @app.route('/favicon.ico')
    def favicon():
        print(app.root_path)
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route("/info")
    def info():
        info = {'running': True, 'test_mode': app.config['TESTING'], 'font_count': len(
            app.config['FONTS']), 'debug_mode': app.debug}
        return jsonify(info)
    from flaskr import message_controller
    app.register_blueprint(message_controller.bp)

    from flaskr import get_uuid
    app.register_blueprint(get_uuid.bp)

    from flaskr import mode_management
    app.register_blueprint(mode_management.bp)

    return app
