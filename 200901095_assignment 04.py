from  threading import Thread

input_str=""
def input_string_thread():
    global input_str
    print("ENTER YOUR STRING")
    input_str = str(input())


def reverse_string_thread():
    print("THIS IS WILL SHOW THE RESULT OF THE STRING IN A REVERSED FORM")
    txt = input_str[::-1]
    print(txt)


def capital_string_thread():
    print("THIS WILL SHOW THE STRING IN UPPER CASE LETTERS ")
    y = input_str.upper()
    print(y)

def shift_string_thread():
    print("THIS WOULD SHIFT THE STRING")
    s = input_str
    shifted_s = ''
    for c in s:
        c_ascii = ord(c)  # get the ASCII value of the character
        c_ascii += 2  # shift the ASCII value by 2 positions
        shifted_c = chr(c_ascii)  # convert the ASCII value back to a character
        shifted_s += shifted_c  # add the shifted character to the result string
    print(shifted_s)



if __name__ == "__main__":
    thread1 = Thread(target=input_string_thread)
    thread2 = Thread(target=reverse_string_thread)
    thread3 = Thread(target=capital_string_thread)
    thread4 = Thread(target=shift_string_thread)

    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
    thread3.start()
    thread3.join()
    thread4.start()








