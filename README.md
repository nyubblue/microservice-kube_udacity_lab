[![<ORG_NAME>](https://circleci.com/gh/nyubblue/microservice-kube_udacity_lab.svg?style=svg)](<https://github.com/nyubblue/microservice-kube_udacity_lab>)

1. Summary: This project perform a Dockerfile to containerize a application, deploy the containerized application using Docker
And configure Kubernetes, create cluster and deploy a container using Kubernetes.

2. About Python script and web app:
- setting env for python : python3 -m venv venv && source venv/bin/activate
- install all dependencies of project : pip install -r requirements.txt
- Run the Python Flask app: python app.py

3. explanation of the files:
- Dockerfile : code of all steps for building a docker image
- Makefile : code of tasks that can call by make command
- app.py : the python code of flask app for the Machine Learning Microservice API
- requirements.txt : contains the list of library for app.py
- run_docker.sh : the script file perform for building the docker image
- upload_docker.sh : the script file perform for pushing the docker image to docker hub
- make_prediction.sh : the script file perform for testing the Machine Learning Microservice API
- run_kubernetes.sh : the script file perform for run docker hub container and forwarding the container port to the pod