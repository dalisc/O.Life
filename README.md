# Pokkamon's Recommendation System

## About the app
This personalized recommendation engine was developed for a virtual hackathon organised by Circles.Life. It uses collaborative filtering to cluster similar users together and content-based filtering to recommend specific items to users in a cluster. We used various APIs to do semantic analysis on event and movie descriptions to see how closely they match users' existing tastes and preferences.

## This web app is now live!
http://dalisc.pythonanywhere.com/

## Prototype demo video
https://youtu.be/AJri3LBhzWU

## Cloning on your own device

#### Pre-requisites
* Java 11
* PostgreSQL

#### 1. Clone the repository
#### 2. Navigate to the project root directory
The root directory contains the files 'manage.py' and 'requirements.txt'.
#### 3. Download required modules
Run the following line on your terminal to download all required modules.
```python
pip install -r requirements.txt
```
#### 4. Run the server
```python
python manage.py runserver
```
