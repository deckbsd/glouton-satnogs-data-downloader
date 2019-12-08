from threading import Thread


def create_thread(target):
    thread = Thread(target=target)
    thread.daemon = True
    thread.start()
    return thread


def is_one_thread_alive(threads):
    for thread in threads:
        if thread.is_alive():
            return True

    return False


def wait(threads):
    while is_one_thread_alive(threads):
        for t in threads:
            # let's control to main thread every seconds (in order to be able to capture Ctrl + C if needed)
            t.join(1)
