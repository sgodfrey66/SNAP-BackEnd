# Starting dev environment

Use this command to start db

```
docker-compose -f docker-compose/docker-compose.dev.yml up -d
```

# Per-object permisssions

https://www.youtube.com/watch?v=90T5D4KUjWI

Use Django Guardian? https://github.com/django-guardian/django-guardian

or

Django Rules

# Logging

Application logging should be handled with `app` or `app.[XYZ]` loggers:

```
import logging
logging.getLogger('app').error('app error')
logging.getLogger('app.[XYZ]').error('app error')
```

Set LOGLEVEL environment variable to control app-level logger verbosity.

# Testing api

Goto `http://localhost:8000/swagger/`, Authorize by entering `Token [ACCESS_TOKEN]` in the authorize box.

To obtain new access token use the command: `./manage.py drf_create_token [USERNAME]`
