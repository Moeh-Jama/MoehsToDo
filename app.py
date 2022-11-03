from datetime import timedelta
from flask import Flask, jsonify, request, session
from .backend_code.src.todo import Todo
# from flask.ext.session import Session

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def main():
    return "Welcome to Moehs ToDo App!"

@app.route('/current_user/', methods=['GET'])
def current_user():
  response = {}
  print(session)
  if 'owner_id' in session:
    response = jsonify({ 'owner_id': session['owner_id'] });
  else:
    response =  jsonify({'error': 'No user is connected, login!'})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/owner/<owner_id>', methods=['GET'])
def owner_posts(owner_id):
  todo = Todo()
  return jsonify(todo.get_all_owner_posts(owner_id))

@app.route('/create_user/<firstname>', methods=['POST'])
def create_user(firstname):
  # print('requestedjson', request.get_json())
  todo = Todo()
  owner_id = todo.create_new_user(firstname)
  if owner_id:
    session['owner_id'] = owner_id
    session.permanent = True
  print(session)
  response = jsonify({ 'owner_id': owner_id })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/delete_user/<owner_id>', methods=['POST'])
def delete_user(owner_id):
  todo = Todo()
  todo.remove_user(owner_id)

@app.route('/post/<owner_id>', methods=['GET'])
def post(owner_id):
  todo = Todo()
  response = jsonify({"posts": todo.get_all_owner_posts(owner_id)})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response
  # if request.args.get('owner_id'):
  #   todo = Todo()
  #   return jsonify(todo.get_post(post_id))
  # else:
  #   return 'create todo post!'