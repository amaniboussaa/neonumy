Build the new image and spin up the two containers:

$ docker-compose up -d --build

Run the migrations:

$ docker-compose exec web python manage.py migrate --noinput

Stop the Docker containers:

docker-compose down -v --rmi all
