import threading

def square(num):
    print(f"Calculating square of {num}")
    square_val = num*num
    print(f"Square of {num} is {square_val}")

if __name__ == '__main__':
    threads = []
    for num in range(1, 11):
        t = threading.Thread(target=square, args=(num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print("All threads finished")

    # 该脚本创建了10个线程，每个线程计算一个数字的平方值。使用
    # `threading.Thread`
    # 类创建线程，并将
    # `square`
    # 函数作为目标函数传递给线程。在主线程中，启动所有线程，并等待它们完成。最后，打印一条消息，表示所有线程都已完成。