import mypredclass
import mobile_Object


z = mypredclass.predictclass()
# print(z.LR.predict([[2500,10,6,1,32,0.1,99,7,14,641,704,418,11,4,14,20,1,2], [2200,10,6,1,32,0.1,99,7,14,641,704,418,11,4,14,20,1,2]]))
ms = []
mp = []
print("input the spec")

for x in range (0,2,1) :
    print('mobile ', x+1)
    bat = input('battery power : ')
    clock = input('clock speed : ')
    dualsim = input('dual sim [0 = no || 1 = yes] : ')
    fc = input('Front Camera mega pixels : ')
    four_G = input('havef 4G [0 = No || 1 = Yes : ')
    inter_memo = input('internal Memory : ')
    m_dep = input('Mobile Depth in cm : ')
    m_weight = input('weight of mobile phone : ')
    n_cores = input('many cores : ')
    pc_cam = input('Primary cam MegaPixel : ')
    px_height = input('Pixel Resolution Height : ')
    px_width = input('Pixel Resolution Width : ') 
    ram = input('RAM : ')
    sch = input('Screen height : ')
    scw = input("Screen Width of mobile in cm : ")
    talk_time = input("longest time that a single battery charge will last when you are : ")
    three_G = input('has 3G [0 = No || 1 = Yes)] : ')
    touchscreen = input('Touch Screen : ')
    price = input("price : ")
    m = mobile_Object.Mobile(bat, clock,dualsim,fc, four_G, inter_memo, m_dep, m_weight, n_cores, pc_cam, px_height, px_width, ram, sch, scw, talk_time, three_G, touchscreen, price);
    
    ms.append(m);
    print('\n\n')

for x in ms :
    mp.append(z.LR.predict(x.returnval()));
    # mp.append(z.LR.predict([[x.batt, x.clock, x.dualsim, x.fc, x.four_G, x.inter_memo, x.m_dep,x.m_weight, x.n_cores, x.pc_cam,
    #              x.px_height, x.px_width, x.ram, x.sch, x.scw, x.talk_time, x.three_G, x.touchscreen]]))
    

if (mp[0] < mp[1] ) :
    if (ms[0].price < ms[1].price) :
        print('VERY WORTH IT')
    else :
        print('not worth it')
else :
    if (ms[0].price > ms[1].price):
        print(' VERY WORTH IT')
    else:
        print('not worth it')
