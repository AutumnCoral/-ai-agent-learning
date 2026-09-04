#上下文管理器，语法糖：with ... as ...
class MyContextManager(object):
    def __enter__(self):
        print('enter')
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print('exit')
    def do_something(self):
        print('do something')
with MyContextManager() as manager:
    manager.do_something()