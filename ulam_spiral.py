import turtle

trt = turtle.Turtle()
trt.right(180)

s = 1

def isPrime(x):
    if (x==2):
        return True

    if(x % 2 == 0): 
        return False
    
    for i in range(2, x-1):
        if(x % i == 0):
            return False  
    return True

for i in range (1, 50):
    x = i * 20

    for z in range (2):
        for y in range (1,i):
            s += 1
            print(s)
            trt.forward(20)
            if (isPrime(s)):
                trt.circle(2)
                print('prime' + str(s))
                trt.write(str(s))

        trt.left(90)



turtle.done()