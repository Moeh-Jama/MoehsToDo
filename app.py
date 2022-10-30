from flask import Flask, jsonify
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
  todo = Todo()
  owner_id = todo.create_new_user(firstname)
  return owner_id

@app.route('/delete_user/<owner_id>', methods=['POST'])
def create_user(owner_id):
  todo = Todo()
  todo.remove_user(owner_id)

@app.route('/post/<owner_id>', methods=['POST'])
def post_todo(owner_id):
  pass

@app.route('/post/<post_id>', methods=['GET'])
def get_post(post_id):
  todo = Todo()
  return jsonify(todo.get_post(post_id)) 
