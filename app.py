from flask import Flask, jsonify, request
from .backend_code.src.todo import Todo

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def main():
    return "Welcome to Moehs ToDo App!"

@app.route('/owner/<owner_id>', methods=['GET'])
def owner_posts(owner_id):
  todo = Todo()
  return jsonify(todo.get_all_owner_posts(owner_id))

@app.route('/create_user/<firstname>', methods=['POST'])
def create_user(firstname):
  print('requestedjson', request.get_json())
  todo = Todo()
  owner_id = todo.create_new_user(firstname)
  response = jsonify({ 'owner_id': owner_id })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/delete_user/<owner_id>', methods=['POST'])
def delete_user(owner_id):
  todo = Todo()
  todo.remove_user(owner_id)

@app.route('/post/', methods=['GET'])
def post():
  if request.args.get('owner_id'):
    todo = Todo()
    return jsonify(todo.get_post(post_id))
  else:
    return 'create todo post!'