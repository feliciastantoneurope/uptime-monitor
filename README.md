Python Uptime Monitor
A lightweight uptime monitoring tool built in Python that checks website availability, logs status changes, and detects downtime in real time.

Purpose of This Project
This project serves as a tool to monitor the availability of web services in real-time. It simulates real-world service reliability tasks common in Technical Product Support and Site Reliability Engineering (SRE) roles. The goal is to strengthen skills in API interaction, automated logging, and system reliability monitoring.

Features
Periodically checks website availability

Logs uptime and downtime status

Detects and records status changes

Simple configuration for target URLs and intervals

Tech Stack
Language: Python

Libraries: Requests, Logging

Environment: Python Virtual Environment (venv)

Status: Fully functional locally; preparing for Docker containerization and cloud deployment.

How to Run This Locally
To run this project on your own machine, follow these steps:

Clone the repository:

Bash
git clone https://github.com/feliciastantoneurope/uptime-monitor
cd uptime-monitor
Set up the virtual environment:

Bash
# Create the environment
python -m venv venv

# Activate the environment (Windows)
venv\Scripts\activate
Install the required dependencies:

Bash
pip install -r requirements.txt
Run the script:

Bash
python main.py
Project Status
Currently in progress:

Adding containerization support using Docker

Preparing deployment on Fly.io

Improving logging and error handling

Future Improvements
Email/Slack alerts for downtime

Dashboard for monitoring results

Config file support (.env or YAML)

Cloud deployment (Fly.io)

Author
Felicia Stanton-Europe GitHub: https://github.com/feliciastantoneurope

Everything looks fantastic, Felicia! You have a professional, recruiter-ready README that clearly outlines what your tool does, why you built it, and how a developer can test it. You're all set to save this on your GitHub! Is there anything else you need help with before you head out for your birthday plans?
