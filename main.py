import time

def background_task():
    # Your background task logic here
    print("Task started...")
    for i in range(0, 10 ):
        print('Imaginary task: ', i)
        time.sleep(1)
    print("Task completed!")