import controll_origin
from controll_origin import Out_Mode, Home_Mode, Axis_Num, Logic_Flag

myController = controll_origin.Controller()

statue_dict = {
    20: 'ALM 无效时作为通用输入口',
    19: '不能使能为通用输入信号',
    18: 'ALM4 无效时作为通用输入口',
    17: 'ORG4 无效时作为通用输入口',
    16: 'EL4-无效时作为通用输入口',
    15: 'EL4+无效时作为通用输入口',
    14: '不能使能为通用输入信号',
    13: 'ALM3 无效时作为通用输入口',
    12: 'ORG3 无效时作为通用输入口',
    11: 'EL3-无效时作为通用输入口',
    10: 'EL3+无效时作为通用输入口',
    9: '不能使能为通用输入信号',
    8: 'ALM2 无效时作为通用输入口',
    7: 'ORG2 无效时作为通用输入口',
    6: 'EL2-无效时作为通用输入口',
    5: 'EL2+无效时作为通用输入口',
    4: '不能使能为通用输入信号',
    3: 'ALM1 无效时作为通用输入口',
    2: 'ORG1 无效时作为通用输入口',
    1: 'EL1-无效时作为通用输入口',
    0: 'EL1+无效时作为通用输入口',
}


class Encapsulation():

    def __init__(self):
        self.cardno = self.initialize()

    def initialize(self):
        # auto_set返回值判断
        auto_set_rec = myController.auto_set()
        if (auto_set_rec == -1):
            raise Exception("错误:auto_set调用失败")

        elif (auto_set_rec == 0):
            raise Exception("错误:无法检测到控制卡")

        elif (auto_set_rec < 4 and auto_set_rec > 0):
            raise Exception(f"错误:已检测到{auto_set_rec}轴,非已知4轴")
        else:
            print("已检测到{0}轴,无误".format(auto_set_rec))

        # init_board返回值判断
        init_board_rec = myController.init_board()
        if (init_board_rec == -1):
            raise Exception("错误:init_board初始化失败")

        elif (init_board_rec == 0):
            raise Exception("错误:无法检测到控制卡")

        else:
            print("已检测到{0}卡，无误".format(init_board_rec))

        # 用户板卡编号,在仅有唯一卡时该函数可读取其ID
        return myController.check_IC(1)

    def set_Board_Mode(self, num):

        '''
        使限位传感器等必要模式使能
        '''

        '''
        设置回原点模式为模式0
        0：检测到原点接近开关信号轴立即停止运动；
        1：检测到出现编码器 Z 相脉冲信号时立即停止运动。
        2：梯形速度模式下，检测到原点接近开关信号有效时控制轴按
        快速运动方式设置的加速度逐渐减速停止；
        3：梯形速度模式下，原点信号有效时，控制轴按快速运动方式
        设置的加速度逐渐减速至低速，直到 Z 脉冲有效立即停止运动。
        '''
        home_mode = Home_Mode.Home_Mode_0.value
        statue = myController.set_home_mode(num, home_mode)
        if statue == -1:
            raise Exception("错误:set_home_mode回原点运动模式设置失败")

        # ------------------------------------------------------------------

        '''
        设置运动模式为脉冲方向
        1 为脉冲／方向方式，
        0 为双脉冲方式,
        这里设置为双脉冲模式，
        且第三个参数没有
        '''
        out_mode = Out_Mode.Pluse_Dir.value
        statue = myController.set_outmode(num, out_mode, 0)
        if statue == -1:
            raise Exception("错误:set_outmode运动模式设置失败")

        # ------------------------------------------------------------------
        '''
        外部报警信号
        '''
        self.check_alarm(num)

        # ------------------------------------------------------------------
        '''
        检查指定轴的限位信号是否有效
        '''
        flag = Logic_Flag.HIGH.value
        statue = myController.set_el_logic(num, flag)
        if statue == -1:
            raise Exception("错误:set_alm_logic外部报警信号有限点电平使能失败")

        flag = Logic_Flag.HIGH.value
        statue = myController.enable_el(num, flag)
        if statue == -1:
            raise Exception("错误:enable_alm外部报警信号使能失败")
        else:
            self.check_limit(num)

        # ------------------------------------------------------------------
        # ====
        '''
        set_org_logic用于设置一个轴原点信号是高电平有效还是低电平有效。
        1 表示外部限位开关高电平触发控制器；
        0 表示外部限位开关低电平触发控制器。
        '''
        flag = Logic_Flag.LOW.value
        statue = myController.set_org_logic(num, flag)
        if statue == -1:
            raise Exception("错误:set_org_logic外部原点信号有限点电平使能失败")

        # 指定轴的原点信号是否有效
        flag = Logic_Flag.HIGH.value
        statue = myController.enable_org(num, flag)
        if statue == -1:
            raise Exception("错误:enable_org外部原点信号使能失败")
        else:
            self.check_home(num)

        # ------------------------------------------------------------------

        '''
        set_card_alm_logic用于设置板卡报警信号是高电平有效还是低电平有效。
        1 表示外部限位开关高电平触发控制器；
        0 表示外部限位开关低电平触发控制器。
        '''
        flag = Logic_Flag.HIGH.value
        statue = myController.set_card_alm_logic(self.cardno, flag)
        if statue == -1:
            raise Exception("错误:set_card_alm_logic板卡报警信号有限点电平使能失败")

        flag = Logic_Flag.LOW.value
        statue = myController.enable_card_alm(self.cardno, flag)
        if statue == -1:
            raise Exception("错误:enable_card_alm板卡报警信号使能失败")
        else:
            # pass
            self.check_card_alarm()

    def get_cur_dir(self, num):
        '''
        用于获取轴的当前运动方向。
        '''
        statue = myController.get_cur_dir(num)
        if statue == -1:
            raise Exception("错误:get_cur_dir运行异常")
        elif statue == -1:
            print("当前运动方向负向")
        elif statue == 1:
            print("当前运动方向正向")
        else:
            print("运动停止")

    def get_rate(self, num):
        '''
        获取当前某个轴的实际运动速度
        单位：每秒脉冲数（pps）
        '''
        statue = myController.get_rate(num)
        if statue == -1:
            raise Exception("错误:get_rate运行异常")
        else:
            print(f"{num}轴速度为{statue}")

    def check_status(self, num):
        '''
        用于查询轴的工作状态。轴状态字
        各位的含义见表 6-2。只有在调用“enable_org”、“enable_limit”、
        “enable_alm”、“enable_card_alm”等指令使相应专用信号使能，
        才能返回正确的专用输入口状态。
        '''
        statue = myController.check_status(num)
        if statue == -1:
            raise Exception("check_status运行异常")
        else:
            print(statue)

    def check_limit(self, num):
        '''
        检查指定轴的限位信号是否有效
        num：所检查的轴号；
        '''
        statue = myController.check_limit(num)
        if statue == 0:
            print(f"错误:{num}轴限位信号无效")
        elif statue == -3:
            raise Exception("错误:check_limit运行异常")
        elif statue == 1:
            print(f'{num}轴正限位信号有效')
        elif statue == -1:
            print(f'{num}轴负限位信号有效')
        else:
            print(f'{num}轴正负限位信号都有效')

    def check_home(self, num):
        '''
        检查指定轴的原点信号是否有效
        check_home 用于检测指定轴的原点信号是否有效，只有在调用
        “enable_org”指令使相应专用信号使能，才能返回正确的专用输
        入口状态。
        '''
        statue = myController.check_home(num)
        if statue == 0:
            print(f'{num}轴原点信号无效')
        elif statue == -3:
            raise Exception("错误:check_home运行异常")
        else:
            print(f'{num}轴原点信号有效')

    def check_alarm(self, num):
        '''
        检查指定轴的报警信号是否有效
        '''
        statue = myController.check_alarm(num)
        if statue == 0:
            print(f"{num}轴报警信号正常")
        elif statue == -3:
            raise Exception("错误:check_alarm运行异常")
        else:
            print(f'{num}轴')

    def check_card_alarm(self):
        '''
        检查板卡的报警信号是否有效
        '''
        statue = myController.check_card_alarm(self.cardno)
        if statue == 0:
            raise Exception("错误:板卡报警信号无效")
        elif statue == -3:
            raise Exception("错误:check_card_alarm运行异常")
        else:
            print('板卡报警信号有效')

    def check_sfr(self):
        '''
        读取专用输入口所有的开关量状态
        状态位    专用信号    说明
         20       ALM       ALM 无效时作为通用输入口
        19        Z4        不能使能为通用输入信号
        18        ALM4      ALM4 无效时作为通用输入口
        17        ORG4      ORG4 无效时作为通用输入口
        16        EL4-      EL4-无效时作为通用输入口
        15        EL4+      EL4+无效时作为通用输入口
        14        Z3        不能使能为通用输入信号
        13        ALM3      ALM3 无效时作为通用输入口
        12        ORG3      ORG3 无效时作为通用输入口
        11        EL3-      EL3-无效时作为通用输入口
        10        EL3+      EL3+无效时作为通用输入口
        9         Z2        不能使能为通用输入信号
        8         ALM2      ALM2 无效时作为通用输入口
        7         ORG2      ORG2 无效时作为通用输入口
        6         EL2-      EL2-无效时作为通用输入口
        5         EL2+      EL2+无效时作为通用输入口
        4         Z1        不能使能为通用输入信号
        3         ALM1      ALM1 无效时作为通用输入口
        2         ORG1      ORG1 无效时作为通用输入口
        1         EL1-      EL1-无效时作为通用输入口
        0         EL1+      EL1+无效时作为通用输入口
        '''
        statue = myController.check_sfr(self.cardno)
        if statue == -1:
            raise Exception("错误:check_sfr运行异常")
        else:
            if type(statue) == list:
                for i in statue:
                    print(statue_dict[i])
            else:
                print(statue_dict[statue])

    def check_sfr_bit(self, bitno):
        '''
        读取专用输入口某位的开关量状态
        bitno：表示第几个输入口，取值范围为 1~21。
        '''
        statue = myController.check_sfr_bit(self.cardno, bitno)
        if statue == -1:
            raise Exception("错误:check_sfr_bit运行异常")
        elif statue == 1:
            print(f"{bitno}输入口处于高电平状态")
        else:
            print(f"{bitno}输入口处于低电平状态")

    def power_on(self):
        '''
        电机上电,给予电位0为上电
        '''
        res_1 = myController.outport_bit(self.cardno, Axis_Num.Axis_NO_1.value, 0)
        res_2 = myController.outport_bit(self.cardno, Axis_Num.Axis_NO_2.value, 0)

        if res_1 == -1 and res_2 == -1:
            raise Exception("错误:2个电机上电失败")
        elif res_1 == -1 and res_2 == 0:
            raise Exception("错误:电机1上电失败")
        elif res_1 == 0 and res_2 == -1:
            raise Exception("错误:电机2上电失败")
        else:
            print('2个电机上电成功')

    def power_off(self):
        '''
        电机下电,给予电位1为下电
        '''
        res_1 = myController.outport_bit(self.cardno, 1, 1)
        res_2 = myController.outport_bit(self.cardno, 2, 1)

        if res_1 == -1 and res_2 == -1:
            raise Exception("错误:2个电机下电失败")
        elif res_1 == -1 and res_2 == 0:
            raise Exception("错误:电机1下电失败")
        elif res_1 == 0 and res_2 == -1:
            raise Exception("错误:电机2下电失败")
        else:
            print('2个电机下电成功')

    def set_profile(self, num, low_speed=10000, high_speed=5000, acceleration=80000, deceleration=80000):
        '''
        设置快速运动的低速、高速和加速度
        '''
        res = myController.set_profile(num, low_speed, high_speed, acceleration, deceleration)
        if res == 0:
            print('T形模式的梯形速度的各参数值设置成功')
        else:
            raise Exception("错误:T形模式的梯形速度的各参数值设置失败")

    # 点位运动是指被控轴以各自的速度分别移动指定的距离，在到达目标位置时自动停止

    def fast_pmove(self, num, step):
        '''
        1 个轴以快速做点位运动
        '''
        res = myController.fast_pmove(num, step)
        if res == -1:
            raise Exception("错误:fast_pmove设运行异常")
        else:
            while True:
                res = myController.check_done(num)
                if res == 0:
                    break
                elif res == 1:
                    pass
                else:
                    raise Exception(f"错误:{num}轴运动异常")

    def con_pmove(self, num, step):
        '''
        1 个轴以常速做相对位置点位运动
        '''
        res = myController.con_pmove(num, step)
        if res == -1:
            raise Exception("错误:con_pmove设运行异常")
        else:
            while True:
                res = myController.check_done(num)
                if res == 0:
                    break
                elif res == 1:
                    pass
                else:
                    raise Exception(f"错误:{num}轴运动异常")

    def con_pmove2(self, num_1, step_1, num_2, step_2):
        '''
        2 个轴以常速做相对位置点位运动
        '''
        res = myController.con_pmove2(num_1, step_1, num_2, step_2)
        if res == -1:
            raise Exception("错误:con_pmove2设运行异常")
        else:
            while True:
                res_1 = myController.check_done(num_1)
                res_2 = myController.check_done(num_2)
                if res_1 == 0 and res_2 == 0:
                    break
                elif (res_1 == 1 and res_2 == 0) or (res_1 == 0 and res_2 == 1):
                    pass
                else:
                    raise Exception("错误:con_pmove2中轴运动异常")

    def fast_pmove2(self, num_1, step_1, num_2, step_2):
        '''
        2 个轴以快速做点位运动
        '''
        res = myController.con_pmove2(num_1, step_1, num_2, step_2)
        if res == -1:
            raise Exception("错误:fast_pmove2设运行异常")
        else:
            while True:
                res_1 = myController.check_done(num_1)
                res_2 = myController.check_done(num_2)
                if res_1 == 0 and res_2 == 0:
                    break
                elif (res_1 == 1 and res_2 == 0) or (res_1 == 0 and res_2 == 1):
                    pass
                else:
                    raise Exception("错误:fast_pmove2中轴运动异常")

    # 连续运动函数，连续运动是指被控轴以各自的速度按给定的方向一直运动，直到碰到限位开关或调用制动函数才会停止。

    def con_vmove(self, num, dir1):
        '''
        一个轴以常速做连续运动
        '''
        res = myController.con_vmove(num, dir1)
        if res == -1:
            raise Exception("错误:con_vmove运行异常")

    def con_vmove2(self, num_1, dir1, num_2, dir2):
        '''
        两个轴以常速做连续运动
        '''
        res = myController.con_vmove2(num_1, dir1, num_2, dir2)
        if res == -1:
            raise Exception("错误:con_vmove2设运行异常")

    def fast_vmove(self, num, dir1):
        '''
        一个轴以快速做连续运动
        '''
        res = myController.fast_vmove(num, dir1)
        if res == -1:
            raise Exception("错误:fast_vmove运行异常")

    def fast_vmove2(self, num_1, dir1, num_2, dir2):
        '''
        两个轴以快速做连续运动
        '''
        res = myController.fast_vmove2(num_1, dir1, num_2, dir2)
        if res == -1:
            raise Exception("错误:fast_vmove2设运行异常")

    # 回原点运动是指被控轴以各自的速度按给定的方向一直运动,直到碰到原点信号、限位开关或调用制动函数才会停止。

    def con_hmove(self, num, dir1):
        '''
        一个轴以常速做回原点运动
        '''
        res = myController.con_hmove(num, dir1)
        if res == -1:
            raise Exception("错误:con_hmove运行异常")

    def fast_hmove(self, num, dir1):
        '''
        一个轴以快速做回原点运动
        '''
        res = myController.fast_hmove(num, dir1)
        if res == -1:
            raise Exception("错误:fast_hmove运行异常")

    def con_hmove2(self, num1, dir1, num2, dir2):
        '''
        两个轴以常速做回原点运动
        '''
        res = myController.con_hmove2(num1, dir1, num2, dir2)
        if res == -1:
            raise Exception("错误:con_hmove2设运行异常")

    def fast_hmove2(self, num1, dir1, num2, dir2):
        '''
        两个轴以快速做回原点运动
        '''
        res = myController.fast_hmove2(num1, dir1, num2, dir2)
        if res == -1:
            raise Exception("错误:fast_hmove2设运行异常")

    '''
    -----------------------------------------------------------------------------------------------------------------------
                                                        下面函数还要调试
    '''

    # 插补运动函数，插补运动是指两轴或三轴按照一定的算法进行联动，被控轴同时启动，并同时到达目标位置。

    def con_line2(self, num1, pos1, num2, pos2):
        '''
        两个轴做常速直线运动
        '''
        res = myController.con_line2(num1, pos1, num2, pos2)
        if res == -1:
            raise Exception("错误:con_line2设运行异常")

    def fast_line2(self, num1, pos1, num2, pos2):
        '''
        两个轴做快速直线运动
        '''
        res = myController.fast_line2(num1, pos1, num2, pos2)
        if res == -1:
            raise Exception("错误:con_line2设运行异常")

    # 制动函数

    def sudden_stop(self, num):
        '''
        立即运动方式下，立即制动一个运动轴
        '''
        res = myController.sudden_stop(num)
        if res == -1:
            raise Exception("错误:sudden_stop设运行异常")

    def sudden_stop2(self, num1, num2):
        '''
        立即运动方式下，立即制动二个运动轴
        '''
        res = myController.sudden_stop2(num1, num2)
        if res == -1:
            raise Exception("错误:sudden_stop2设运行异常")

    def decel_stop(self, num):
        '''
        立即运动方式下，光滑制动一个运动轴
        '''
        res = myController.decel_stop(num)
        if res == -1:
            raise Exception("错误:decel_stop设运行异常")

    def decel_stop2(self, num1, num2):
        '''
        光滑制动二个运动轴
        '''
        res = myController.decel_stop2(num1, num2)
        if res == -1:
            raise Exception("错误:decel_stop2设运行异常")

    def move_pause(self, num):
        '''
        立即运动方式下，暂停一个运动轴
        '''
        res = myController.move_pause(num)
        if res == -1:
            raise Exception("错误:move_pause设运行异常")

    def move_resume(self, num):
        '''
        立即运动方式下，恢复一个运动轴的运动
        '''
        res = myController.move_resume(num)
        if res == -1:
            raise Exception("错误:move_resume设运行异常")

    def change_pos(self, num, pos):
        '''
        在相对位置模式下使用函数 change_pos 来动态改变目标位置。
        单轴点位运动过程中，在常速模式或梯形速度模式下，若用户发
        现发出的运动指令终点位置需要改变，可在该点位运动结束前或
        者结束后调用“change_pos”动态改变终点位置。系统将自动按
        新的终点位置运动。该终点位置以上一条用户发出的运动指令
        （fast_pmove、con_pmove）的起点为起点。可多次调用该函数
        来改变目标位置
        '''
        res = myController.change_pos(num, pos)
        if res == -1:
            raise Exception("错误:change_pos设运行异常")

    def set_backlash(self, num, backlash):
        '''
        设置由于机构换向形成间隙的补偿值
        backlash：由于机构换向形成的间隙值，单位为脉冲数，必须大于等于 0
        '''
        res = myController.set_backlash(num, backlash)
        if res == -1:
            raise Exception("错误:set_backlash设运行异常")

    def start_backlash(self, num):
        '''
        开始补偿由于机构换向间隙而导致的位置误差
        '''
        res = myController.start_backlash(num)
        if res == -1:
            raise Exception("错误:start_backlash设运行异常")

    def end_backlash(self, num):
        '''
        停止补偿由于机构换向间隙而导致的位置误差
        '''
        res = myController.end_backlash(num)
        if res == -1:
            raise Exception("错误:end_backlash设运行异常")

    def reset_pos(self, num):
        '''
        将指定轴的绝对位置和相对位置复位至 0，通常在
        轴的原点找到时调用，调用这个函数后，当前位置值变为 0，这
        以后，所有的绝对位置值均是相对于这一点的。
        '''
        res = myController.reset_pos(num)
        if res == -1:
            raise Exception("错误:reset_pos设运行异常")

    def set_s_curve(self, num, mode=0):
        '''
        设置轴的快速运动模式。
        mode：快速运动模式
            0—梯形加减速模式
            1—S 形加减速模式
        '''
        res = myController.set_s_curve(num, mode)
        if res == -1:
            raise Exception("错误:set_s_curve设运行异常")

    def set_s_section(self, num, accel_sec=100, decel_sec=200):
        '''
        设置轴的 S 形升降速的 S 段。
        accel_sec：S 形升速的 S 段升速值, 不能大于设置的高速的 1/2。
        decel_sec：S形减速的S段减速值, 不能大于设置的高速的1/2。
        '''
        res = myController.set_s_section(num, accel_sec, decel_sec)
        if res == -1:
            raise Exception("错误:set_s_section设运行异常")
