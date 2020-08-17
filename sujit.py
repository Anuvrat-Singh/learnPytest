from multiprocessing import Process
def test1(ip):
    return str(ip) + "hello"
if __name__ == "__main__":
    p = Process(target=test1, args=([1,2,3,4,5],))
    p.start()
    p.join()