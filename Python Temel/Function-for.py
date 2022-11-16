def cube(x):
    return x*x*x

res=cube(5)
print(res)

my_cube=cube

res=my_cube(5)
print(res)

print("type res:",type(res))
print("type my_cube:",type(my_cube))
print("type cube:",type(cube))

print("\n")
print("---------------------------------------")

def my_map(method, argument_list):
    result=list()
    for item in argument_list:
        result.append(method(item))
    return result

my_list=my_map(cube,[1,2,3,4,5,6,7,8])
print(my_list)

print("\n")

def create_logger(message):
    def log():
        print('Log Message: ' , message)
    return log # Return a function
my_logger=create_logger('Hello World')


print("type crate_logger:",type(create_logger))
print("type my_logger:",type(my_logger))
print("type my_logger:",type(my_logger))

print("\n")
print("---------------------------------------")

l=[1,2,3,4]

def apply(l,f):
    for i in range(len(l)):
        l[i]=f(l[i])

def kare(x):
    return x**2

print(apply(l,kare))
# çıktı none  verdi

print("\n")
print("---------------------------------------")

def apply_funcs(f_list,x):
    l=[]
    for f in f_list:
        l.append(f(x))
    return l
print(apply_funcs([kare,cube],5))