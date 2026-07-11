# The Ghost Satellite

I wanted to see if a space defense tracking system could run on a phone with zero graphics. So I built this. 

It is a text-based satellite monitoring tool built with Python on Google Colab. It pulls live space data, checks boundaries, and uses AI for security profiling.

## What it does
* **Live Feed:** Pulls real satellite data instantly from CelesTrak.
* **Border Check:** Sets a boundary over India. If a satellite crosses it, the system triggers an alert.
* **Security Match:** Checks the satellite ID against a safe list. If it is not found, the satellite is flagged as unknown.
* **AI Analysis:** Sends the unknown satellite details to Gemini AI. The AI then writes a quick report on what kind of spy threat it could be.

## Tech
* Python 3
* Skyfield (for space math)
* Requests (to get data)
* Google Colab & Drive

Built completely on a mobile screen using cloud servers.

