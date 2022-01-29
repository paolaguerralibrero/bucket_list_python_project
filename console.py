import pdb

import repositories.user_repository as user_repository
from models.user import User


#user = User("Cleyra", "Uzcategui")
#user_saved = user_repository.save(user)
#print("user id: " + str(user_saved.id) + " user name:" + user_saved.first_name)

users = user_repository.select_all()

for user in users:
    print(user)

pdb.set_trace()
