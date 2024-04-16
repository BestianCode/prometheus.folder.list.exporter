FROM python:3.11-slim-bullseye

ENV USERNAME app
ENV UID 1001
ENV USERHOME /app
ENV APP_ROOT ${USERHOME}/src

RUN mkdir -p ${APP_ROOT}

COPY exporter.py ${APP_ROOT}/
COPY start.sh ${APP_ROOT}/
COPY requirements.txt ${APP_ROOT}/

RUN pip install -r ${APP_ROOT}/requirements.txt
RUN chmod 0755 ${APP_ROOT}/*.sh

RUN addgroup ${USERNAME} --gid ${UID}
RUN adduser  ${USERNAME} --uid ${UID} --gid ${UID} --home ${USERHOME} --shell /bin/bash --no-create-home

RUN chown -R ${USERNAME}:${USERNAME} ${USERHOME}

USER ${USERNAME}:${USERNAME}
WORKDIR ${APP_ROOT}

CMD ["./start.sh"]