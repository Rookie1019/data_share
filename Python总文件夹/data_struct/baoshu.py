from data_opera import Queue
import turtle



def main():
    q = Queue()
    

    name = ['A','B','C','D','E','F','G','H','I','J']
    num = 7

    for i in name:
        q.enqueue(i)

     
    while q.size() > 1:
        for i in range(num):
            head = q.dequeue()
            q.enqueue(head)
        q.dequeue()
    print(q.size())
    return q.dequeue()

t = turtle.Turtle()






if __name__ == "__main__":
    x = main()
    print(x)
    