from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class VoteMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    answer_start = db.Column(db.DateTime)
    answer_end = db.Column(db.DateTime)
    mobile = db.Column(db.String)
    qq = db.Column(db.String)
    grade = db.Column(db.String)
    school = db.Column(db.String)
    rank = db.Column(db.String)
    book_type = db.Column(db.String)
    book_pic_1 = db.Column(db.String)
    book_pic_2 = db.Column(db.String)
    book_design_pic = db.Column(db.String)
    book_read_me = db.Column(db.String)
    book_skill = db.Column(db.String)
    selected = db.Column(db.Boolean)

db.create_all()


@app.route('/message/<id>')
def message(id=None):
    vm = VoteMessage.query.filter_by(id=id).first()
    return render_template('message.html', vm=vm)


@app.route('/accept/<id>')
def accept(id=None):
    vm = VoteMessage.query.filter_by(id=id).first()
    vm.selected = True
    db.session.commit()
    return "OK"


@app.route('/reject/<id>')
def reject(id=None):
    vm = VoteMessage.query.filter_by(id=id).first()
    vm.selected = False
    db.session.commit()
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=8000)