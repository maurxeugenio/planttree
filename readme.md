#  Tutorial para subir o projeto

Para subir o projeto rode:
$ docker-compose build
$ make migrate
$ make createsuperuser  
> (vai criar um usuário com e-mail: dev@plantree.com senha: dev123)

$ docker-compose run app python populate.py
> vai criar usuários, contas, plantas, plantar arvores e adicionar usuários a contas.

$ make runserver
> localhost:8000


não foram escritos testes. 
