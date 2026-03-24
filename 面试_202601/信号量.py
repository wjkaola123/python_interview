import threading
import time

# Create a semaphore that allows a maximum of 3 threads to run concurrently
semaphore = threading.Semaphore(3)


def access_resource(thread_id):
    print(f"Thread {thread_id} attempting to acquire semaphore...")
    with semaphore:  # The 'with' statement handles acquire() and release() automatically
        print(f"Thread {thread_id} acquired semaphore, accessing resource...")
        time.sleep(2)  # Simulate work
        print(f"Thread {thread_id} releasing semaphore.")
    # The semaphore is released automatically when exiting the 'with' block


# Create and start 5 threads
threads = []
for i in range(1, 6):
    t = threading.Thread(target=access_resource, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads finished.")
