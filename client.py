import socket

def start_client():
    # 创建 TCP socket 同 server 设定，IPV4 和 TCP 协议
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取用户想要链接的服务器的地址和端口
    HOST = input("Enter server IP address: ")
    PORT = int(input("Enter server port: "))

    # 连接到服务器
    client_socket.connect((HOST, PORT))

    # 给个反馈，告诉用户我们已经连接到服务器
    print("Connected to server at HOST {} : PORT {}".format(HOST, PORT))

    # 无限循环，让客户端一直处于运行，等待用户输入
    while True:
        # 获取用户输入的消息
        message = input("Enter message，exit to quit: ")

        # 如果用户输入 exit，就退出程序
        if message == 'exit':
            break

        # 发送消息到服务器
        client_socket.send(message.encode('utf-8'))

        # 接受服务器返回的消息
        reply = client_socket.recv(1024)

        # 打印服务器返回的消息
        print(f"Server replied: {reply.decode('utf-8')}")

    # 关闭 socket
    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_client()

