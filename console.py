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
country3 = Country("Bulgaria", "Europe", "https://upload.wikimedia.org/wikipedia/commons/9/9a/Flag_of_Bulgaria.svg")
country_repository.save(country3)
country4 = Country("Italy", "Europe", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Flag_of_Italy.svg/2560px-Flag_of_Italy.svg.png")
country_repository.save(country4)
country5 = Country("Spain", "Europe", "https://stuffedeyes.files.wordpress.com/2018/06/spain-2906824_960_720.png?w=640")
country_repository.save(country5)
country6 = Country("Senegal", "Africa", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Flag_of_Senegal.svg/250px-Flag_of_Senegal.svg.png")
country_repository.save(country6)



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
