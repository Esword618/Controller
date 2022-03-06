
    # 特殊功能函数
    # (1)反向间隙补偿
    def set_backlash(self,num,backlash):
        num=ctypes.c_int(num)
        backlash=ctypes.c_double(backlash)
        self.controller.set_backlash.restype=ctypes.c_int
        return self.controller.set_backlash(num,backlash)
    def start_backlash(self,num):
        num=ctypes.c_int(num)
        self.controller.start_backlash.restype=ctypes.c_int
        return self.controller.start_backlash(num)
    def end_backlash(self,num):
        num=ctypes.c_int(num)
        self.controller.end_backlash.restype=ctypes.c_int
        return self.controller.end_backlash(num)

    # (2)动态改变目标位置
    def change_pos(self,num,pos):
        num=ctypes.c_int(num)
        pos=ctypes.c_double(pos)
        self.controller.change_pos.restype=ctypes.c_int
        return self.controller.change_pos(num,pos)

    # (3)可掉电保护数据区读写功能
    def write_password_flash(self,cardno,no,data,password):
        cardno=ctypes.c_int(cardno)
        no=ctypes.c_int(no)
        data=ctypes.c_int(data)
        password=ctypes.c_int(password)
        self.controller.write_password_flash.restype=ctypes.c_int
        return self.controller.write_password_flash(cardno,no,data,password)
    def read_password_flash(self,cardno,no,data,password):
        cardno = ctypes.c_int(cardno)
        no = ctypes.c_int(no)
        data = ctypes.c_int(data)
        password = ctypes.c_int(password)
        self.controller.read_password_flash.restype=ctypes.c_int
        return self.controller.read_password_flash(cardno,no,data,password)
    def clear_password_flash(self,cardno,password):
        cardno = ctypes.c_int(cardno)
        password = ctypes.c_int(password)
        self.controller.clear_password_flash.restype=ctypes.c_int
        return self.controller.clear_password_flash(cardno,password)
    def write_flash(self,cardno,piece,no,data):
        cardno = ctypes.c_int(cardno)
        piece = ctypes.c_int(piece)
        no = ctypes.c_int(no)
        data = ctypes.c_int(data)
        self.controller.write_flash.restype=ctypes.c_int
        return self.controller.write_flash(cardno,piece,no,data)
    def read_flash(self,cardno,piece,no,password):
        cardno=ctypes.c_int(cardno)
        piece = ctypes.c_int(piece)
        no=ctypes.c_int(no)
        password=ctypes.c_int(password)
        self.controller.read_flash.restype=ctypes.c_int
        return self.controller.read_flash(cardno,piece,no,password)
    def clear_flash(self,cardno,piece):
        cardno = ctypes.c_int(cardno)
        piece = ctypes.c_int(piece)
        self.controller.clear_flash.restype=ctypes.c_int
        return self.controller.clear_flash(cardno,piece)
