#!/bin/sh
cd /home/pi/Projects/pi_healthcheck
source pi_healthcheck_venv/bin/activate 
pi_healthcheck_venv/bin/python -m send-ip