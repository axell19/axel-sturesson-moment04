K = float(input("Ange en temperatur i Kelvin "))

C = K-273.15

print(f"{K} Kelvin = {C:.2f} Celsius")


C = float(input("Ange en temperatur i Celsius"))

K = C+273.15

print(f"{C} Celsius = {K:.2f} Kelvin")


A = float(input("Hur många gånger åker du buss under en månad?"))

EB = A*30

MB = 775

print(f"Om du betalar engångsbiljett kostar det {EB}kr")

if EB > MB:
    print(f"Mer värt att köpa månadskort")

if MB > EB:
    print(f"Mer värt att köpa engångsbiljett")