# Django

## Launch App

```
$ make install
$ make run
```

Sample .env.prod file:

```
DJANGO_SETTINGS_MODULE=myservice.settings.production
DJANGO_SECRET_KEY=areallysupersecretkey
DEBUG=False
STATIC_URL=/static/
STATIC_ROOT=static
ALLOWED_HOSTS='*','localhost'
```

## Utilities and useful commands

- Developer mode

```
$ make install && make dev
```

- Docker compose

Build project and start

```
$ docker-compose build
```

Start with a pre builded project

```
$ docker-compose up
```

- Lint and Prettify code

```
$ make lint
```

- Coverage and test

Run only tests

```
$ make test
```

Run coverage

```
$ make coverage
```

- Swagger

Go to [http://localhost:8000/swagger/](http://localhost:8000/swagger/) URL to see the API documentation