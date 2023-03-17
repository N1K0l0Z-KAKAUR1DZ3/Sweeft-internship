### URL Shortener
This is a simple URL shortener app built with Flask, a web framework for Python.

## Description
The URL shortener has two endpoints:

POST /shorten: This endpoint accepts a JSON payload containing a long URL and returns a short URL. It generates a random 6-character string composed of lowercase letters and digits to be used as the short URL ID. The short URL is returned in the response.

GET /<short_id>: This endpoint accepts a short URL ID as a URL parameter and redirects the request to the long URL associated with that short URL ID.

The app keeps track of the mappings between short URLs and long URLs in a dictionary called urls.

## Dependencies
Flask: The web framework used to build the app.
Random: Used to generate random IDs for short URLs.
String: Used to generate random IDs for short URLs.
