FROM gitlab.ldv.ei.tum.de:5005/cellphaser/cp-containers/cp-component-backend-template:latest
# To have a look at what's available in this image already have a look at:
# https://gitlab.ldv.ei.tum.de/cellphaser/cp-containers/-/tree/master/cp-component-backend-template

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install cellface

WORKDIR /usr/src/app/src

EXPOSE 5000
ENV SCRIPT_NAME="/cytometrygating" PORT="5000" FLASK_APP="app:app"

ENTRYPOINT flask db upgrade && flask db migrate && flask db upgrade && gunicorn --reload --reload-engine=poll --timeout $CP_DEV_GUNICORN_TIMEOUT app:app