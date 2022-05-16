ARG APP_VERSION=0.0.1

FROM python:3.10-rc-slim AS dev
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN python -m pip install --upgrade pip \
    && pip install --no-input -q --no-cache-dir .[dev] \
    && pip install --no-input -q --no-cache-dir -e .

FROM dev AS tests
RUN pip install --no-input -q .[test]
CMD tox

FROM dev AS wheeler
ARG APP_VERSION
RUN pip wheel . -w dist

FROM python:3.10-rc-slim AS production
ARG APP_VERSION
COPY --from=wheeler /usr/src/app/dist/app-${APP_VERSION}-py3-none-any.whl /tmp/
RUN pip install /tmp/app-${APP_VERSION}-py3-none-any.whl

CMD ["app-cli"]
