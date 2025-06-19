# cloudstudio-test-mqtt

A Python script for testing MQTT connections to cloud studio.

## Required Environment Variables

Create a `.env` file in the project root directory.

The following variables are **required** and the script will fail if they are not set:
- `MQTT_USER`
- `MQTT_PASS` 
- `MQTT_TOPIC`

The following variables have defaults if not specified:
- `MQTT_HOST` (defaults to "cloud-mqtt.movitherm.com")
- `MQTT_PORT` (defaults to 8883)


## SSL Certificate

The script expects an `mqtt_cert.pem` file in the project directory for SSL certificate verification.
