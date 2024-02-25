def f(x):
    return x**2-4
def df(x):
    return 2*x
x=1
f_x=f(x)
df_x=df(x)
print(f'f({x} = {f_x})')
print(f'df({x} = {df_x})')

for i in range(10):
    if df(x) == 0:
        print('df(x) is zero')
        break
    x -= f(x)/df(x)
    print(f'at i={i} x = {x}, f(x) ] {f(x)}')

print(f'final x = {x})')
