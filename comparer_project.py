import mypredclass
import mobile_Object


z = mypredclass.predictclass()
ms = []
mp = []

choice = True

while (choice) :
    while (True) :
        print("\n\nwelcome to my phone comparer project, \nhere we are able to compare 2 phones with their price to see which one is worth it and which one is not")
        print('==========================================================================================')
        print("\n1. Start \n2. Exit")
        a = int(input("Please Input a choice >> "))
        
        if (a != 1 and a != 2) :
            print("\n\n" + "Please Input '1' or '2'")
            input("Press anything to continue..")
        else :
            break

    if a == 2 :
        choice = False
        continue
    
    print("input the spec")
    
    for x in range (0,2,1) :
        print('mobile ', x+1)
        bat = (input('battery power : '))
        clock = float(input('clock speed : '))
        dualsim = int(input('dual sim [0 = no || 1 = yes] : '))
        fc = int(input('Front Camera mega pixels : '))
        four_G = int(input('have 4G [0 = No || 1 = Yes] : '))
        inter_memo = int(input('internal Memory : '))
        m_dep = float(input('Mobile Depth in cm : '))
        m_weight = int(input('weight of mobile phone : '))
        n_cores = int(input('many cores : '))
        pc_cam = int(input('Primary cam MegaPixel : '))
        px_height = int(input('Pixel Resolution Height : '))
        px_width = int(input('Pixel Resolution Width : ') )
        ram = int(input('RAM : '))
        sch = int(input('Screen height : '))
        scw = int(input("Screen Width of mobile in cm : "))
        talk_time = int(input("longest time that a single battery charge will last when you are : "))
        three_G = int(input('has 3G [0 = No || 1 = Yes)] : '))
        touchscreen = int(input('Touch Screen [0 = No || 1 = Yes] : '))
        price = int(input("price : "))
        m = mobile_Object.Mobile(bat, clock,dualsim,fc, four_G, inter_memo, m_dep, m_weight, n_cores, pc_cam, px_height, px_width, ram, sch, scw, talk_time, three_G, touchscreen, price);
        
        ms.append(m);
        print('\n\n')

    for x in ms :
        mp.append(z.rfc.predict(m.returnval()));

    if (mp[0] < mp[1] ) :
        if (ms[0].price < ms[1].price) :
            print(' phone 1 is VERY WORTH IT')
        else :
            print('phone 1 is not worth it')
    if (mp[0] > mp[1]) :
        if (ms[0].price > ms[1].price):
            print('phone 1 is VERY WORTH IT')
        else:
            print('phone 1 is not worth it')
    else :
        if(ms[0].price > ms[1].price):
            print('phone 1 is not worth it')
        else :
            print("phone 1 is VERY WORTH IT")
else :
    print("Thank you for passing by, see you later :) ")

