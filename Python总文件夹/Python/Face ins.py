

class House(object):
        def __init__(self, house_type, total_area, free_area,fur_list = None):
            self.house_type = house_type
            self.total_area = total_area
            self.free_area = free_area
            if fur_list == None: # 如果输入值为空的话   （默认值  但是不要直接把[]写在参数后面）
                self.fur_list = [] # 将列表设置成空列表



house1 = House('两室一厅',30,30)