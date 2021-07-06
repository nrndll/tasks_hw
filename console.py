# import pdb
from models.task import Task
from models.user import User

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

task_repository.delete_all()
user_repository.delete_all()

user_1 = User("Jack", "Jarvis")
user_2 = User("Victor", "McDade")
user_repository.save(user_1)
user_repository.save(user_2)

user_repository.select_all()

task = Task("walk the dog", user_1, 60)
task_repository.save(task)

print(user_repository.select_all())
print(task_repository.select_all())

# # pdb.set_trace()
