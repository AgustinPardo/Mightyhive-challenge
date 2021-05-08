# Mightyhive-challenge

## Deploy locally

#### Prerequisites:
python3(3.6.9)

git

#### Instalation (step by step):

1. Clone the repository:
```
git clone https://github.com/AgustinPardo/Mightyhive-challenge.git
```

2. Go inside "Mightyhive-challenge" folder:
```
cd Mightyhive-challenge
```

3. Install requirements:
```python
pip install -r requirements.txt
```

4. Create the database:
```python
python manage.py migrate
```

5. Populate the database-model based on "data.json" file:
```python
python manage.py shell < model_dump.py
```

6. Run the app at http://127.0.0.1:8000/:
```python
python manage.py runserver
```

## Testing
```python
python manage.py test
```

## Usage: REST Endpoint

1. Run app
2. Open any web browser you prefer
3. Go to http://localhost:8000/getData/?key= "key to search" (e.g. http://localhost:8000/getData/?key=friends)
