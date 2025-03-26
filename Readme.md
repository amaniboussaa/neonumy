# Neonumy Photo Album Test

## Overview
Neonumy Photo Album Test is a simple web application that allows users to upload, list, view, and delete images. The project focuses on functionality over aesthetics and provides a REST API for CRUD operations. PostgreSQL is used as the primary database.

## Features
- Upload images via a web interface.
- List all uploaded images as thumbnails.
- View images in full size on a separate details page.
- Delete images from the database.
- REST API for full CRUD operations.
- Docker and Docker Compose setup.

## Technologies Used
- **Backend:** Django with Python 3
- **Frontend:** HTML / Bootstrap (Basic UI for listing and uploading images)
- **Database:** PostgreSQL
- **Version Control:** Git
- **Containerization:** Docker, Docker Compose

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- Docker & Docker Compose
- Git

### Clone the Repository
```sh
$ git clone <repository_url>
$ cd neonumy/NeonumyProject
```


### Running with Docker
Build and run the containers using Docker Compose:
```sh
$ docker-compose up --build
```

### Run Database Migrations
```sh
$ docker-compose exec web python manage.py migrate
```

### Access the Application
- Open your browser and go to `http://127.0.0.1:8000/`.

## API Endpoints
| Method  | Endpoint        | Description                |
|---------|---------------|---------------------------|
| GET     | /photos/list   | List all images           |
| POST    | /photos/upload   | Upload an image           |
| GET     | /photos/<id> | Get image details       |
| DELETE  | /photos/<id>/delete | Delete an image         |

### Stop the Docker containers:
```sh
$ docker-compose down -v --rmi all
```
## License
This project is open-source and available for use and modification.
