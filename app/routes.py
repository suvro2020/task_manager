from flask import Blueprint, render_template, request, redirect, url_for
import mysql.connector
from flask import current_app

main_bp = Blueprint('main', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host=current_app.config['MYSQL_HOST'],
        user=current_app.config['MYSQL_USER'],
        password=current_app.config['MYSQL_PASSWORD'],
        database=current_app.config['MYSQL_DB']
    )

@main_bp.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks WHERE status="pending"')
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', tasks=tasks)

@main_bp.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tasks (task_name) VALUES (%s)', (task_name,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('main.index'))

@main_bp.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE tasks SET status="completed" WHERE id=%s', (task_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('main.index'))

@main_bp.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=%s', (task_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('main.index'))
