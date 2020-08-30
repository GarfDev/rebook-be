echo "Starting server in Production mode"
gunicorn --bind 0.0.0.0:5000 wsgi:application -e ENV=production