from flask import Flask, render_template
import datetime

app = Flask(__name__, static_url_path = "/static", static_folder = "static")

@app.route('/')
def index():
  present = datetime.datetime.now()
  future = datetime.datetime(2021, 8, 31, 0, 0, 0)
  difference = future - present
  days = difference.days
  secs = difference.seconds

  hours = secs//3600
  minutes = (secs//60)%60
  return render_template('index.html', days=days, hours=hours, minutes=minutes)


if __name__ == "__main__":
  app.run()
