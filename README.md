# Weather based Travel recommendation system

This django based project has two apps. One shows top 10 coolest and cleanest air city in Bangladesh and the other has recommend whether to travel to a district or not.

## Features

- Get list of coolest and cleanest city & Get travel recommendation


## To run this locally
### 1. Clone the repository

```bash
git clone https://github.com/nafiul-miraj-strativ/weather-app
```

### 2. Create a virtual environment

```bash
    python3 -m venv new
```
### 3. For macos/linux

```bash
    source new/bin/activate
```
or for windows

```bash
    new/scripts/activate
```
### 4. Install the dependencies
```bash
pip install -r requirements.txt
```

### 5. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Run server
```bash
python manage.py runserver
```
### 7. Go to this url and other simillar ones 
```bash
http://127.0.0.1:8000/topdistricts/api/v1/topdistricts/
http://127.0.0.1:8000/api/v1/recommender/

```


## Author

- [@nafiul-miraj-startiv](https://www.github.com/nafiul-miraj-strativ)

