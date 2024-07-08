import threading
import time


def calc_squares(numbers):
    print("square")
    for number in numbers:
        time.sleep(0.2)
        print("squares", number * number)


def calc_cubes(numbers):
    print("cubes")
    for number in numbers:
        time.sleep(0.2)
        print("cubes", number * number * number)


intial_time = time.time()
numbers = [1, 2, 3, 4, 5]
t1 = threading.Thread(target=calc_squares, args=(numbers,))
t2 = threading.Thread(target=calc_cubes, args=(numbers,))
print('Timetaken:', time.time() - intial_time)

t1.start()
t2.start()
t1.join()
t2.join()
