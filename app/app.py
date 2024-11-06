from flask import Flask

from app.controllers import healthcheck,information_system

app = Flask(__name__)
app.config.from_object('config')

# Controller blueprint registration
app.register_blueprint(healthcheck.bp)
app.register_blueprint(information_system.bp)