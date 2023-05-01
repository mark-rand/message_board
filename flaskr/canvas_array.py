
class CanvasArray():
    """Alpha is the 'transparent' colour"""

    def __init__(self, height=11, alpha=-1):
        self.array = []
        self.height = height
        self.alpha = alpha

    def append(self, list_to_append):
        self.array.append(list_to_append)

    def write(self, list_to_write, position):
        if isinstance(list_to_write[0], list):
            for count, item in enumerate(list_to_write):
                self.write_single(item, position + count)
        else:
            self.write_single(list_to_write, position)

    def write_single(self, list_to_write, position):
        if position >= len(self.array):
            for x in range(len(self.array), position):
                self.array.append([self.alpha] * self.height)
            self.append(list_to_write)
        else:
            for x in range(len(self.array[position])):
                if list_to_write[x] != self.alpha:
                    self.array[position][x] = list_to_write[x]

    def get_bg_for_position(self, background, offset):
        if isinstance(background, list):
            return background[offset % len(background)]
        return background

    def bg_array(self, list_items, background, offset=0):
        b = []
        for position, item in enumerate(list_items):
            if isinstance(item, list):
                b.append(self.bg_array(item, background, position))
                offset += len(item)
            else:
                if item == self.alpha:
                    b.append(self.get_bg_for_position(background, position + offset))
                else:
                    b.append(item)
        return b

    def array_with_bg(self, background):
        return self.bg_array(self.array, background)
