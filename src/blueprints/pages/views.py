from flask import (Blueprint,
                   request,
                   jsonify)


page = Blueprint('pages', __name__, template_folder='templates')


@page.route("/")
def index():
    """
    Index / Main page
    :return: html
    """

    return jsonify({'message': 'This is a test message'}), 201


@page.route("/_execute_task", methods=['POST'])
def _execute_task():
    """
    :return: json
    """
    from src.blueprints.pages.tasks import my_task

    if request.method == 'POST':
        # Invoke celery task
        print(request.json)
        payload = request.json
        task = my_task.delay(payload=payload)

    return jsonify({
        'taskID': task.id,
        'status': task.status,
        'result': task.result
        }), 201
