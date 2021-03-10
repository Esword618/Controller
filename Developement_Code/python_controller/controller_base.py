import ctypes
from ctypes import POINTER


class Controller(object):
    def __init__(self):
        self.__path = '.\DLL\MPC08D.dll'  # 按照具体路径设置
        self.controller = ctypes.windll.LoadLibrary(self.__path)

    def auto_set(self):
        self.controller.auto_set.restype = ctypes.c_int
        return self.controller.auto_set()

    def init_board(self):
        self.controller.init_board.restype = ctypes.c_int
        return self.controller.init_board()

    # 属性设置
    def set_outmode(self, num, mode, outlogic):
        self.controller.set_outmode.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.set_outmode.restype = ctypes.c_int
        return self.controller.set_outmode(num, mode, outlogic)

    def set_home_mode(self, num, home_mode):
        self.controller.set_home_mode.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.set_home_mode.restype = ctypes.c_int
        return self.controller.set_home_mode(num, home_mode)

    def set_dir(self, num, dir):
        self.controller.set_dir.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.set_dir.restype = ctypes.c_int
        return self.controller.set_dir(num, dir)

    def enable_alm(self, num, flag):
        self.controller.enable_alm.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.enable_alm.restype = ctypes.c_int
        return self.controller.enable_alm(num, flag)

    def enable_el(self, num, flag):
        self.controller.enable_el.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.enable_el.restype = ctypes.c_int
        return self.controller.enable_el(num, flag)

    def enable_org(self, num, flag):
        self.controller.enable_org.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.enable_org.restype = ctypes.c_int
        return self.controller.enable_org(num, flag)

    def enable_card_alm(self, cardno, flag):
        self.controller.enable_card_alm.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.enable_card_alm.restype = ctypes.c_int
        return self.controller.enable_card_alm(cardno, flag)

    def set_alm_logic(self, num, flag):
        self.controller.set_alm_logic.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.set_alm_logic.restype = ctypes.c_int
        return self.controller.set_alm_logic(num, flag)

    def set_el_logic(self, num, flag):
        self.controller.set_el_logic.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.set_el_logic.restype = ctypes.c_int
        return self.controller.set_el_logic(num, flag)

    def set_org_logic(self, num, flag):
        self.controller.set_org_logic.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.set_org_logic.restype = ctypes.c_int
        return self.controller.set_org_logic(num, flag)

    def set_card_alm_logic(self, num, flag):
        self.controller.set_card_alm_logic.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.set_card_alm_logic.restype = ctypes.c_int
        return self.controller.set_card_alm_logic(num, flag)

    # 运动参数设置
    def set_max_speed(self, num, max_speed):
        self.controller.set_max_speed.argtypes = (ctypes.c_int, ctypes.c_double)
        self.controller.set_max_speed.restype = ctypes.c_int
        return self.controller.set_max_speed(num, max_speed)

    def set_conspeed(self, num, conspeed):
        self.controller.set_conspeed.argtypes = (ctypes.c_int, ctypes.c_double)
        self.controller.set_conspeed.restype = ctypes.c_int
        return self.controller.set_conspeed(num, conspeed)

    def set_profile(self, num, low_speed, high_speed, acceleration, deceleration):
        self.controller.set_profile.argtypes = (
            ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
        self.controller.set_profile.restype = ctypes.c_int
        return self.controller.set_profile(num, low_speed, high_speed, acceleration, deceleration)

    def set_vector_conspeed(self, vec_conspeed):
        self.controller.set_vector_conspeed.argtypes = (ctypes.c_double)
        self.controller.set_vector_conspeed.restype = ctypes.c_int
        return self.controller.set_vector_conspeed(vec_conspeed)

    def set_vector_profile(self, vec_vl, vec_vh, vec_ad, vec_dc):
        self.controller.set_vector_profile.argtypes = (
            ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
        self.controller.set_vector_profile.restype = ctypes.c_int
        return self.controller.set_vector_profile(vec_vl, vec_vh, vec_ad, vec_dc)

    def set_s_curve(self, num, mode):
        self.controller.set_s_curve.argtypes = (ctypes.c_int, ctypes.c_int)
        self.controller.set_s_cureve.restype = ctypes.c_int
        return self.controller.set_s_curve(num, mode)

    def set_s_section(self, num, accel_sec, decel_sec):
        self.controller.set_s_section.argtypes = (ctypes.c_int, ctypes.c_double, ctypes.c_double)
        self.controller.set_s_section.restype = ctypes.c_int
        return self.controller.set_s_section(num, accel_sec, decel_sec)

    def set_abs_pos(self, num, pos):
        self.controller.set_abs_pos.argtypes = (ctypes.c_int, ctypes.c_double)
        self.controller.set_abs_pos.restyps = ctypes.c_int
        return self.controller.set_abs_pos(num, pos)

    def reset_pos(self, num):
        self.controller.reset_pos.argtypes = (ctypes.c_int)
        self.controller.reset_pos.restype = ctypes.c_int
        return self.controller.reset_pos(num)

    # 独立运动函数
    # (1)点位运动函数
    def con_pmove(self, num, step):
        self.controller.con_pmove.argtyps = (ctypes.c_int, ctypes.c_double)
        self.controller.con_pmove.restype = ctypes.c_int
        return self.controller.con_pmove(num, step)

    def fast_pmove(self, num, step):
        self.controller.fast_pmove.argtyps = (ctypes.c_int, ctypes.c_double)
        self.controller.fast_pmove.restype = ctypes.c_int
        return self.controller.fast_pmove(num, step)

    def con_pmove2(self, num_1, step_1, num_2, step_2):
        self.controller.con_pmove2.argtyps = (ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.con_pmove2.restype = ctypes.c_int
        return self.controller.con_pmove2(num_1, step_1, num_2, step_2)

    def fast_pmove2(self, num_1, step_1, num_2, step_2):
        self.controller.fast_pmove2.argtyps = (ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.fast_pmove2.restype = ctypes.c_int
        return self.controller.fast_pmove2(num_1, step_1, num_2, step_2)

    def con_pmove3(self, num_1, step_1, num_2, step_2, num_3, step_3):
        self.controller.con_pmove3.argtyps = (
            ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.con_pmove3.restype = ctypes.c_int
        return self.controller.con_pmove3(num_1, step_1, num_2, step_2, num_3, step_3)

    def fast_pmove3(self, num_1, step_1, num_2, step_2, num_3, step_3):
        self.controller.fast_pmove3.argtyps = (
            ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.fast_pmove3.restype = ctypes.c_int
        return self.controller.fast_pmove3(num_1, step_1, num_2, step_2, num_3, step_3)

    def con_pmove4(self, num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4):
        self.controller.con_pmove4.argtyps = (
            ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int,
            ctypes.c_double)
        self.controller.con_pmove4.restype = ctypes.c_int
        return self.controller.con_pmove4(num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4)

    def fast_pmove4(self, num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4):
        self.controller.fast_pmove4.argtyps = (
            ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int,
            ctypes.c_double)
        self.controller.fast_pmove4.restype = ctypes.c_int
        return self.controller.fast_pmove4(num_1, step_1, num_2, step_2, num_3, step_3, num_4, step_4)

    # (2)连续运动函数
    def con_vmove(self, num, dir1):
        self.controller.con_vmove.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.con_vmove.restype = ctypes.c_int
        return self.controller.con_vmove(num, dir1)

    def fast_vmove(self, num, dir1):
        self.controller.fast_vmove.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.fast_vmove.restype = ctypes.c_int
        return self.controller.fast_vmove(num, dir1)

    def con_vmove2(self, num_1, dir1, num_2, dir2):
        self.controller.con_vmove2.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.con_vmove2.restype = ctypes.c_int
        return self.controller.con_vmove2(num_1, dir1, num_2, dir2)

    def fast_vmove2(self, num_1, dir1, num_2, dir2):
        self.controller.fast_vmove2.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.fast_vmove2.restype = ctypes.c_int
        return self.controller.fast_vmove2(num_1, dir1, num_2, dir2)

    def con_vmove3(self, num_1, dir1, num_2, dir2, num_3, dir3):
        self.controller.con_vmove3.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.con_vmove3.restype = ctypes.c_int
        return self.controller.con_vmove3(num_1, dir1, num_2, dir2, num_3, dir3)

    def fast_vmove3(self, num_1, dir1, num_2, dir2, num_3, dir3):
        self.controller.fast_vmove3.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.fast_vmove3.restype = ctypes.c_int
        return self.controller.fast_vmove3(num_1, dir1, num_2, dir2, num_3, dir3)

    def con_vmove4(self, num_1, dir1, num_2, dir2, num_3, dir3):
        self.controller.con_vmove4.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.con_vmove4.restype = ctypes.c_int
        return self.controller.con_vmove4(num_1, dir1, num_2, dir2, num_3, dir3)

    def fast_vmove4(self, num_1, dir1, num_2, dir2, num_3, dir3, num_4, dir4):
        self.controller.fast_vmove4.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.fast_vmove4.restype = ctypes.c_int
        return self.controller.fast_vmove4(num_1, dir1, num_2, dir2, num_3, dir3, num_4, dir4)

    # (3)回原点函数
    def con_hmove(self, num, dir1):
        self.controller.con_hmove.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.con_homove.restype = ctypes.c_int
        return self.controller.com_hmove(num, dir1)

    def fast_hmove(self, num, dir1):
        self.controller.fast_hmove.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.fast_hmove.restype = ctypes.c_int
        return self.controller.fast_hmove(num, dir1)

    def con_hmove2(self, num1, dir1, num2, dir2):
        self.controller.con_hmove2.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.con_hmove2.restype = ctypes.c_int
        return self.controller.con_hmove2(num1, dir1, num2, dir2)

    def fast_hmove2(self, num1, dir1, num2, dir2):
        self.controller.fast_hmove2.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.fast_hmove2.restype = ctypes.c_int
        return self.controller.fast_hmove2(num1, dir1, num2, dir2)

    def con_hmove3(self, num1, dir1, num2, dir2, num3, dir3):
        self.controller.con_hmove3.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.con_hmove3.restype = ctypes.c_int
        return self.controller.con_hmove3(num1, dir1, num2, dir2, num3, dir3)

    def fast_hmove3(self, num1, dir1, num2, dir2, num3, dir3):
        self.controller.fast_hmove3.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.fast_hmove3.restype = ctypes.c_int
        return self.controller.fast_hmove3(num1, dir1, num2, dir2, num3, dir3)

    def fast_hmove4(self, num1, dir1, num2, dir2, num3, dir3, num4, dir4):
        self.controller.fast_hmove3.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.fast_hmove3.restype = ctypes.c_int
        return self.controller.fast_hmove3(num1, dir1, num2, dir2, num3, dir3, num4, dir4)

    def con_hmove4(self, num1, dir1, num2, dir2, num3, dir3, num4, dir4):
        self.controller.con_hmove3.argtyps = (
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.con_hmove3.restype = ctypes.c_int
        return self.controller.con_hmove3(num1, dir1, num2, dir2, num3, dir3, num4, dir4)

    # 插补运动函数
    # (1)线性插补函数
    def con_line2(self, num1, pos1, num2, pos2):
        self.controller.con_line2.argtyps = (ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.con_line2.restype = ctypes.c_int
        return self.controller.con_line2(num1, pos1, num2, pos2)

    def fast_line2(self, num1, pos1, num2, pos2):
        self.controller.fast_line2.argtyps = (ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.fast_line2.restype = ctypes.c_int
        return self.controller.fast_line2(num1, pos1, num2, pos2)

    def con_line3(self, num1, pos1, num2, pos2, num3, pos3):
        self.controller.con_line3.argtyps = (
        ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.con_line3.restype = ctypes.c_int
        return self.controller.con_line3(num1, pos1, num2, pos2, num3, pos3)

    def fast_line3(self, num1, pos1, num2, pos2, num3, pos3):
        self.controller.fast_line3.argtyps = (
        ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double)
        self.controller.fast_line3.restype = ctypes.c_int
        return self.controller.fast_line3(num1, pos1, num2, pos2, num3, pos3)

    def con_line4(self, num1, pos1, num2, pos2, num3, pos3, num4, pos4):
        self.controller.con_line3.argtyps = (
        ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int,
        ctypes.c_double)
        self.controller.con_line3.restype = ctypes.c_int
        return self.controller.con_line3(num1, pos1, num2, pos2, num3, pos3, num4, pos4)

    def fast_line4(self, num1, pos1, num2, pos2, num3, pos3, num4, pos4):
        self.controller.fast_line3.argtyps = (
        ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_int,
        ctypes.c_double)
        self.controller.fast_line3.restype = ctypes.c_int
        return self.controller.fast_line3(num1, pos1, num2, pos2, num3, pos3, num4, pos4)

    # 制动函数
    def sudden_stop(self, num):
        self.controller.sudden_stop.argtyps = (ctypes.c_int)
        self.controller.sudden_stop.restype = ctypes.c_int
        return self.controller.sudden_stop(num)

    def sudden_stop2(self, num1, num2):
        self.controller.sudden_stop2.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.sudden_stop2.restype = ctypes.c_int
        return self.controller.sudden_stop(num1, num2)

    def sudden_stop3(self, num1, num2, num3):
        self.controller.sudden_stop3.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.sudden_stop3.restype = ctypes.c_int
        return self.controller.sudden_stop(num1, num2, num3)

    def sudden_stop4(self, num1, num2, num3, num4):
        self.controller.sudden_stop3.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.sudden_stop3.restype = ctypes.c_int
        return self.controller.sudden_stop(num1, num2, num3, num4)

    def decel_stop(self, num):
        self.controller.decel_stop.argtyps = (ctypes.c_int)
        self.controller.decel_stop.restype = ctypes.c_int
        return self.controller.decel_stop(num)

    def decel_stop2(self, num1, num2):
        self.controller.decel_stop2.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.decel_stop2.restype = ctypes.c_int
        return self.controller.decel_stop(num1, num2)

    def decel_stop3(self, num1, num2, num3):
        self.controller.decel_stop3.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.decel_stop3.restype = ctypes.c_int
        return self.controller.decel_stop(num1, num2, num3)

    def decel_stop4(self, num1, num2, num3, num4):
        self.controller.decel_stop3.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.decel_stop3.restype = ctypes.c_int
        return self.controller.decel_stop(num1, num2, num3, num4)

    def dmove_pause(self, num):
        self.controller.move_pause.argtyps = (ctypes.c_int)
        self.controller.move_pause.restype = ctypes.c_int
        return self.controller.move_pause(num)

    def move_resume(self, num):
        self.controller.move_resume.argtyps = (ctypes.c_int)
        self.controller.move_resume.restype = ctypes.c_int
        return self.controller.move_resume(num)

    # 数字IO操作函数

    # 特殊功能函数
    # (1)反向间隙补偿

    # (2)动态改变目标位置

    # (3)可掉电保护数据区读写功能

    # 位置和状态设置函数

    # 错误代码处理函数

    # 控制器版本获取函数
    def get_lib_ver(self, major, minor1, minor2):
        self.controller.get_lib_ver.argtyps = (POINTER(ctypes.c_int), POINTER(ctypes.c_int), POINTER(ctypes.c_int))
        self.controller.get_lib_ver.restype = ctypes.c_int
        return self.controller.get_lib_ver(major, minor1, minor2)

    def get_sys_ver(self, major, minor1, minor2):
        self.controller.get_sys_ver.argtyps = (POINTER(ctypes.c_int), POINTER(ctypes.c_int), POINTER(ctypes.c_int))
        self.controller.get_sys_ver.restype = ctypes.c_int
        return self.controller.get_sys_ver(major, minor1, minor2)

    def get_card_ver(self, cardno, type, major, minor1, minor2):
        self.controller.get_card_ver.argtyps = (
            POINTER(ctypes.c_int), POINTER(ctypes.c_int), POINTER(ctypes.c_int), POINTER(ctypes.c_int),
            POINTER(ctypes.c_int))
        self.controller.get_card_ver.restype = ctypes.c_int
        return self.controller.get_card_ver(cardno, type, major, minor1, minor2)
