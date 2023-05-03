# Setup debuggin capabilities
from os import getenv
if getenv("CP_DEV_VSCODEDEBUG_HOST") == "cp-plugin-cytometrygating-backend":
    import debugpy
    debugpy.listen(('cp-plugin-cytometrygating-backend', 5678))
    print("\033[1m\033[32m ready to attach VS Code debugger, press F5 in VS Code! \033[0m") # \033 stuff is for bold green text
if getenv("CP_DEV_PYCHARMDEBUG_TARGET") == "cp-plugin-cytometrygating-backend":
    import pydevd_pycharm
    pydevd_pycharm.settrace('cp-traefik', port=5679, stdoutToServer=True, stderrToServer=True, suspend=False)


from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
import os

# We create the app object BEFORE importing apis and database, so they can use the app object
# Yes, this creates curcular imports, see https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.wsgi_app = ProxyFix(app.wsgi_app)

# Setup logging, as this is also used by apis and database
import logging
logger = logging.getLogger('gunicorn.error')

# Next we import database instead of apis, because the apis depend on the database
import database

from apis import api
api.init_app(app)


if __name__ == '__main__':
    # THIS IS NOT BEING EXECUTED
    # To cater for the URL prefix when running with "cellphaser start",
    # "gunicorn" is used to serve this app (see ../Dockerfile)
    app.run(debug=True, host='0.0.0.0')