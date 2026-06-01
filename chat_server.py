#   CHAT APPLICATION - SERVER SIDE
#   Oasis Infobyte Internship - Project 7


import socket
import threading
import datetime

HOST = '127.0.0.1'   # Localhost (apna hi computer)
PORT = 55555          # Port number

clients = []
usernames = []

def broadcast(message, sender_socket=None):
    """
    Sabhi connected clients ko message bhejo
    sender_socket ko message nahi bhejna (jo bhej raha hai)
    """
    timestamp = datetime.datetime.now().strftime("%H:%M")
    for client in clients:
        if client != sender_socket:
            try:
                client.send(f"[{timestamp}] {message}".encode('utf-8'))
            except:
                remove_client(client)

def send_to_all(message):
    """Sabhi clients ko message bhejo including sender"""
    timestamp = datetime.datetime.now().strftime("%H:%M")
    for client in clients:
        try:
            client.send(f"[{timestamp}] {message}".encode('utf-8'))
        except:
            remove_client(client)

def remove_client(client):
    """Client ko list se hatao"""
    if client in clients:
        index = clients.index(client)
        username = usernames[index]
        clients.remove(client)
        usernames.remove(username)
        send_to_all(f" SERVER: {username} chat se chala gaya!")
        print(f"    {username} disconnect hua")
        client.close()

def handle_client(client, address):
    """
    Har client ke liye alag thread mein chalega
    Client ke messages receive karega aur sabhi ko broadcast karega
    """
    try:
        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8').strip()

        if not username:
            username = f"User_{address[1]}"

        usernames.append(username)
        clients.append(client)

        print(f"   {username} join hua ({address[0]}:{address[1]})")
        print(f"    Total connected: {len(clients)}")

        client.send(f"\n  Aap chat mein aa gaye hain! Aap ka naam: {username}".encode('utf-8'))
        client.send(f" '/quit' type karein chat chodne ke liye\n".encode('utf-8'))

        broadcast(f"  {username} chat mein aa gaya! Swagat hai! ", client)

        while True:
            try:
                message = client.recv(1024).decode('utf-8')

                if not message:
                    break

                if message.lower() == '/quit':
                    break
                elif message.lower() == '/users':
                    user_list = ", ".join(usernames)
                    client.send(f"  Connected users: {user_list}".encode('utf-8'))
                elif message.lower() == '/help':
                    help_text = (
                        "\n  COMMANDS:\n"
                        "  /users  - Connected users dekhein\n"
                        "  /quit   - Chat chodein\n"
                        "  /help   - Yeh help dekhein\n"
                    )
                    client.send(help_text.encode('utf-8'))
                else:
                    full_message = f"  {username}: {message}"
                    print(f"    {username}: {message}")
                    broadcast(full_message, client)

            except ConnectionResetError:
                break
            except Exception as e:
                print(f"    Error from {username}: {e}")
                break

    except Exception as e:
        print(f"    Connection error: {e}")
    finally:
        remove_client(client)

def start_server():
    """Server start karo"""
    print("\n" + "="*55)
    print("    CHAT APPLICATION SERVER - Oasis Infobyte")
    print("="*55)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        server.listen(10)  

        print(f"   Server chalu ho gaya!")
        print(f"   Address: {HOST}:{PORT}")
        print(f"   Clients ka intezaar hai...")
        print(f"   Band karne ke liye Ctrl+C dabayein")
        print("="*55 + "\n")

        while True:
            try:
                client_socket, address = server.accept()
                print(f"\n    Naya connection: {address[0]}:{address[1]}")

                thread = threading.Thread(
                    target=handle_client,
                    args=(client_socket, address)
                )
                thread.daemon = True
                thread.start()

            except KeyboardInterrupt:
                print("\n\n    Server band ho raha hai...")
                break

    except OSError as e:
        print(f"    Server shuru nahi ho saka: {e}")
        print(f"    Shayad port {PORT} already use mein hai. Thodi der baad try karein.")
    finally:
        server.close()
        print("    Server band ho gaya. Allah Hafiz!\n")

if __name__ == "__main__":
    start_server()
