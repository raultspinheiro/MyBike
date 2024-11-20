from selmodule import available

print('======Welcome to the YAMAHA AIRLINES======')
url = str(input("Insert the 'yamaha-motor.eu' bike url that you want to see if it is available: "))

if available(url) == False:
    print("This model its not available")

else:
    
    print("This model its available")
    print(f"And it costs {available(url)}")
    
print('=========================================')