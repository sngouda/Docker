DOCKER TASK

Project: Containerize a web service

You're a DevOps engineer at esc bash. A developer hands you a small Python web service and asks you to containerize it properly so it can run the same way everywhere - built cleanly, cache-friendly, and not running as root.

Set up the project
Run this first. It creates /root/orders-web with the app source:

bash

curl -fsSL https://raw.githubusercontent.com/Esc-Bash/project-init-scripts/main/docker/project-1/init.sh | bash
This drops in app.py (a small web app that serves esc bash orders v1 on its root path and listens on port 8000) and a requirements.txt. Do not change these files - your job is to containerize them.

What to build
In /root/orders-web, produce:

A .dockerignore that excludes at least __pycache__.
A Dockerfile that:
builds on python:3.12-slim
is ordered so requirements.txt is copied and installed with pip before the rest of the source is copied with COPY . .
creates a non-root user and switches to it so the app does not run as root
runs the app by default
A built image tagged orders-web:1.0.
A running container named orders that publishes host port 8080 to the app's port 8000.
When it works, curl http://localhost:8080/ returns esc bash orders v1, and the container runs as a non-root user.


