from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

#----- run once to create db -----#
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task_content = request.form.get('task')
    new_task = Task(content=new_task_content)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)






