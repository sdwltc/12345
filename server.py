import socket
# 定义一个检查端口是否有效的方法,Python中，方法必须写 mian 前面

def get_valid_port():
    while True:
        try:
            port = int(input("Enter port: "))

            # 检查端口是否在 0-65535 之间
            if 0 <= port <= 65535:
                return port

            else:
                print("Invalid port! Port must be between 0 and 65535.")

        except ValueError:
            print("Invalid port! Port must be an integer.")








# 类似 JAVA 的 method，定义一个函数
def start_server():
    """ 创建一个 TCP socket
                        .socket调用内置的 socket 函数,
                               socket.AF_INET 表示我们将使用 IPv4 地址
                                               socket.SOCK_STREAM 表示我们将使用 TCP 协议
     也就是说，我们创建了一个 TCP socket，它将使用 IPv4 地址，使用 TCP 协议
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 定义想要监听的地址
    # 全 0 表示监听所有地址，也就是通配符
    # HOST 就是地址名，任意定义，不过 host 更通用
    HOST = '0.0.0.0'

    # 定义想要监听的端口，让用户输入端口,调用检查是否是 valid 方法
    PORT = get_valid_port()

    # 把 socket绑定 到指定的地址和端口
    # bind告诉操作系统，让它把 socket 绑定到指定的地址和端口上
    # bind()方法的参数是一个元组,元组的第一个元素为地址,第二个元素为端口
    server_socket.bind((HOST, PORT))


    # 开始监听
    # listen()方法的参数是指定在拒绝连接之前，操作系统可以挂起的最大连接数量
    server_socket.listen(5)


    # 给个反馈，告诉用户我们已经开始监听
    # format()方法的作用是把字符串中的占位符 {} 替换成传入的参数
    print('Server listening on HOST {} : PORT {}'.format(HOST, PORT))



    # 无限循环，让服务器一直处于运行，等待客户端连接
    # True 常量在 Python 首字母大写，且表示它是一个常量，不可修改
    # 小写的 true 是变量名
    while True:
        # 引用client_socket object,告诉操作系统，我们接受客户端的连接
        # 调用accept()方法时，程序会停止运行，一直停在这里，直到有客户端与其建立连接，叫做阻塞
        # accept()方法返回一对元组，元组的第一个是新的 socket object，第二个是客户端的地址(IP 和 端口)
        # client_socket 是新的 socket object，用来与客户端通信
        client_socket, client_address = server_socket.accept()

        # 给个反馈，告诉用户我们已经接受了客户端的连接
        print(f"Client connected from {client_address}.")

        #  接收数据
        #  recv()方法接收数据，参数是要接收的最大数据量，单位是字节
        #  数据存 data 里
        data = client_socket.recv(1024)

        # 持续接收数据，直到数据为空
        while data:
            # 给个反馈，告诉用户我们已经接收到了数据
            # decode()方法把 bytes 对象转换成字符串
            print(f"Received {data.decode('utf-8')} from client {client_address}.")

            # 提示用户输入回复
            reply = input("Reply: ")

            # 发送回复
            # send()方法发送数据，参数是要发送的数据，是 bytes(字节) 对象，所以要用 encode()方法把字符串转换成 bytes 对象
            client_socket.send(reply.encode('utf-8'))

            # 给个反馈，告诉用户我们已经发送了回复
            print(f"Sent {reply} to client {client_address}.")

            # 继续接收数据
            data = client_socket.recv(1024)

        # 通信结束关闭 socket
        # close()方法关闭 socket
        client_socket.close()

        # 给个反馈，告诉用户我们已经关闭了 socket
        print(f"Client {client_address} disconnected.")



# 如果这个文件是被其他文件引用的，那么这个 if 语句就不会被执行
# 如果这个文件是直接被执行的，那么这个 if 语句就会被执行
if __name__ == '__main__':
    start_server()





