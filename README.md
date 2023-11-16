# hackathon2
to run the backend:
git clone the repo
python -m venv env
env\scripts\activate.bat
pip install -r requirements
python manage.py runserver
api : http://127.0.0.1:8000/listzones -> list all zones
http://127.0.0.1:8000/listzones/dragons/changeloc/pk/newzone -> change the location of the current dragon
http://127.0.0.1:8000/zones/zoneid -> list details of current zone

