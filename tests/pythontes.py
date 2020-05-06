#Servo test

e1 = Entry(root)
e1.grid(row=0, column=1)

def cal():
    global dc
    
    deg = abs(float(deg1))
    dc = 0.056*deg + 2.5
    p.ChangeDutyCycle(dc)
    print(deg, dc)