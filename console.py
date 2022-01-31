import pdb

import repositories.user_repository as user_repository
from models.user import User
from models.country import Country
from models.visit import Visit

import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repo


#user = User("Cleyra", "Uzcategui")
#user_saved = user_repository.save(user)
#print("user id: " + str(user_saved.id) + " user name:" + user_saved.first_name)
#country = Country("Denmark")
#country_repository.save(country)

#users = user_repository.select_all()

#for user in users:
#    print(user)

#user = user_repository.select_by_id(9)
#print(user)

# user_repository.delete_all()

#country_repository.delete_all()




# user = User("Emilia", "Uzcategui", 10)
# user_repository.update(user)

# country = Country("Finland", 0)
# country_repository.update(country)

# visit_repo.save(Visit(User("","",1), Country("",1)))
# visit_repo.save(Visit(User("","",2), Country("",2)))


pdb.set_trace()
