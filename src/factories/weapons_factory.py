from ..objects import weapon

class WeaponsFactory:

    def get_weapon(self, type, level):

        config = self.get_weapon_config("rusty bike chains")

        return weapon.Weapon(config)

    def get_weapon_config(self, name):

        # will be loaded from dataRepo

        return {
            "name": "rusty bike chain",
            "type": weapon.WeaponType.MELEE,
            "weight": 1,
            "ammo": 1,
            "range": 1,
            "accuracy": 80,
            "damage" : 1
        }

wp = WeaponsFactory()

print(wp.get_weapon(1, 2))