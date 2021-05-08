# Mightyhive-challenge

## To deploy locally

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

4. ```python
python3 manage.py makemigrations
```

5. ```python
python3 manage.py migrate
```

6. Create the a model based on json.data file

```python
python3 manage.py shell < model_dump.py
```

#### Run app   at http://127.0.0.1:8000/

5. Execute:
```python
python3 manage.py runserver
```

## Testing
Execute:
```python
python3 manage.py Test
```

## Usage: REST Endpoint

1. Run app
2. Open any web browser you prefer.
3. Go to http://localhost:8000/getData/?key="key to search" (e.g. http://localhost:8000/getData/?key="friends")

