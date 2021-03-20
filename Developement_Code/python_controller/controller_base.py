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
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
            ctypes.c_int)
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
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
            ctypes.c_int)
        self.controller.fast_hmove3.restype = ctypes.c_int
        return self.controller.fast_hmove3(num1, dir1, num2, dir2, num3, dir3, num4, dir4)

    def con_hmove4(self, num1, dir1, num2, dir2, num3, dir3, num4, dir4):
        self.controller.con_hmove3.argtyps = (
            ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
            ctypes.c_int)
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
    def checkin_byte(self, cardno):
        self.controller.checkin_byte.argtyps = (ctypes.c_int)
        self.controller.checkin_byte.restype = ctypes.c_int
        return self.controller.checkin_byte(cardno)

    def checkin_bit(self, cardno, bitno):
        self.controller.checkin_bit.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.checkin_bit.restype = ctypes.c_int
        return self.controller.checkin_bit(cardno, bitno)

    def outport_byte(self, cardno, bytedata):
        self.controller.outport_byte.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.outport_byte.restype = ctypes.c_int
        return self.controller.outport_byte(cardno, bytedata)

    def outport_bit(self, cardno, bitno, status):
        self.controller.utport_bit.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.utport_bit.restype = ctypes.c_int
        return self.controller.outport_bit(cardno, bitno, status)

    def check_sfr(self, cardno):
        self.controller.check_sfr.cardno.argtyps = (ctypes.c_int)
        self.controller.check_sfr.cardno.restype = ctypes.c_int
        return self.controller.check_sfr(cardno)

    def check_sfr_bit(self, cardno, bitno):
        self.controller.check_sfr_bit.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.check_sfr_bit.restype = ctypes.c_int
        return self.controller.check_sfr_bit(cardno, bitno)

        def checkin_byte(self, cardno):

            self.controller.checkin_byte.argtyps = (ctypes.c_int)
        self.controller.checkin_byte.restype = ctypes.c_int
        return self.controller.checkin_byte(cardno)

    def checkin_bit(self, cardno, bitno):
        self.controller.checkin_bit.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.checkin_bit.restype = ctypes.c_int
        return self.controller.checkin_bit(cardno, bitno)

    def outport_byte(self, cardno, bytedata):
        self.controller.outport_byte.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.outport_byte.restype = ctypes.c_int
        return self.controller.outport_byte(cardno, bytedata)

    def outport_bit(self, cardno, bitno, status):
        self.controller.utport_bit.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.utport_bit.restype = ctypes.c_int
        return self.controller.outport_bit(cardno, bitno, status)

    def check_sfr(self, cardno):
        self.controller.check_sfr.cardno.argtyps = (ctypes.c_int)
        self.controller.check_sfr.cardno.restype = ctypes.c_int
        return self.controller.check_sfr(cardno)

    def check_sfr_bit(self, cardno, bitno):
        self.controller.check_sfr_bit.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.check_sfr_bit.restype = ctypes.c_int
        return self.controller.check_sfr_bit(cardno, bitno)

    # 特殊功能函数
    # (1)反向间隙补偿
    def set_backlash(self, num, backlash):
        self.controller.set_backlash.argtyps = (ctypes.c_int, ctypes.c_double)
        self.controller.set_backlash.restype = ctypes.c_int
        return self.controller.set_backlash(num, backlash)

    def start_backlash(self, num):
        self.controller.start_backlash.argtyps = (ctypes.c_int)
        self.controller.start_backlash.restype = ctypes.c_int
        return self.controller.start_backlash(num)

    def end_backlash(self, num):
        self.controller.end_backlash.argtyps = (ctypes.c_int)
        self.controller.end_backlash.restype = ctypes.c_int
        return self.controller.end_backlash(num)

    # (2)动态改变目标位置
    def change_pos(self, num, pos):
        self.controller.change_pos.argtyps = (ctypes.c_int, ctypes.c_double)
        self.controller.change_pos.restype = ctypes.c_int
        return self.controller.change_pos(num, pos)

    # (3)可掉电保护数据区读写功能
    def write_password_flash(self, cardno, no, data, password):
        self.controller.write_password_flash.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.write_password_flash.restype = ctypes.c_int
        return self.controller.write_password_flash(cardno, no, data, password)

    def read_password_flash(self, cardno, no, data, password):
        self.controller.read_password_flash.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.read_password_flash.restype = ctypes.c_int
        return self.controller.read_password_flash(cardno, no, data, password)

    def clear_password_flash(self, cardno, password):
        self.controller.clear_password_flash.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.clear_password_flash.restype = ctypes.c_int
        return self.controller.clear_password_flash(cardno, password)

    def write_flash(self, cardno, piece, no, data):
        self.controller.write_flash.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.write_flash.restype = ctypes.c_int
        return self.controller.write_flash(cardno, piece, no, data)

    def read_flash(self, cardno, piece, no, password):
        self.controller.read_flash.argtyps = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.controller.read_flash.restype = ctypes.c_int
        return self.controller.read_flash(cardno, piece, no, password)

    def clear_flash(self, cardno, piece):
        self.controller.clear_flash.argtyps = (ctypes.c_int, ctypes.c_int)
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
        self.controller.check_IC.argtyps = (ctypes.c_int)
        self.controller.check_IC.restype = ctypes.c_int
        return self.controller.check_IC(cardno)

    def get_abs_pos(self, num, pos):
        self.controller.get_abs_pos.argtyps = (ctypes.c_int, ctypes.c_double)
        self.controller.get_abs_pos.restype = ctypes.c_int
        return self.controller.get_abs_pos(num, pos)

    def get_conspeed(self, num):
        self.controller.get_conspeed.argtyps = (ctypes.c_int)
        self.controller.get_conspeed.restype = ctypes.c_double
        return self.controller.get_conspeed(num)

    def get_profile(self, num, vl, vh, ad, dc):
        self.controller.get_profile.argtyps = (
        ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
        self.controller.get_profile.restype = ctypes.c_int
        return self.controller.get_profile(num, vl, vh, ad, dc)

    def get_vector_conspeed(self):
        self.controller.get_vector_conspeed.restype = ctypes.c_double
        return self.controller.get_vector_conspeed()

    def get_vector_profile(self, vec_vl, vec_vh, vec_ad, vec_dc):
        self.controller.get_vector_profile.argtyps = (
        ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)
        self.controller.get_vector_profile.restype = ctypes.c_int
        return self.controller.get_vector_profile(vec_vl, vec_vh, vec_ad, vec_dc)

    def get_rate(self, num):
        self.controller.get_rate.argtyps = (ctypes.c_int)
        self.controller.get_rate.restype = ctypes.c_double
        return self.controller.get_rate(num)

    def get_cur_dir(self, num):
        self.controller.get_cur_dir.argtyps = (ctypes.c_int)
        self.controller.get_cur_dir.restype = ctypes.c_int
        return self.controller.get_cur_dir(num)

    def check_status(self, num):
        self.controller.check_status.argtyps = (ctypes.c_int)
        self.controller.check_status.restype = ctypes.c_int
        return self.controller.check_status(num)

    def check_done(self, num):
        self.controller.check_done.argtyps = (ctypes.c_int)
        self.controller.check_done.restype = ctypes.c_int
        return self.controller.check_done(num)

    def check_limit(self, num):
        self.controller.check_limit.argtyps = (ctypes.c_int)
        self.controller.check_limit.restype = ctypes.c_int
        return self.controller.check_limit(num)

    def check_home(self, num):
        self.controller.check_home.argtyps = (ctypes.c_int)
        self.controller.check_home.restype = ctypes.c_int
        return self.controller.check_home(num)

    def check_alarm(self, num):
        self.controller.check_alarm.argtyps = (ctypes.c_int)
        self.controller.check_alarm.restype = ctypes.c_int
        return self.controller.check_alarm(num)

    def check_card_alarm(self, num):
        self.controller.check_card_alarm.argtyps = (ctypes.c_int)
        self.controller.check_card_alarm.restype = ctypes.c_int
        return self.controller.check_card_alarm(num)

    def get_done_source(self, num, src):
        self.controller.get_done_source.argtyps = (ctypes.c_int, ctypes.c_int)
        self.controller.get_done_source.restype = ctypes.c_int
        return self.controller.get_done_source(num, src)

    # 错误代码处理函数
    def get_err(self, index, data):
        self.controller.get_err.argtyps = (ctypes.c_int, ctypes.c_int)
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
