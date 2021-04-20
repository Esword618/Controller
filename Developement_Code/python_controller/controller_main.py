import controller_base
import argparse
import sys

# parser = argparse.ArgumentParser(description='test')
# parser.add_argument('para1',type=int,help='test:parameter-1')

myController=controller_base.Controller()

#初始化控制卡
def init_Board():
    auto_set_rec = myController.auto_set()
    init_board_rec = myController.init_board()

    #auto_set返回值判断
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
    
    #init_board返回值判断
    if(init_board_rec == -1):
        print("init_board初始化失败")
        return False 
    elif(init_board_rec == 0):
        print("无法检测到控制卡")
        return False
    else:
        print("已检测到{0}卡，无误".format(init_board_rec))
    
    return True

#控制卡模式设置
def set_Board_Mode(num, mode, home_mode):
    if(myController.set_outmode(num, mode, 0) == -1):
        return False
    if(myController.set_home_mode(num, home_mode) == -1):
        return False
    
    return True

#运动参数设置
def set_Motion_Mode():
    myController
    # TODO

#调用运动指令
def execute():
    myController
    # TODO

#运动状态查询
def check_Motion_State():
    myController
    # TODO


def main():

    #初始化控制卡失败则退出测试系统
    if(init_Board() == False):
        print("请检查配置后重试")
        sys.exit(0)

    #控制卡模式设置失败处理
    if(set_Board_Mode(controller_base.Axis_Num.Axis_NO_1, controller_base.Mode.double_Pluse, controller_base.Home_Mode.Home_Mode_0) == False):
        print("控制卡设置出错")
        #TODO
    

    


    






if __name__=="__main__":
    main()