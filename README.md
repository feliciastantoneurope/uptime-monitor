# Python Uptime Monitor

A lightweight uptime monitoring tool built in Python that checks website availability, logs status changes, and detects downtime in real time.

This project is part of my learning journey into backend development, automation, and technical product support engineering.

---

##  Features

- Periodically checks website availability
- Logs uptime and downtime status
- Detects and records status changes
- Simple configuration for target URLs and intervals

---

## Tech Stack

- Python
- Requests (HTTP checks)
- Logging module
- (Planned) Docker containerization
- (Planned) Fly.io deployment

---

## Set up a virtual environment

1. Clone the repository:
git clone https://github.com/feliciastantoneurope/uptime-monitor
cd uptime-monitor

2. Set up the virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
 pip install -r requirements.txt

4. Run the monitor:
 python main.py


##  Project Status

Currently in progress:
- Adding containerization support using Docker
- Preparing deployment on Fly.io
- Improving logging and error handling

---

## Purpose of This Project

This project serves as a tool to monitor the availability of web services in real-time. It simulates real-world service reliability tasks common in Technical Product Support and Site Reliability Engineering (SRE) roles. The goal is to strengthen skills in API interaction, automated logging, and system reliability monitoring.

---

##  Future Improvements

- Email/Slack alerts for downtime
- Dashboard for monitoring results
- Config file support (.env or YAML)
- Cloud deployment (Fly.io)

---

##  Author

Felicia Stanton-Europe  
GitHub: https://github.com/feliciastantoneurope




