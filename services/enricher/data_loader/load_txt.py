
class Loader:
    @staticmethod
    def load_weapons():
        with open(r".\data\weapon_list.txt", 'r') as f:
            weapons = f.read()
            weapon_list = weapons.split('\n')
            return weapon_list