from flask import Flask
from app.extensions import db
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig

def create_app(config_name: str = "development") -> Flask:
    app = Flask(__name__)
    if config_name == "testing":
        app.config.from_object(TestingConfig)
    elif config_name == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    return app
