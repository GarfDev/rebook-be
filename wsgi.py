from os import getenv
from app import initialize_app

## At this point, we will replace default flask WSGI by another
## WSGI called Gunicoin, you can see how we embed our app on that
## at ./scripts/serve.sh

config_type = "development" if getenv('ENV') == None else getenv('ENV')
application = initialize_app(config_type)

if __name__ == "__main__":
  application.run(host='0.0.0.0')