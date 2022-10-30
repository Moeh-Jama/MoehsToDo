from backend_code.src.todo import Todo

def create_user_stuff(app, owner_id):
  app.add_new_post(owner_id, 'my name is jem')

app = Todo()
mo = app.create_new_user('jemima')
create_user_stuff(app, mo)


# jem = app.create_new_user('jemima')