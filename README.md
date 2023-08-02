# CG-assignment



### Clone Repository
```shell
git clone https://github.com/Affaaf/CG-assignment.git
```
## Non Docker Envoirment

### Create Virtual env  
```shell
python3 -m venv env
source env/bin/activate
```
### Database Migrations
```shell
python manage.py makemigrations
python manage.py migrate
```
### Run Server
```shell
python manage.py runserver
```

## Docker Envoirment
Build Docker Images and Run server
```shell
sudo docker compose up --build -d
```
Open Docker Terminal
```shell
sudo docker-compose exec web bash
```