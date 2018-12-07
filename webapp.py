import os

import pytz as pytz
from flask import Flask, render_template, send_from_directory
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def root():
    return "Homer Simpson picture is on  /homersimpson, " \
           "The time in the moment of request in Covilha City (Portugal)  is on /covilha"


@app.route("/homersimpson")
def homersimpson():
    return render_template("homersimpson.html", user_image='static/pic/homer.jpg')


@app.route("/covilha")
def covilha():
    utcmoment_naive = datetime.utcnow()
    utcmoment = utcmoment_naive.replace(tzinfo=pytz.utc)
    timezones = 'Portugal'
    localformat = "%Y-%m-%d %H:%M:%S"
    localdatetime = utcmoment.astimezone(pytz.timezone(timezones))
    return localdatetime.strftime(localformat)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80") #//TODO: Read Host and port from env config
