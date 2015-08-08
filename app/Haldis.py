from flask import Flask
from flask.ext.bootstrap import Bootstrap, StaticCDN
from flask.ext.sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

Bootstrap(app)
app.extensions['bootstrap']['cdns']['bootstrap'] = StaticCDN()
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(debug=True)
