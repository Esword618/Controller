from controll.controll_origin import Axis_Num
from controll.encapsulation import Encapsulation

base = Encapsulation()
numX = Axis_Num.Axis_NO_1.value
numY = Axis_Num.Axis_NO_2.value
# 上电
base.power_on()
# 1,2轴限位传感器设置
print('--------')
base.set_Board_Mode(numX)
print('--------')
# base.set_Board_Mode(numY)
# 运动
base.reset_pos(numX)
# 默认mode=0,为梯形加减速模式
base.set_s_curve(numX)
# set_profile(numX, 10000, 50000, 80000, 80000)默认
# base.set_profile(num=numX)
base.set_profile(numX, 10000, 50000, 80000, 80000)
base.fast_pmove(numX, -100000)


# 下电
base.power_off()
