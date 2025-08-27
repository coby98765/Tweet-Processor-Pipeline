
class Loader:
    @staticmethod
    def load_weapons():
        with open(r"..\data\weapon_list.txt", 'r') as f:
            weapon_list = []
            for line in f:
                weapon_list.append(line.lower())
            return weapon_list