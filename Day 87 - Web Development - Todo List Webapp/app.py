from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = 'c7e3bbf68f5c4a8004fc08ff8858117f'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    task_id = HiddenField('Task ID')
    submit = SubmitField('Update Task')

#----- run once to create db -----#
# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    form = TaskForm()
    return render_template('index.html', tasks=tasks, form=form)

@app.route('/add', methods=['POST'])
def add_task():
    form = TaskForm(request.form)
    if form.validate_on_submit:
        new_task_content = form.task.data
        new_task = Task(content=new_task_content)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = TaskForm(request.form, obj=task)

    if request.method == 'POST' and form.validate_on_submit():
        task.content = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', form=form, task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
