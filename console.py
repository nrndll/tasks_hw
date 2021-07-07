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

task_1 = Task("walk the dog", user_1, 60)
task_repository.save(task_1)
task_2 = Task("feed the cat", user_1, 10)
task_repository.save(task_2)

print(user_repository.select_all())
print(task_repository.select_all())
print(user_repository.tasks(user_1))

#pdb.set_trace()
