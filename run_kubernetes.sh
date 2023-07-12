#!/usr/bin/env bash

# Step 1:
# This is your Docker ID/path
dockerpath="nyubblue/ybun-python-app";

# Step 2
# Run the Docker Hub container with kubernetes
kubectl create deploy py-helloworld-kube --image="${dockerpath}:v1.0.0" --port=8000;

# Step 3:
# List kubernetes pods
kubectl get pods;

# Step 4:
# Forward the container port to a host
POD_NAME=$(kubectl get pods -l app=py-helloworld-kube -o jsonpath='{.items[0].metadata.name}');
kubectl port-forward "pod/${POD_NAME}" --address 0.0.0.0 8000:80
