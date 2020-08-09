import socket

def main():
    #创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #链接服务器
    server_ip = input("请输入要链接的服务器ip：")
    server_port = int(input("请输入要链接的服务器端口："))
    server_add = (server_ip,server_port)
    tcp_socket.connect(server_add)
    #发送/接收数据127
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("utf-8"))
    #关闭套接字
    tcp_socket.close()

if __name__ == '__main__':
    main()