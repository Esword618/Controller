import ctypes
from ctypes import POINTER
from enum import Enum


class Controller(object):
    def __init__(self):
        self.__path = r'C:\Users\jiaxi\Documents\Jiaxin.Qian_personal\Controller\Developement_Code\python_controller\MPC08D.dll'  # 按照具体路径设置
        self.controller = ctypes.windll.LoadLibrary(self.__path)

    def auto_set(self):
        self.controller.auto_set.restype = ctypes.c_int
        return self.controller.auto_set()

    def init_board(self):
        self.controller.init_board.restype = ctypes.c_int
        return self.controller.init_board()

    # 属性设置
    def set_outmode(self, num, mode, outlogic):
        '''
        num：需要设置输出方式的控制轴。
        mode：脉冲输出模式设置（1 为脉冲／方向方式，0 为双脉冲方式）。
        outlogic：该参数在 AP88K 中无效。
        '''
        num = ctypes.c_int(num)
        mode = ctypes.c_int(mode)
        outlogic = ctypes.c_int(outlogic)
        self.controller.set_outmode.restype = ctypes.c_int
        return self.controller.set_outmode(num, mode, outlogic)

    def set_home_mode(self, num, home_mode):
        '''
        num：是所设置的轴；
        home_mode：回原点运动时检测原点信号的方式
        0：检测到原点接近开关信号轴立即停止运动；
        1：检测到出现编码器 Z 相脉冲信号时立即停止运动。
        2：梯形速度模式下，检测到原点接近开关信号有效时控制轴按
        快速运动方式设置的加速度逐渐减速停止；
        3：梯形速度模式下，原点信号有效时，控制轴按快速运动方式
        设置的加速度逐渐减速至低速，直到 Z 脉冲有效立即停止运动。
        '''
        num = ctypes.c_int(num)
        home_mode = ctypes.c_int(home_mode)
        self.controller.set_home_mode.restype = ctypes.c_int
        return self.controller.set_home_mode(num, home_mode)

    def set_dir(self, num, dir):
        num = ctypes.c_int(num)
        dir = ctypes.c_int(dir)
        self.controller.set_dir.restype = ctypes.c_int
        return self.controller.set_dir(num, dir)

    def enable_alm(self, num, flag):
        '''
        num：控制轴的编号。
        flag：外部报警信号是否有效的标志，1 表示使能外部报警信号；0 表示禁止外部报警信号。
        '''
        num = ctypes.c_int(num)
        flag = ctypes.c_int(flag)
        self.controller.enable_alm.restype = ctypes.c_int
        return self.controller.enable_alm(num, flag)

    def enable_el(self, num, flag):
        '''
        num：控制轴的编号。
        flag：外部限位信号是否有效的标志，1 表示使能外部限位信号；0 表示禁止外部限位信号。
        '''
        num = ctypes.c_int(num)
        flag = ctypes.c_int(flag)
        self.controller.enable_el.restype = ctypes.c_int
        return self.controller.enable_el(num, flag)

    def enable_org(self, num, flag):
        '''
        num：控制轴的编号。
        flag：外部原点信号是否有效的标志，1 表示使能外部原点信号；0 表示禁止外部原点信号。
        '''
        num = ctypes.c_int(num)
        flag = ctypes.c_int(flag)
        self.controller.enable_org.restype = ctypes.c_int
        return self.controller.enable_org(num, flag)

    def enable_card_alm(self, cardno, flag):
        '''
        cardno：板卡的编号。
        flag：板卡的外部报警信号是否有效的标志，1 表示使能外部报警信号；0 表示禁止外部报警信号。
        '''
        cardno = ctypes.c_int(cardno)
        flag = ctypes.c_int(flag)
        self.controller.enable_card_alm.restype = ctypes.c_int
        return self.controller.enable_card_alm(cardno, flag)

    def set_alm_logic(self, num, flag):
        '''
        num：所要设置的轴；
        flag：外部报警信号有效电平标志，1 表示外部报警开关高电平触发；0 表示外部报警开关低电平触发。
        '''
        num = ctypes.c_int(num)
        flag = ctypes.c_int(flag)
        self.controller.set_alm_logic.restype = ctypes.c_int
        return self.controller.set_alm_logic(num, flag)

    def set_el_logic(self, num, flag):
        '''
        num：控制轴的编号。
        flag：外部限位信号有效电平标志，1 表示外部限位开关高电平触发控制器；0 表示外部限位开关低电平触发控制器。
        '''
        num = ctypes.c_int(num)
        flag = ctypes.c_int(flag)
        self.controller.set_el_logic.restype = ctypes.c_int
        return self.controller.set_el_logic(num, flag)

    def set_org_logic(self, num, flag):
        '''
        ch：控制轴的编号。
        flag：外部原点信号有效电平标志，1 表示外部原点开关高电平触发控制器；0 表示外部原点开关低电平触发控制器。
        '''
        num = ctypes.c_int(num)
        flag = ctypes.c_int(flag)
        self.controller.set_org_logic.restype = ctypes.c_int
        return self.controller.set_org_logic(num, flag)

    def set_card_alm_logic(self, cardno, flag):
        '''
        cardno：板卡的编号。
        flag：外部报警信号有效电平标志，1 表示外部报警开关高电平触发控制器；0 表示外部报警开关低电平触发控制器。
        '''
        cardno = ctypes.c_int(cardno)
        flag = ctypes.c_int(flag)
        self.controller.set_card_alm_logic.restype = ctypes.c_int
        return self.controller.set_card_alm_logic(cardno, flag)

    # 运动参数设置
    def set_maxspeed(self, num, max_speed):
        num = ctypes.c_int(num)
        max_speed = ctypes.c_double(max_speed)
        self.controller.set_maxspeed.restype = ctypes.c_int
        return self.controller.set_maxspeed(num, max_speed)

    def set_conspeed(self, num, conspeed):
        num = ctypes.c_int(num)
        conspeed = ctypes.c_double(conspeed)
        self.controller.set_conspeed.restype = ctypes.c_int
        return self.controller.set_conspeed(num, conspeed)

    def set_profile(self, num, low_speed, high_speed, acceleration, deceleration):
        num = ctypes.c_int(num)
        low_speed = ctypes.c_double(low_speed)
        high_speed = ctypes.c_double(high_speed)
        acceleration = ctypes.c_double(acceleration)
        deceleration = ctypes.c_double(deceleration)
        self.controller.set_profile.restype = ctypes.c_int
        return self.controller.set_profile(num, low_speed, high_speed, acceleration, deceleration)

    def set_vector_conspeed(self, vec_conspeed):
        vec_conspeed = ctypes.c_double(vec_conspeed)
        self.controller.set_vector_conspeed.restype = ctypes.c_int
        return self.controller.set_vector_conspeed(vec_conspeed)

    def set_vector_profile(self, vec_vl, vec_vh, vec_ad, vec_dc):
        vec_vl = ctypes.c_double(vec_vl)
        vec_vh = ctypes.c_double(vec_vh)
        vec_ad = ctypes.c_double(vec_ad)
        vec_dc = ctypes.c_double(vec_dc)
        self.controller.set_vector_profile.restype = ctypes.c_int
        return self.controller.set_vector_profile(vec_vl, vec_vh, vec_ad, vec_dc)

    def set_s_curve(self, num, mode):
        num = ctypes.c_int(num)
        mode = ctypes.c_int(mode)
        self.controller.set_s_curve.restype = ctypes.c_int
        return self.controller.set_s_curve(num, mode)

    def set_s_section(self, num, accel_sec, decel_sec):
        num = ctypes.c_int(num)
        accel_sec = ctypes.c_double(accel_sec)
        decel_sec = ctypes.c_double(decel_sec)
        self.controller.set_s_section.restype = ctypes.c_int
        return self.controller.set_s_section(num, accel_sec, decel_sec)

    def set_abs_pos(self, num, pos):
        num = ctypes.c_int(num)
        pos = ctypes.c_double(pos)
        self.controller.set_abs_pos.restyps = ctypes.c_int
        return self.controller.set_abs_pos(num, pos)

    def reset_pos(self, num):
        num = ctypes.c_int(num)
        self.controller.reset_pos.restype = ctypes.c_int
        return self.controller.reset_pos(num)

    # 独立运动函数
    # (1)点位运动函数
    def con_pmove(self, num, step):
        num = ctypes.c_int(num)
        step = ctypes.c_double(step)
        self.controller.con_pmove.restype = ctypes.c_int
        return self.controller.con_pmove(num, step)

    def fast_pmove(self, num, step):
        num = ctypes.c_int(num)
        step = ctypes.c_double(step)
        self.controller.fast_pmove.restype = ctypes.c_int
        return self.controller.fast_pmove(num, step)

    def con_pmove2(self, num_1, step_1, num_2, step_2):
        num_1 = ctypes.c_int(num_1)
        step_1 = ctypes.c_double(step_1)
        num_2 = ctypes.c_int(num_2)
        step_2 = ctypes.c_double(step_2)
        self.controller.con_pmove2.restype = ctypes.c_int
        return self.controller.con_pmove2(num_1, step_1, num_2, step_2)

    def fast_pmove2(self, num_1, step_1, num_2, step_2):
        num_1 = ctypes.c_int(num_1)
        step_1 = ctypes.c_double(step_1)
        num_2 = ctypes.c_int(num_2)
        step_2 = ctypes.c_double(step_2)
        self.controller.fast_pmove2.restype = ctypes.c_int
        return self.controller.fast_pmove2(num_1, step_1, num_2, step_2)

    def con_pmove3(self, num_1, step_1, num_2, step_2, num_3, step_3):
        num_1 = ctypes.c_int(num_1)
        step_1 = ctypes.c_double(step_1)
        num_2 = ctypes.c_int(num_2)
        step_2 = ctypes.c_double(step_2)
        num_3 = ctypes.c_int(num_3)
        step_3 = ctypes.c_double(step_3)
        self.controller.con_pmove3.restype = ctypes.c_int
        return self.controller.con_pmove3(num_1, step_1, num_2, step_2, num_3, step_3)

    def fast_pmove3(self, num_1, step_1, num_2, step_2, num_3, step_3):
        num_1 = ctypes.c_int(num_1)
        step_1 = ctypes.c_double(step_1)
        num_2 = ctypes.c_int(num_2)
        step_2 = ctypes.c_double(step_2)
        num_3 = ctypes.c_int(num_3)
        step_3 = ctypes.c_double(step_3)
        self.controller.fast_pmove3.restype = ctypes.c_int
        return self.controller.fast_pmove3(num_1, step_1, num_2, step_2, num_3, step_3)

    def con_pmove4(self, num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4):
        num_1 = ctypes.c_int(num_1)
        step_1 = ctypes.c_double(step_1)
        num_2 = ctypes.c_int(num_2)
        step_2 = ctypes.c_double(step_2)
        num_3 = ctypes.c_int(num_3)
        step_3 = ctypes.c_double(step_3)
        num_4 = ctypes.c_int(num_4)
        step_4 = ctypes.c_double(step_4)
        self.controller.con_pmove4.restype = ctypes.c_int
        return self.controller.con_pmove4(num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4)

    def fast_pmove4(self, num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4):
        num_1 = ctypes.c_int(num_1)
        step_1 = ctypes.c_double(step_1)
        num_2 = ctypes.c_int(num_2)
        step_2 = ctypes.c_double(step_2)
        num_3 = ctypes.c_int(num_3)
        step_3 = ctypes.c_double(step_3)
        num_4 = ctypes.c_int(num_4)
        step_4 = ctypes.c_double(step_4)
        self.controller.fast_pmove4.restype = ctypes.c_int
        return self.controller.fast_pmove4(num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4)

    # (2)连续运动函数
    def con_vmove(self, num, dir1):
        num = ctypes.c_int(num)
        dir1 = ctypes.c_int(dir1)
        self.controller.con_vmove.restype = ctypes.c_int
        return self.controller.con_vmove(num, dir1)

    def fast_vmove(self, num, dir1):
        num = ctypes.c_int(num)
        dir1 = ctypes.c_int(dir1)
        self.controller.fast_vmove.restype = ctypes.c_int
        return self.controller.fast_vmove(num, dir1)

    def con_vmove2(self, num_1, dir1, num_2, dir2):
        num_1 = ctypes.c_int(num_1)
        dir1 = ctypes.c_int(dir1)
        num_2 = ctypes.c_int(num_2)
        dir2 = ctypes.c_int(dir2)
        self.controller.con_vmove2.restype = ctypes.c_int
        return self.controller.con_vmove2(num_1, dir1, num_2, dir2)

    def fast_vmove2(self, num_1, dir1, num_2, dir2):
        num_1 = ctypes.c_int(num_1)
        num_2 = ctypes.c_int(num_2)
        dir1 = ctypes.c_int(dir1)
        dir2 = ctypes.c_int(dir2)
        self.controller.fast_vmove2.restype = ctypes.c_int
        return self.controller.fast_vmove2(num_1, dir1, num_2, dir2)

    def con_vmove3(self, num_1, dir1, num_2, dir2, num_3, dir3):
        num_1 = ctypes.c_int(num_1)
        num_2 = ctypes.c_int(num_2)
        num_3 = ctypes.c_int(num_3)
        dir1 = ctypes.c_int(dir1)
        dir2 = ctypes.c_int(dir2)
        dir3 = ctypes.c_int(dir3)
        self.controller.con_vmove3.restype = ctypes.c_int
        return self.controller.con_vmove3(num_1, dir1, num_2, dir2, num_3, dir3)

    def fast_vmove3(self, num_1, dir1, num_2, dir2, num_3, dir3):
        num_1 = ctypes.c_int(num_1)
        num_2 = ctypes.c_int(num_2)
        num_3 = ctypes.c_int(num_3)
        dir1 = ctypes.c_int(dir1)
        dir2 = ctypes.c_int(dir2)
        dir3 = ctypes.c_int(dir3)
        self.controller.fast_vmove3.restype = ctypes.c_int
        return self.controller.fast_vmove3(num_1, dir1, num_2, dir2, num_3, dir3)

    def con_vmove4(self, num_1, dir1, num_2, dir2, num_3, dir3):
        num_1 = ctypes.c_int(num_1)
        num_2 = ctypes.c_int(num_2)
        num_3 = ctypes.c_int(num_3)
        dir1 = ctypes.c_int(dir1)
        dir2 = ctypes.c_int(dir2)
        dir3 = ctypes.c_int(dir3)
        self.controller.con_vmove4.restype = ctypes.c_int
        return self.controller.con_vmove4(num_1, dir1, num_2, dir2, num_3, dir3)

    def fast_vmove4(self, num_1, dir1, num_2, dir2, num_3, dir3, num_4, dir4):
        num_1 = ctypes.c_int(num_1)
        num_2 = ctypes.c_int(num_2)
        num_3 = ctypes.c_int(num_3)
        num_4 = ctypes.c_int(num_4)
        dir1 = ctypes.c_int(dir1)
        dir2 = ctypes.c_int(dir2)
        dir3 = ctypes.c_int(dir3)
        dir4 = ctypes.c_int(dir4)
        self.controller.fast_vmove4.restype = ctypes.c_int
        return self.controller.fast_vmove4(num_1, dir1, num_2, dir2, num_3, dir3, num_4, dir4)

    # (3)回原点函数
    def con_hmove(self, num, dir1):
        num = ctypes.c_int(num)
        dir1 = ctypes.c_int(dir1)
        self.controller.con_homove.restype = ctypes.c_int
        return self.controller.com_hmove(num, dir1)

    def fast_hmove(self, num, dir1):
        num = ctypes.c_int(num)
        dir1 = ctypes.c_int(dir1)
        self.controller.fast_hmove.restype = ctypes.c_int
        return self.controller.fast_hmove(num, dir1)

    def con_hmove2(self, num1, dir1, num2, dir2):
        num1 = ctypes.c_int(num1)
        dir1 = ctypes.c_int(dir1)
        num2 = ctypes.c_int(num2)
        dir2 = ctypes.c_int(dir2)
        self.controller.con_hmove2.restype = ctypes.c_int
        return self.controller.con_hmove2(num1, dir1, num2, dir2)

    def fast_hmove2(self, num1, dir1, num2, dir2):
        num1 = ctypes.c_int(num1)
        dir1 = ctypes.c_int(dir1)
        num2 = ctypes.c_int(num2)
        dir2 = ctypes.c_int(dir2)
        self.controller.fast_hmove2.restype = ctypes.c_int
        return self.controller.fast_hmove2(num1, dir1, num2, dir2)

    def con_hmove3(self, num1, dir1, num2, dir2, num3, dir3):
        num1 = ctypes.c_int(num1)
        dir1 = ctypes.c_int(dir1)
        num2 = ctypes.c_int(num2)
        dir2 = ctypes.c_int(dir2)
        num3 = ctypes.c_int(num3)
        dir3 = ctypes.c_int(dir3)
        self.controller.con_hmove3.restype = ctypes.c_int
        return self.controller.con_hmove3(num1, dir1, num2, dir2, num3, dir3)

    def fast_hmove3(self, num1, dir1, num2, dir2, num3, dir3):
        num1 = ctypes.c_int(num1)
        dir1 = ctypes.c_int(dir1)
        num2 = ctypes.c_int(num2)
        dir2 = ctypes.c_int(dir2)
        num3 = ctypes.c_int(num3)
        dir3 = ctypes.c_int(dir3)
        self.controller.fast_hmove3.restype = ctypes.c_int
        return self.controller.fast_hmove3(num1, dir1, num2, dir2, num3, dir3)

    def fast_hmove4(self, num1, dir1, num2, dir2, num3, dir3, num4, dir4):
        num1 = ctypes.c_int(num1)
        dir1 = ctypes.c_int(dir1)
        num2 = ctypes.c_int(num2)
        dir2 = ctypes.c_int(dir2)
        num3 = ctypes.c_int(num3)
        dir3 = ctypes.c_int(dir3)
        num4 = ctypes.c_int(num4)
        dir4 = ctypes.c_int(dir4)
        self.controller.fast_hmove3.restype = ctypes.c_int
        return self.controller.fast_hmove3(num1, dir1, num2, dir2, num3, dir3, num4, dir4)

    def con_hmove4(self, num1, dir1, num2, dir2, num3, dir3, num4, dir4):
        num1 = ctypes.c_int(num1)
        dir1 = ctypes.c_int(dir1)
        num2 = ctypes.c_int(num2)
        dir2 = ctypes.c_int(dir2)
        num3 = ctypes.c_int(num3)
        dir3 = ctypes.c_int(dir3)
        num4 = ctypes.c_int(num4)
        dir4 = ctypes.c_int(dir4)
        self.controller.con_hmove3.restype = ctypes.c_int
        return self.controller.con_hmove3(num1, dir1, num2, dir2, num3, dir3, num4, dir4)

    # 插补运动函数
    # (1)线性插补函数
    def con_line2(self, num1, pos1, num2, pos2):
        num1 = ctypes.c_int(num1)
        pos1 = ctypes.c_double(pos1)
        num2 = ctypes.c_int(num2)
        pos2 = ctypes.c_double(pos2)
        self.controller.con_line2.restype = ctypes.c_int
        return self.controller.con_line2(num1, pos1, num2, pos2)

    def fast_line2(self, num1, pos1, num2, pos2):
        num1 = ctypes.c_int(num1)
        pos1 = ctypes.c_double(pos1)
        num2 = ctypes.c_int(num2)
        pos2 = ctypes.c_double(pos2)
        self.controller.fast_line2.restype = ctypes.c_int
        return self.controller.fast_line2(num1, pos1, num2, pos2)

    def con_line3(self, num1, pos1, num2, pos2, num3, pos3):
        num1 = ctypes.c_int(num1)
        pos1 = ctypes.c_double(pos1)
        num2 = ctypes.c_int(num2)
        pos2 = ctypes.c_double(pos2)
        num3 = ctypes.c_int(num3)
        pos3 = ctypes.c_double(pos3)
        self.controller.con_line3.restype = ctypes.c_int
        return self.controller.con_line3(num1, pos1, num2, pos2, num3, pos3)

    def fast_line3(self, num1, pos1, num2, pos2, num3, pos3):
        num1 = ctypes.c_int(num1)
        pos1 = ctypes.c_double(pos1)
        num2 = ctypes.c_int(num2)
        pos2 = ctypes.c_double(pos2)
        num3 = ctypes.c_int(num3)
        pos3 = ctypes.c_double(pos3)
        self.controller.fast_line3.restype = ctypes.c_int
        return self.controller.fast_line3(num1, pos1, num2, pos2, num3, pos3)

    def con_line4(self, num1, pos1, num2, pos2, num3, pos3, num4, pos4):
        num1 = ctypes.c_int(num1)
        pos1 = ctypes.c_double(pos1)
        num2 = ctypes.c_int(num2)
        pos2 = ctypes.c_double(pos2)
        num3 = ctypes.c_int(num3)
        pos3 = ctypes.c_double(pos3)
        num4 = ctypes.c_int(num4)
        pos4 = ctypes.c_double(pos4)
        self.controller.con_line3.restype = ctypes.c_int
        return self.controller.con_line3(num1, pos1, num2, pos2, num3, pos3, num4, pos4)

    def fast_line4(self, num1, pos1, num2, pos2, num3, pos3, num4, pos4):
        num1 = ctypes.c_int(num1)
        pos1 = ctypes.c_double(pos1)
        num2 = ctypes.c_int(num2)
        pos2 = ctypes.c_double(pos2)
        num3 = ctypes.c_int(num3)
        pos3 = ctypes.c_double(pos3)
        num4 = ctypes.c_int(num4)
        pos4 = ctypes.c_double(pos4)
        self.controller.fast_line3.restype = ctypes.c_int
        return self.controller.fast_line3(num1, pos1, num2, pos2, num3, pos3, num4, pos4)

    # 制动函数
    def sudden_stop(self, num):
        num = ctypes.c_int(num)
        self.controller.sudden_stop.restype = ctypes.c_int
        return self.controller.sudden_stop(num)

    def sudden_stop2(self, num1, num2):
        num1 = ctypes.c_int(num1)
        num2 = ctypes.c_int(num2)
        self.controller.sudden_stop2.restype = ctypes.c_int
        return self.controller.sudden_stop(num1, num2)

    def sudden_stop3(self, num1, num2, num3):
        num1 = ctypes.c_int(num1)
        num2 = ctypes.c_int(num2)
        num3 = ctypes.c_int(num3)
        self.controller.sudden_stop3.restype = ctypes.c_int
        return self.controller.sudden_stop(num1, num2, num3)

    def sudden_stop4(self, num1, num2, num3, num4):
        num1 = ctypes.c_int(num1)
        num2 = ctypes.c_int(num2)
        num3 = ctypes.c_int(num3)
        num4 = ctypes.c_int(num4)
        self.controller.sudden_stop3.restype = ctypes.c_int
        return self.controller.sudden_stop(num1, num2, num3, num4)

    def decel_stop(self, num):
        num = ctypes.c_int(num)
        self.controller.decel_stop.restype = ctypes.c_int
        return self.controller.decel_stop(num)

    def decel_stop2(self, num1, num2):
        num1 = ctypes.c_int(num1)
        num2 = ctypes.c_int(num2)
        self.controller.decel_stop2.restype = ctypes.c_int
        return self.controller.decel_stop(num1, num2)

    def decel_stop3(self, num1, num2, num3):
        num1 = ctypes.c_int(num1)
        num2 = ctypes.c_int(num2)
        num3 = ctypes.c_int(num3)
        self.controller.decel_stop3.restype = ctypes.c_int
        return self.controller.decel_stop(num1, num2, num3)

    def decel_stop4(self, num1, num2, num3, num4):
        num1 = ctypes.c_int(num1)
        num2 = ctypes.c_int(num2)
        num3 = ctypes.c_int(num3)
        num4 = ctypes.c_int(num4)
        self.controller.decel_stop3.restype = ctypes.c_int
        return self.controller.decel_stop(num1, num2, num3, num4)

    def move_pause(self, num):
        num = ctypes.c_int(num)
        self.controller.move_pause.restype = ctypes.c_int
        return self.controller.move_pause(num)

    def move_resume(self, num):
        num = ctypes.c_int(num)
        self.controller.move_resume.restype = ctypes.c_int
        return self.controller.move_resume(num)

    # 数字IO操作函数
    def checkin_byte(self, cardno):
        cardno = ctypes.c_int(cardno)
        self.controller.checkin_byte.restype = ctypes.c_int
        return self.controller.checkin_byte(cardno)

    def checkin_bit(self, cardno, bitno):
        cardno = ctypes.c_int(cardno)
        bitno = ctypes.c_int(bitno)
        self.controller.checkin_bit.restype = ctypes.c_int
        return self.controller.checkin_bit(cardno, bitno)

    def outport_byte(self, cardno, bytedata):
        cardno = ctypes.c_int(cardno)
        bytedata = ctypes.c_int(bytedata)
        self.controller.outport_byte.restype = ctypes.c_int
        return self.controller.outport_byte(cardno, bytedata)

    def outport_bit(self, cardno, bitno, status):
        cardno = ctypes.c_int(cardno)
        bitno = ctypes.c_int(bitno)
        status = ctypes.c_int(status)
        self.controller.outport_bit.restype = ctypes.c_int
        return self.controller.outport_bit(cardno, bitno, status)

    def check_sfr(self, cardno):
        '''
        读取专用输入口所有的开关量状态
        其它：IO 状态
        -1：错误
        '''
        cardno = ctypes.c_int(cardno)
        self.controller.check_sfr.cardno.restype = ctypes.c_int
        return self.controller.check_sfr(cardno)

    def check_sfr_bit(self, cardno, bitno):
        '''
        cardno：卡编号，即用户设置的板卡本地 ID 号，取值范围从 1 到卡最大编号。
        bitno：表示第几个输入口，取值范围为 1~21。
        读取专用输入口某位的开关量状态
        0：低电平
        1：高电平
        -1：错误
        '''
        cardno = ctypes.c_int(cardno)
        bitno = ctypes.c_int(bitno)
        self.controller.check_sfr_bit.restype = ctypes.c_int
        return self.controller.check_sfr_bit(cardno, bitno)

    ## 特殊功能函数
    # (1)反向间隙补偿
    def set_backlash(self, num, backlash):
        num = ctypes.c_int(num)
        backlash = ctypes.c_double(backlash)
        self.controller.set_backlash.restype = ctypes.c_int
        return self.controller.set_backlash(num, backlash)

    def start_backlash(self, num):
        num = ctypes.c_int(num)
        self.controller.start_backlash.restype = ctypes.c_int
        return self.controller.start_backlash(num)

    def end_backlash(self, num):
        num = ctypes.c_int(num)
        self.controller.end_backlash.restype = ctypes.c_int
        return self.controller.end_backlash(num)

    # (2)动态改变目标位置
    def change_pos(self, num, pos):
        num = ctypes.c_int(num)
        pos = ctypes.c_double(pos)
        self.controller.change_pos.restype = ctypes.c_int
        return self.controller.change_pos(num, pos)

    # (3)可掉电保护数据区读写功能
    def write_password_flash(self, cardno, no, data, password):
        cardno = ctypes.c_int(cardno)
        no = ctypes.c_int(no)
        data = ctypes.c_int(data)
        password = ctypes.c_int(password)
        self.controller.write_password_flash.restype = ctypes.c_int
        return self.controller.write_password_flash(cardno, no, data, password)

    def read_password_flash(self, cardno, no, data, password):
        cardno = ctypes.c_int(cardno)
        no = ctypes.c_int(no)
        data = ctypes.c_int(data)
        password = ctypes.c_int(password)
        self.controller.read_password_flash.restype = ctypes.c_int
        return self.controller.read_password_flash(cardno, no, data, password)

    def clear_password_flash(self, cardno, password):
        cardno = ctypes.c_int(cardno)
        password = ctypes.c_int(password)
        self.controller.clear_password_flash.restype = ctypes.c_int
        return self.controller.clear_password_flash(cardno, password)

    def write_flash(self, cardno, piece, no, data):
        cardno = ctypes.c_int(cardno)
        piece = ctypes.c_int(piece)
        no = ctypes.c_int(no)
        data = ctypes.c_int(data)
        self.controller.write_flash.restype = ctypes.c_int
        return self.controller.write_flash(cardno, piece, no, data)

    def read_flash(self, cardno, piece, no, password):
        cardno = ctypes.c_int(cardno)
        piece = ctypes.c_int(piece)
        no = ctypes.c_int(no)
        password = ctypes.c_int(password)
        self.controller.read_flash.restype = ctypes.c_int
        return self.controller.read_flash(cardno, piece, no, password)

    def clear_flash(self, cardno, piece):
        cardno = ctypes.c_int(cardno)
        piece = ctypes.c_int(piece)
        self.controller.clear_flash.restype = ctypes.c_int
        return self.controller.clear_flash(cardno, piece)

    # 位置和状态设置函数
    def get_max_axe(self):
        self.controller.get_max_axe.restype = ctypes.c_int
        return self.controller.get_max_axe()

    def get_board_num(self):
        self.controller.get_board_num.restype = ctypes.c_int
        return self.controller.get_board_num()

    def get_axe(self, board_no):
        self.controller.get_axe.argtyps = (ctypes.c_int)
        self.controller.get_axe.restype = ctypes.c_int
        return self.controller.get_axe(board_no)

    def check_IC(self, cardno):
        cardno = ctypes.c_int(cardno)
        self.controller.check_IC.restype = ctypes.c_int
        return self.controller.check_IC(cardno)

    def get_abs_pos(self, num, pos):
        self.controller.get_card_ver.argtyps = (ctypes.c_int, POINTER(ctypes.c_double))
        self.controller.get_abs_pos.restype = ctypes.c_int
        return self.controller.get_abs_pos(num, pos)

    def get_conspeed(self, num):
        num = ctypes.c_int(num)
        self.controller.get_conspeed.restype = ctypes.c_double
        return self.controller.get_conspeed(num)

    # 指针
    def get_profile(self, num, vl, vh, ad, dc):
        self.controller.get_card_ver.argtyps = (
           ctypes.c_int, POINTER(ctypes.c_double), POINTER(
                ctypes.c_double), POINTER(ctypes.c_double),POINTER(ctypes.c_double))
        self.controller.get_profile.argtyps = (
            ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
        self.controller.get_profile.restype = ctypes.c_int
        return self.controller.get_profile(num, vl, vh, ad, dc)

    def get_vector_conspeed(self):
        self.controller.get_vector_conspeed.restype = ctypes.c_double
        return self.controller.get_vector_conspeed()

    # 指针
    def get_vector_profile(self, vec_vl, vec_vh, vec_ad, vec_dc):
        self.controller.get_card_ver.argtyps = (
            POINTER(ctypes.c_double), POINTER(ctypes.c_double), POINTER(
                ctypes.c_double), POINTER(ctypes.c_double))
        self.controller.get_vector_profile.restype = ctypes.c_int
        return self.controller.get_vector_profile(vec_vl, vec_vh, vec_ad, vec_dc)

    def get_rate(self, num):
        num = ctypes.c_int(num)
        self.controller.get_rate.restype = ctypes.c_double
        return self.controller.get_rate(num)

    def get_cur_dir(self, num):
        num = ctypes.c_int(num)
        self.controller.get_cur_dir.restype = ctypes.c_int
        return self.controller.get_cur_dir(num)

    def check_status(self, num):
        '''
        函数 check_status 读取指定轴的状态。AP88K 控制器每个轴都有
        1 个 32 位（双字）的状态值，用于查询轴的工作状态。轴状态字
        各位的含义见表 6-2。只有在调用“enable_org”、“enable_limit”、
        “enable_alm”、“enable_card_alm”等指令使相应专用信号使能，
        才能返回正确的专用输入口状态。
        '''
        num = ctypes.c_int(num)
        self.controller.check_status.restype = ctypes.c_int
        return self.controller.check_status(num)

    def check_done(self, num):
        num = ctypes.c_int(num)
        self.controller.check_done.restype = ctypes.c_int
        return self.controller.check_done(num)

    def check_limit(self, num):
        '''
        检查指定轴的限位信号是否有效
        num：所检查的轴号；
        0：无效
        1：正限位信号有效
        -1：负限位信号有效
        2：正负限位信号均有效
        -3：错误
        '''
        num = ctypes.c_int(num)
        self.controller.check_limit.restype = ctypes.c_int
        return self.controller.check_limit(num)

    def check_home(self, num):
        '''
        检查指定轴的原点信号是否有效
        0：无效
        1：有效
        -3：错误
        '''
        num = ctypes.c_int(num)
        self.controller.check_home.restype = ctypes.c_int
        return self.controller.check_home(num)

    def check_alarm(self, num):
        '''
        检查指定轴的报警信号是否有效
        0：无效
        1：有效
        -3：错误
        '''
        num = ctypes.c_int(num)
        self.controller.check_alarm.restype = ctypes.c_int
        return self.controller.check_alarm(num)

    def check_card_alarm(self, num):
        '''
        检查板卡的报警信号是否有效
        0：无效
        1：有效
        -3：错误
        '''
        num = ctypes.c_int(num)
        self.controller.check_card_alarm.restype = ctypes.c_int
        return self.controller.check_card_alarm(num)

    def get_done_source(self, num, src):
        num = ctypes.c_int(num)
        src = ctypes.c_int(src)
        self.controller.get_done_source.restype = ctypes.c_int
        return self.controller.get_done_source(num, src)

    # 错误代码处理函数
    def get_err(self, index, data):
        index = ctypes.c_int(index)
        data = ctypes.c_int(data)
        self.controller.get_err.restype = ctypes.c_int
        return self.controller.get_err(index, data)

    def get_last_err(self):
        self.controller.get_last_err.restype = ctypes.c_int
        return self.controller.get_last_err()

    def reset_err(self):
        self.controller.reset_err.restype = ctypes.c_int
        return self.controller.reset_err()

    # 控制器版本获取函数
    def get_lib_ver(self, major, minor1, minor2):
        major = ctypes.c_int(major)
        minor1 = ctypes.c_int(minor1)
        minor2 = ctypes.c_int(minor2)
        self.controller.get_lib_ver.restype = ctypes.c_int
        return self.controller.get_lib_ver(major, minor1, minor2)

    def get_sys_ver(self, major, minor1, minor2):
        major = ctypes.c_int(major)
        minor1 = ctypes.c_int(minor1)
        minor2 = ctypes.c_int(minor2)
        self.controller.get_sys_ver.restype = ctypes.c_int
        return self.controller.get_sys_ver(major, minor1, minor2)

    def get_card_ver(self, cardno, type, major, minor1, minor2):
        self.controller.get_card_ver.argtyps = (
            POINTER(ctypes.c_int), POINTER(ctypes.c_int), POINTER(
                ctypes.c_int), POINTER(ctypes.c_int),
            POINTER(ctypes.c_int))
        self.controller.get_card_ver.restype = ctypes.c_int
        return self.controller.get_card_ver(cardno, type, major, minor1, minor2)


class Out_Mode(Enum):
    Double_Pluse = 0
    Pluse_Dir = 1


class Home_Mode(Enum):
    Home_Mode_0 = 0
    Home_Mode_1 = 1
    Home_Mode_2 = 2
    Home_Mode_3 = 3


class Axis_Num(Enum):
    Axis_NO_1 = 1
    Axis_NO_2 = 2
    Axis_NO_3 = 3
    Axis_NO_4 = 4


class Status(Enum):
    OFF = 0
    ON = 1


class Logic_Flag(Enum):
    LOW = 0
    HIGH = 1
