import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args):
        return json.dumps(func(*args))
    return wrapped

@to_json
def get_data():
  return {
    'data': 42
  }

#print(get_data())
  
get_data()  # вернёт '{"data": 42}'
