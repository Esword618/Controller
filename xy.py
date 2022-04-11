from controll.controll_origin import Axis_Num
from controll.encapsulation import Encapsulation

x,y = 234,453  #x，y以实际为准

base = Encapsulation()
numY = Axis_Num.Axis_NO_2.value
numX = Axis_Num.Axis_NO_1.value
# 上电
base.power_on()
# 1,2轴限位传感器设置
print('----一轴限位传感器设置中----')
base.set_Board_Mode(numX)
print('----二轴限位传感器设置中----')
base.set_Board_Mode(numY)
#准备运动 xy轴绝对位置和相对位置复位至 0
base.reset_pos(numX)
base.reset_pos(numY)
# 设置轴的快速运动模式  默认mode=0,为梯形加减速模式
base.set_s_curve(numX)
base.set_s_curve(numY)
# 设置快速运动的低速、高速和加速度 默认为梯形加减速模式
# 默认low_speed=10000, high_speed=5000, acceleration=80000, deceleration=80000
base.set_profile(numX, 10000, 50000, 80000, 80000)
base.set_profile(numY, 10000, 50000, 80000, 80000)

#单轴移动
if x == 0 or y == 0:
    if x >= 10000:
        base.fast_pmove(numX,x)
    elif x <= 10000:
        base.con_pmove(numX,x)
    if y >= 10000:
        base.fast_pmove(numY,y)
    elif y <= 10000:
        base.con_pmove(numY,y)
    else:
        pass

# 两轴移动
if x >= 10000 and y >= 10000:
    base.fast_pmove2(numX,x,numY,y)
elif x >= 10000 and y <= 10000:
    base.fast_pmove(numX,x)
    base.con_pmove(numY,y)
elif x <= 10000 and y >= 10000:
    base.con_pmove(numX,x)
    base.fast_pmove(numY,y)
elif x <= 10000 and y <= 10000:
    base.fast_pmove2(numX,x,numY,y)
else:
    pass


# 回原点运动 调用hmove

# 连续运动  直到碰到限位开关或调用制动函数才会停止


# 运动结束 准备下电
base.power_off()

