ARG APP_VERSION=0.0.1

FROM python:3.10-rc-slim AS wheeler
ARG APP_VERSION

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip wheel . -w dist

FROM python:3.10-rc-slim AS production
ARG APP_VERSION

COPY --from=wheeler /usr/src/app/dist/app-${APP_VERSION}-py3-none-any.whl /tmp/
RUN pip install /tmp/app-${APP_VERSION}-py3-none-any.whl

CMD ["app-cli"]
