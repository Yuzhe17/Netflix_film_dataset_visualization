from flask import Flask

app=Flask(__name__)

from netflix_app import routes
