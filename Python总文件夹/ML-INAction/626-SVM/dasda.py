import multiprocessing, time, tkinter
class Spider:
    def __init__(self, root):
        self.root = root
        start_button = tkinter.Button(self.root, text="开始", font=('微软雅黑', 15), command=self.run)
        start_button.grid(row=0, column=1, columnspan=3, padx=30, pady=3, sticky='w')

    def print(self):
        for i in range(10000):
            print(i)
            time.sleep(1)

    def run(self):
        self.process_list = []
        for i in range(10):
            self.process_list.append(multiprocessing.Process(target=self.print, args=(i,)))
        print(self.process_list)
        for i in self.process_list:
            i.Daemon = True
            i.start()

if __name__ == '__main__':
    root = tkinter.Tk()
    spider = Spider(root)
    root.mainloop()