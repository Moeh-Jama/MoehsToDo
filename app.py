from datetime import timedelta
from flask import Flask, jsonify, request, session, make_response
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
    response = jsonify({ 'owner_id': session['owner_id'] })
  else:
    response =  jsonify({'error': 'No user is connected, login!'})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/user/<owner_id>', methods=['GET'])
def user_details(owner_id):
  todo = Todo()
  user = todo.get_user_details(owner_id)
  response = jsonify({ 'user': user })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/owner/<owner_id>', methods=['GET'])
def owner_posts(owner_id):
  todo = Todo()
  posts = todo.get_all_owner_posts(owner_id)
  print('first posts', posts[0])
  return jsonify(posts)

@app.route('/create_user/<firstname>', methods=['POST', 'OPTIONS'])
def create_user(firstname):
  if request.method == "OPTIONS": # CORS preflight
    return _build_cors_preflight_response()

  data = request.json
  profile_image = data['profileImage']
  todo = Todo()
  owner_id = todo.create_new_user(firstname, profile_image=profile_image)
  if owner_id:
    session['owner_id'] = owner_id
    session.permanent = True
  print(session)
  response = jsonify({ 'owner_id': owner_id, 'profile_image': profile_image })
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/delete_user/<owner_id>', methods=['POST'])
def delete_user(owner_id):
  todo = Todo()
  todo.remove_user(owner_id)

@app.route('/post/<owner_id>', methods=['GET'])
def post(owner_id):
  todo = Todo()
  posts = todo.get_all_owner_posts(owner_id)
  print('first posts', posts[0])
  response = jsonify({"posts": posts})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route('/postee/<owner_id>', methods=['POST', 'OPTIONS'])
def new_post(owner_id):
  if request.method == "OPTIONS": # CORS preflight
    return _build_cors_preflight_response()
  todo = Todo()
  # check user id is non-null
  data = request.json
  post_message = data['postMessage']
  print('post_message is', post_message)
  todo.add_new_post(owner_id, post_message)
  response = jsonify({})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
