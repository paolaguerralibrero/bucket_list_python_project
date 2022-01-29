import pdb

import repositories.user_repository as user_repository
from models.user import User


#user = User("Cleyra", "Uzcategui")
#user_saved = user_repository.save(user)
#print("user id: " + str(user_saved.id) + " user name:" + user_saved.first_name)

users = user_repository.select_all()

#for user in users:
#    print(user)

#user = user_repository.select_by_id(9)
#print(user)

# user_repository.delete_all()


user = User("Emilia", "Uzcategui", 10)

user_repository.update(user)

pdb.set_trace()
