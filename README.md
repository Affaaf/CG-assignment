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
### Install Requirements.txt
```shell
pip install -r requirements.txt
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
The server will start on port 8000 on address http://127.0.0.1:8000. 

## Docker Envoirment
Build Docker Images and Run server
```shell
sudo docker compose up --build -d
```
Open Docker Terminal
```shell
sudo docker-compose exec web bash
```

## Pytest
```shell
pytest -v
```
For running pytests