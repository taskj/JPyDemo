import socket

def main():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        #从键盘获取的数据的
        send_data = input("请输入要获取的数据：")

        if send_data == "exit":
            break

        #使用套接字首发数据
        udp_socket.sendto(send_data.encode("utf-8"),("127.0.0.1",8080))

    udp_socket.close()


if __name__ == '__main__':
    main()