import Developement_Code.python_controller.controller_base as base
import ctypes
import sys
import time

# parser = argparse.ArgumentParser(description='test')
# parser.add_argument('para1',type=int,help='test:parameter-1')

myController = base.Controller()

# CARDNO = myController.check_IC(1)  #用户板卡编号,在仅有唯一卡时该函数可读取其ID

# 初始化控制卡
def init_Board():
    # auto_set返回值判断
    auto_set_rec = myController.auto_set()
    if(auto_set_rec == -1):
        print("auto_set调用失败")
        return False
    elif(auto_set_rec == 0):
        print("无法检测到控制卡")
        return False
    elif(auto_set_rec < 4 and auto_set_rec > 0):
        print("已检测到{0}轴".format(auto_set_rec))
        return False
    else:
        print("已检测到{0}轴,无误".format(auto_set_rec))
    
    # init_board返回值判断
    init_board_rec = myController.init_board()
    if(init_board_rec == -1):
        print("init_board初始化失败")
        return False
    elif(init_board_rec == 0):
        print("无法检测到控制卡")
        return False
    else:
        print("已检测到{0}卡，无误".format(init_board_rec))

    return True

# 控制卡模式设置
def set_Board_Mode(Channel_Num,CARDNO):

    if (myController.outport_bit(CARDNO, 1, 0) == -1):
        print("电机上电失败")
        return False
    if (myController.outport_bit(CARDNO, 2, 0) == -1):
        print("电机上电失败")
        return False

    #设置回原点模式为模式0
    if(myController.set_home_mode(Channel_Num, base.Home_Mode.Home_Mode_0.value) == -1):
        print("回原点运动模式设置失败")
        return False


    # 设置运动模式为脉冲方向
    if(myController.set_outmode(Channel_Num, 1, 0) == -1):
        print("运动模式设置失败")
        return False


    #设置外部报警信号有效电平为高电平并使能
    if(myController.set_alm_logic(Channel_Num, 0) == -1):
        print("外部报警信号有限点电平使能失败")
        return False
    if(myController.enable_alm(Channel_Num, 0) == -1):
        print("外部报警信号使能失败")
        return False

    # 设置外部限位信号有效电平为高电平并使能
    if(myController.set_el_logic(Channel_Num, 1) == -1):
        print("外部限位信号有效电平设置失败")
        return False
    if(myController.enable_el(Channel_Num, 1) == -1):
        print("外部限位信号使能失败")
        return False

    #设置外部原点信号有效电平为高电平并使能
    if(myController.set_org_logic(Channel_Num, 0) == -1):
        print("外部原点信号有限点电平使能失败")
        return False

    if(myController.enable_org(Channel_Num, 1) == -1):
        print("外部原点信号使能失败")
        return False

    # 设置板卡报警信号有效电平为高电平并使能
    if(myController.set_card_alm_logic(CARDNO, 0) == -1):
        print("板卡报警信号有限点电平使能失败")
        return False
    if(myController.enable_card_alm(Channel_Num, 0) == -1):
        print("板卡报警信号使能失败")
        return False


    return True

def Power_On(CARDNO):
    '''
    电机上电
    :param CARDNO: 板卡号
    '''
    num1 = myController.outport_bit(CARDNO, 1, 0)
    num2 = myController.outport_bit(CARDNO, 2, 0)
    if num1 == -1 or num2 == -1:
        sys.exit()

def Power_Off(CARDNO):
    '''
    电机上电
    :param CARDNO: 板卡号
    '''
    num1 = myController.outport_bit(CARDNO, 1, 1)
    num2 = myController.outport_bit(CARDNO, 2, 1)
    if num1 == -1 or num2 == -1:
        sys.exit()



# 运动参数设置
def set_Motion_Mode():
    myController.set_maxspeed()
    # TODO

# 调用运动指令
def execute(Channel_Num,step):
    '''
    :param Channel_Num:轴数
    :param step:轴数运动距离
    '''
    myController.reset_pos(Channel_Num)
    myController.set_s_curve(Channel_Num, 0)
    myController.set_profile(Channel_Num, 10000, 50000, 80000, 80000)
    # myController.set_s_section(Channel_Num, 800, 800)
    myController.fast_pmove(Channel_Num, step)
    while True:
        num = myController.check_done(Channel_Num)
        if num == 0:
            break
        elif num == 1:
            pass
        else:
            sys.exit()

# 运动状态查询
def check_Motion_State():
    pass
    # myController
    # TODO


def main():
    # 初始化控制卡失败则退出测试系统
    if(init_Board() == False):
        print("请检查配置后重试")
        sys.exit(0)
    CARDNO = myController.check_IC(1)  # 用户板卡编号,在仅有唯一卡时该函数可读取其ID
    Channel_Num = base.Axis_Num.Axis_NO_1.value
    # 控制卡模式设置失败处理
    if(set_Board_Mode(Channel_Num,CARDNO) == False):
        print("请检查配置后重试")
        sys.exit(0)

    execute(1,1000)
    # 给电机下电
    myController.outport_bit(CARDNO, 1, 1)
    myController.outport_bit(CARDNO, 2, 1)


if __name__ == "__main__":
    main()
