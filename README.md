# Mightyhive-challenge

## Deploy locally

#### Prerequisites:
python3(3.6.9)

git

#### Instalation (step by step):

1. Execute:
```
git clone https://github.com/AgustinPardo/Mightyhive-challenge.git
```

2. Go inside "Mightyhive-challenge" folder:
```
cd Mightyhive-challenge
```

3. Execute:
```python
pip install -r requirements.txt
```

4. Execute:
```python
python manage.py makemigrations
```

5. Execute:
```python
python manage.py migrate
```

6. Populate the model based on json.data file:

```python
python manage.py shell < model_dump.py
```

#### Run app

5. Execute to run the app at http://127.0.0.1:8000/:
```python
python manage.py runserver
```

## Testing
Execute:
```python
python manage.py Test
```

## Usage: REST Endpoint

1. Run app
2. Open any web browser you prefer.
3. Go to http://localhost:8000/getData/?key= "key to search" (e.g. http://localhost:8000/getData/?key="friends")
