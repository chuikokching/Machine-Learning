# This is a sample Python script.
import numpy as np
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_h(name,test):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name},{test}')  # Press ⌘F8 to toggle the breakpoint.
    for _ in range(10):
        print('BBBBB')
    print(np.random.random(1))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_h('GoGOGOGO','PyCharm')
    data = [i**2 for i in range(10)]
    print(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
