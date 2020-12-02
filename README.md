# recipe_manager
Deploy in docker for recipe storage and invetory management.

## Security Issues
Django secret must be regenerated and added as and environment variable
Nginx needs to be added to serve static files and reverse proxy for gunicorn

## Tests
One test has been added. 100% coverage for all code is expected.

## Next Steps
Nginx, secrets and tests.
Docker-compose instead of sh scripts.
Streamline deployment to AWS or GCP.
