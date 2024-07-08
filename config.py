import re
import requests
import logging

SESSION = requests.Session()

APP_URL = "https://restful-booker.herokuapp.com"
ADMIN_USER = "admin"
ADMIN_PASSWORD = "password123"