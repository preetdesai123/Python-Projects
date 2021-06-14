
import math

def calculate_pi():
    '''
    Takes a natural number input from the user and
    prints out an estimate of pi upto that many decimal places

    Requires:
     input <= 15
    '''
    str_num = input("Enter a number: ")
    n = int(str_num)
    print(round(math.pi, n))

def main():
    calculate_pi()
main()
