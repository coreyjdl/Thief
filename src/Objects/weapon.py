from enum import Enum

class WeaponType(Enum):
    MELEE = 1
    RANGE = 2
    PROJECTILE = 3
    RADIUS = 4

class Weapon(object):

    _name = None
    _type = None
    _weight = None
    _ammo = None
    _range = None
    _accuracy = None
    _damage = None

    def __init__(self, file):
        # move this process to a loader
        try:
            
            with open(file) as f:
                props = json.loads(f.read())

            self.name = props.name
            self.type = props.type
            self.weight = props.weight
            self.ammo = props.ammo
            self.range = props.range
            self.accuracy = props.accuracy
            self.damage = props.damage

        except:
            ...

    @property
    def name(self):
        ...

    @name.setter
    def name(self, x):
        if self._name:
            x = self._name

        self._name = x

    @name.getter
    def name(self):
        return self._name

    @property
    def type(self):
        ...
    
    @type.setter
    def type(self, x):
        if self._type:
            x = self._type

        self._type = x 

    @type.getter
    def type(self):
        return self._type 
    
    @property
    def weight(self):
        ...
    
    @weight.setter
    def weight(self, x):
        if self._weight:
            x = self._weight

        self._weight = x 

    @weight.getter
    def weight(self):
        return self._weight 
    
    @property
    def ammo(self):
        ...

    @ammo.setter
    def ammo(self, x):
        self._ammo = x 

    @ammo.getter
    def ammo(self):
        return self._ammo 

    @property
    def range(self):
        ...

    @range.setter
    def range(self, x):
        if self._range:
            x = self._range

        self._range = x 

    @range.getter
    def range(self):
        return self._range 

    @property
    def accuracy(self):
        ...

    @accuracy.setter
    def accuracy(self, x):
        if self._accuracy:
            x = self._accuracy

        self._accuracy = x 

    @accuracy.getter
    def accuracy(self):
        return self._accuracy 

    @property
    def damage(self):
        ...
    
    @damage.setter
    def damage(self, x):
        if self._damage:
            x = self._damage

        self._damage = x 

    @damage.getter
    def damage(self):
        return self._damage

    def __str__(self):
        return self.name

    def __int__(self):
        return self.ammo

    def __add__(self, other):
        if (self.type == WeaponType.PROJECTILE):
            self.ammo += other.ammo
            return self
        
        return self