#! venv/bin/python
import socket
import network
import click

@click.group()
def main():
    pass

@click.command
@click.argument("wifi")
@click.argument("passw")
@click.argument("ip")
@click.argument("port")
@click.argument("text")
def client(wifi, ip, text, passw, port):
    print(f"{wifi}|{ip}|{text}|{passw}|{port}")
    print("setting up")
    sta_if=network.WLAN(network.STA_IF)
    sta_if.active(True)
    while not sta_if.isconnected():
        print("connectin")
        sta_if.connect(wifi,passw)
        time.sleep(0.5)
    print("connected")
    time.sleep(1)
    print("sending")
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.sendto(b"{0}".format(text),(ip,port))
    print("sent!")

@click.command()
@click.argument("ip")
@click.argument("port")
def server(ip, port):
    print (f"{ip}|{port}")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((f"{port}",port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print ("Connected by {0}".format(addr))
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
main.add_command(client)
main.add_command(server)
if __name__ == "__main__":
    main()
# By Cosita3cz
