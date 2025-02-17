class Necromant:

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.energy = 0
        self.bones = 0
        self.gold = 0
        self.level = 0
        self.skeletons = {'waiter': 0,
                          'farmer': 0,
                          'defer': 0,
                          'attacker': 0}

    def add_enegry(self, change=1):
        self.energy += change

    def take_energy(self, change=1):
        self.energy -= change

    def add_bones(self, change):
        self.bones += change

    def take_bones(self, change):
        self.bones -= change

    def add_gold(self, change):
        self.bones += change

    def take_gold(self, change):
        self.bones -= change

    def get_skeletons(self, skeleton_type):
        if skeleton_type not in self.skeletons.keys():
            print('Error class Necromant get_skeletons')
        return self.skeletons[skeleton_type]

    def set_skeletons(self, skeleton_type, count):
        if skeleton_type not in self.skeletons.keys():
            print('Error class Necromant set_skeletons')
        self.skeletons[skeleton_type] = self.skeletons[skeleton_type] + count

    def lvlup(self):
        self.level += 1

    def set_lvl(self,lvl):
        self.level = lvl