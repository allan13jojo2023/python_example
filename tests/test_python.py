import inspect
import unittest


class AutoLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'before call')
        result = self.func(*args, **kwargs)
        print('after call')
        return result


def log(func):
    def invoke(*args, **kwargs):
        print(f'before invoke {func.__name__}')
        result = func(*args, **kwargs)
        print('after invoke')
        return result

    return invoke


@log
def aaa(part):
    print(f'test {part}')


@AutoLogger
def bbb(part):
    print(f'bbb {part}')


class Something:
    val1 = 'aaa'
    def foo(self):
        print(f'val1 is {self.val1}')
        pass


for name, fn in inspect.getmembers(Something, inspect.isfunction):
    setattr(Something, name, log(fn))


class TestPython(unittest.TestCase):
    def test_1(self):
        print('test')
        engine = pyttsx3.init()
        # convert this text to speech
        text = "Python is a great programming language"
        engine.say(text)
        # play the speech
        engine.runAndWait()

    def test_2(self):
        aaa('1')
        bbb('test')
        a = Something()
        a.foo()
