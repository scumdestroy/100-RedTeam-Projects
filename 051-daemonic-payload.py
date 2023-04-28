import time
import daemon

def main():
    while True:
        # Replace the benign processes below with your demonic payload instead
        print("Daemon is running...")
        time.sleep(10)

if __name__ == '__main__':
    with daemon.DaemonContext():
        main()
