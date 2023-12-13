from flask import Flask, jsonify, request
app = Flask(__name__)

# suppose you have your data in the variable named some_data
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    # you can convert that variable into a json string like this
    json_todos = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
        request_body_json = request.json
        todos.append(request_body_json)
        json_todos = jsonify(todos)
        return json_todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position - 1]

    json_todos = jsonify(todos)

    return json_todos

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)