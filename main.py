from flask import Flask
from random import randint


app = Flask(__name__)
def my_calculator(self, x, y): return x + y

@app.route('/')
def randomcal():
  num1 = randint(0, 100)
  num2 = randint(0, 100)
  message = "{} + {} = {}!".format(num1, num2, my_calculator.add(num1, num2))
  return message

if __name__ == '__main__':
  app.run(host='0.0.0.0')
