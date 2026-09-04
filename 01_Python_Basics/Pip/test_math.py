#测试：第一个测试
def add(a, b):
  return a + b 

#测试：第二个测试
def test_add():
  assert add(2, 3) == 5
  assert add(-1, 1) == 0
  assert add(0, 0) == 0

  def test_add_negative():
    assert add(-2, -3) == -5
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0