import multiprocessing
from multiprocessing import Process, Pipe

def sender(conn, msg):
    """
    function to send messages to other end of pipe
    """
    for msg in msgs:
        conn.send(msg)
        print("Sent the message: {}".format(msg))
    conn.close()
  
def receiver(conn):
    """
    function to print the messages received from other
    end of pipe
    """
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))

def pipe():
    msg = ["save all"]

    #Creates the Pipe
    p_conn, c_conn = multiprocessing.Pipe()

    #The actual processes that get started
    p1 = multiprocessing.Process(target=sender, args=(p_conn,msg))
    p2 = multiprocessing.Process()
