import django, os, sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ptree.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from apps.plants.models import Plant, PlantedTree
from apps.accounts.models import User, Accounts
from django.core import management

user_list = [
    'dev1@plantree.com',
    'dev2@plantree.com',
    'dev3@plantree.com',
]

plants_list = [
    ['Acácia', 'Acacia'],
	['Araucária', 'Araucaria angustifolia'],
	['Jaboticabeira', 'Plinia cauliflora'],
	['Mangueira', 'Mangifera indica']
]

accounts_list = [
    'plantaneiros',
    'plantadores',
    'plantagem'
]


for user in user_list:
    User.objects.create(
        email=user,
        password='dev123'
    )
    print(f'created user: {user} password: dev123')


for plant in plants_list:
    Plant.objects.create(
        name=plant[0],
        scientific_name=plant[1]
    )
    print(f'created plant: {plant}')


for account in accounts_list:
    Accounts.objects.create(
        name=account
    )
    print(f'created account: {account}')



# plant multiple tree for users
users = User.objects.all()
plants = Plant.objects.all()

for user in users:
    user.plant_tree(plants.first().id, (0.00, 0.00))
    print(f'planted: {plants.first().name} for: {user.username}')

    list_plants = []
    for plant in plants:
        list_plants.append((plant.id, (0.00, 0.00)))
    user.plant_trees(list_plants)

# add users in accounts
user_list_accounts = [users.first(), users.last()]
accounts_list = [Accounts.objects.all().first(), Accounts.objects.all().last()]

for index, account in enumerate(accounts_list, start=0):
    account.users.add(users[index], users[index+1])
