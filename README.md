# CodeToGive Backend Server
CodeToGive Backend Server is a Python REST API server powered by FastAPI framework.

## Tech stack
### API Framework
- FastAPI
### Database
- Postgresql
- Redis
### Containerirzation
- Docker
- Docker compose (development)
- Kubernetes (production)
### Deployment
- GCE-GKE (Google Compute Engine-Goole Kubernetes Engine)
- Travis-CI
### Dependencies management
- poetry
### Others:
- Nginx
- Makefile
- OpenAPI

## Installation
### Development
The whole development workflow is powered by `docker` and `docker-compose`. 
To run the application locally, only `docker` and `docker-compose` are required to be installed
In order to install `docker` and `docker-compose`. Please visit https://docs.docker.com/compose/install/

#### Usage
To start the application using `docker-compose`
```bash
docker compose up --build
```

### Production
By the support of Docker and Kubernetes, the application is continuously deployed into Google Cloud Kubernetes Engine. 
Intermediate steps (building docker images, connecting to GKE, run tests,...) are done by TravisCI
To visit the OpenAPI UI: https://34.116.151.108/docs

## Contributing
This is a hackathon project. Once it's public, depends on further decisions of the hackathon organization and team member, pull requests might be welcome.

## License
[MIT](https://choosealicense.com/license/mit/)