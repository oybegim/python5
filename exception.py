try:
    int(salom)
except NameError:
    print("integer son qabul qiladi")


try:
    a = 1
    a + "hello"
except TypeError:
    print("integerga string qo'shib bo'lmaydi")
    