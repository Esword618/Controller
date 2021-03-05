import ctypes

class Controller(object):
    def __init__(self):
        self.__path='./python_controller/MPC08D.dll'
        self.controller=ctypes.windll.LoadLibrary(self.__path)
    def auto_set(self):
        self.controller.auto_set.restype=ctypes.c_int
        return self.controller.auto_set()
    def init_board(self):
        self.controller.init_board.restype=ctypes.c_int
        return self.controller.init_board()
    def set_outmode(self):
        self.controller.set_outmode.restype=ctypes.c_int
        return self.controller.set_outmode
    def set_home_mode(self):
        self.controller.set_home_mode.restype=ctypes.c_int
        return self.controller.set_home_mode()
    def enable_alm(self):
        self.controller.enable_alm.restype=ctypes.c_int
        return self.controller.enable_alm()
    def enable_el(self):
        self.controller.enable_el.restype=ctypes.c_int
        return self.controller.enable_el()
    def enable_org(self):
        self.controller.enable_org.restype=ctypes.c_int
        return self.controller.enable_org()
    def enable_card_alm(self):
        self.controller.enable_card_alm.restype=ctypes.c_int
        return self.controller.enable_card_alm()
    def set_alm_logic(self):
        self.controller.set_alm_logic.restype=ctypes.c_int
        return self.controller.set_alm_logic()
    def set_el_logic(self):
        self.controller.set_el_logic.restype=ctypes.c_int
        return self.controller.set_el_logic()
    def set_org_logic(self):
        self.controller.set_org_logic.restype=ctypes.c_int
        return self.controller.set_org_logic()
    def set_card_alm_logic(self):
        self.controller.set_card_alm_logic.restype=ctypes.c_int
        return self.controller.set_card_alm_logic()


def main():
    myController=Controller()
    while True:
        axis_num=myController.auto_set()
        if axis_num==-1:
            print('auto_set: error')
        else:
            print('auto_set: OK')
            break
    while True:
        card_num=myController.init_board()
        if card_num==-1:
            print('init_borad: error')
        else:
            print('init_board: OK')
            break



if __name__=="__main__":
    main()

    


