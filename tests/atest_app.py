import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)

from fizzbuzz import app

def test_fizzbuzz():
    assert app

def test_fizzbuzz_render_number():
    assert app.run(1) == 1

def test_fizzbuzz_render_zero():
    assert app.run(0) == 0

def test_fizzbuzz_render_three():
    assert app.run(3) == 'Fizz'

def test_fizzbuzz_render_six():
    assert app.run(6) == 'Fizz'

def test_fizzbuzz_render_twelve():
    assert app.run(12) == 'Fizz'

def test_fizzbuzz_render_five():
    assert app.run(5) == 'Buzz'

def test_fizzbuzz_render_50():
    assert app.run(50) == 'Buzz'

def test_fizzbuzz_render_100():
    assert app.run(100) == 'Buzz'

def test_fizzbuzz_render_15():
    assert app.run(15) == 'FizzBuzz'