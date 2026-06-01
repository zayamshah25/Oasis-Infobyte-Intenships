#   CHAT APPLICATION - CLIENT SIDE
#   Oasis Infobyte Internship - Project 7


import socket
import threading
import sys


HOST = '127.0.0.1'
PORT = 55555

running = True

def receive_messages(client_socket):
    """
    Server se messages receive karta raho
    Alag thread mein chalega
    """
    global running
    while running:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == "USERNAME":
                pass
            elif message:
                print(f"\n{message}")
                print("Aap: ", end='', flush=True)
            else:
                print("\n    Server se connection toot gayi!")
                running = False
                break
        except ConnectionAbortedError:
            if running:
                print("\n    Connection toot gayi!")
            break
        except Exception as e:
            if running:
                print(f"\n   Error: {e}")
            break

def start_client():
    """Client start karo aur server se connect karo"""
    global running

    print("\n" + "="*55)
    print("     CHAT APPLICATION CLIENT - Oasis Infobyte")
    print("="*55)
    print(f"    Server se connect ho raha hai {HOST}:{PORT}...")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print("   Server se connect ho gaye!")
        print("="*55)

        while True:
            username = input("\n  👤  Apna naam daalen: ").strip()
            if username:
                break
            print("   Naam khali nahi ho sakta!")

        client_socket.send(username.encode('utf-8'))

        print("\n    Chat mein aa gaye hain!")
        print("   '/help' type karein commands dekhne ke liye")
        print("   '/quit' type karein bahar nikalne ke liye")
        print("="*55 + "\n")

        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,)
        )
        receive_thread.daemon = True
        receive_thread.start()

        while running:
            try:
                message = input("Aap: ").strip()

                if not message:
                    continue

                if message.lower() == '/quit':
                    client_socket.send('/quit'.encode('utf-8'))
                    print("\n    Chat se nikal rahe hain...")
                    running = False
                    break

                client_socket.send(message.encode('utf-8'))

            except KeyboardInterrupt:
                print("\n\n    Ctrl+C dabaya, bahar nikal rahe hain...")
                running = False
                break
            except Exception as e:
                if running:
                    print(f"\n     Message bhejne mein error: {e}")
                running = False
                break

    except ConnectionRefusedError:
        print(f"\n  Server se connect nahi ho saka!")
        print(f"   Kya aap ne chat_server.py pehle chalaya?")
        print(f"   Server {HOST}:{PORT} par chalu hona chahiye.\n")
        return
    except Exception as e:
        print(f"\n    Error: {e}\n")
        return
    finally:
        running = False
        try:
            client_socket.close()
        except:
            pass
        print("  Allah Hafiz!\n")

if __name__ == "__main__":
    start_client()
