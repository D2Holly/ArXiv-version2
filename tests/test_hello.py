import app.hello as hello

class TestMain():
    def test_happy_path_true(self):
        result = hello.test_function(1)
        assert result is True
    
    def test_happy_path_false(self):
        result = hello.test_function(0)
        assert result is False

    def test_happy_path_error(self):
        result = hello.test_function('banana')
        assert result == 'Unknown error'

 