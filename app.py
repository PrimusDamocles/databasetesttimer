from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime
from flask_migrate import Migrate
from models import db, Posts


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app


app = create_app()
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/", methods=['GET', 'POST'])
def timer():
    if request.method == 'POST':
        new_message = Posts(message= request.form['message'])
        db.session.add(new_message)
        db.session.commit()
    messages = Posts.query.order_by(Posts.created_at.desc()).all()
    return render_template('timer.html', message=messages)


