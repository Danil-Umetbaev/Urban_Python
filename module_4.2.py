def test_function():
    def inner_function():
        print("Я в области видимости функции 'test_function'!")
    inner_function()

test_function()
#inner_function()
#Ошибка связана с тем, что функция inner_funtion() видна ТОЛЬКО в простарнстве имён функции test_function()
