import controller_base
import argparse

# parser = argparse.ArgumentParser(description='test')
# parser.add_argument('para1',type=int,help='test:parameter-1')


def main():
    myController=controller_base.Controller()
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