# fibbonacci using generator
def fibbonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
gen = fibbonacci()
for x in range(100):
    print(next(gen))