from config import app
from models.models import *
from routes.routes import *
from flask import render_template

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5555)))

