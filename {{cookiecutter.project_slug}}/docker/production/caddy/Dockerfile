{% if cookiecutter.use_react == 'y' %}
# We utilize the multi stage build pattern to create a temporary image we
# use to compile Caddy from scratch (so we can install plugins).
{% else %}
# We utilize the multi stage build pattern to create temporary images we
# use to compile both Caddy from scratch (so we can install plugins) and the
# React project, these are then copied over to the Caddy production image.
{% endif %}

{% if cookiecutter.use_react == 'y' %}
# Build React-image:
FROM node:14.4.0 AS react-builder
WORKDIR /app
COPY ./react/package.json ./package.json
COPY ./react/package-lock.json ./package-lock.json
COPY ./react/src ./src
RUN npm install
COPY ./react/jsconfig.json ./jsconfig.json
COPY ./react/public ./public
RUN npm run build
{% endif %}

# Build Caddy-image:
FROM caddy:2.1.1-builder AS caddy-builder
RUN xcaddy build --with github.com/sillygod/cdp-cache

FROM caddy:2.1.1
COPY --from=caddy-builder /usr/bin/caddy /usr/bin/caddy
{% if cookiecutter.use_react == 'y' %}
COPY --from=build /app/build /srv/react
{% endif %}
COPY ./docker/production/caddy/Caddyfile /etc/Caddyfile