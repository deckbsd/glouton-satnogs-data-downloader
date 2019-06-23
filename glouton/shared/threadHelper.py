from threading import Thread

def create_thread(target):
    thread = Thread(target=target)
    thread.daemon = True
    thread.start()
    return thread