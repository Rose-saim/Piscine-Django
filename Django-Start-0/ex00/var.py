# var.py
def my_var():
    var1 = 42
    var2 = '42'
    var3 = 'quarante-deux'
    var4 = 42.0
    var5 = True
    var6 = [42]
    var7 = {42: 42}
    var8 = (42,)
    var9 = set()

    variables = [var1, var2, var3, var4, var5, var6, var7, var8, var9]

    for var in variables:
        print(f"{var} est de type {type(var)}")

if __name__ == '__main__':
    my_var()
