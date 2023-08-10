class Movement:
    def __init__(self, id_from, id_to):
        self.id_to = None
        self.id_from = None
        self.set_id_from(id_from)
        self.set_id_to(id_to)

    def set_id_from(self, id):
        if 0 <= id <= 63:
            self.id_from = id
            return 0
        else:
            return 1
    
    def set_id_to(self, id):
        if 0 <= id <= 63:
            self.id_to = id
            return 0
        else:
            return 1
    
    def get_id_from(self):
        return self.id_from
    
    def get_id_to(self):
        return self.id_to
    