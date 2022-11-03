from backend_code.src.todo import Todo

def create_user_stuff(app, owner_id):
  app.add_new_post(owner_id, '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''')

app = Todo()
# mo = app.create_new_user('jemima')
create_user_stuff(app, 'be7b5a832d6843859383c78a53d91347')


# jem = app.create_new_user('jemima')