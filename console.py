import pdb

import repositories.user_repository as user_repository
from models.user import User
from models.country import Country
from models.visit import Visit

import repositories.country_repository as country_repository
import repositories.visit_repository as visit_repo


user = User("Cleyra", "Uzcategui")
user_saved = user_repository.save(user)
user = User("Steve", "Meiklejohn")
user_saved = user_repository.save(user)
# print("user id: " + str(user_saved.id) + " user name:" + user_saved.first_name)
country = Country("Denmark", "Europe", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Flag_of_Denmark.svg/1200px-Flag_of_Denmark.svg.png")
country_repository.save(country)
country2 = Country("France", "Europe", "https://cdn.britannica.com/82/682-004-F0B47FCB/Flag-France.jpg")
country_repository.save(country2)


# users = user_repository.select_all()

# for user in users:
#    print(user)

# user = user_repository.select_by_id(9)
# print(user)

# user_repository.delete_all()

# country_repository.delete_all()






# country = Country("Finland", 0)
# country_repository.update(country)



pdb.set_trace()
