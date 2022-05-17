class LifeGivingFire:
    def __init__(self, color, firewood, T):
        self.color = color
        self.firewood = firewood
        self.T = T

    def __gt__(self, other):
        if sorted([self.color, other.color])[0] == other.color or self.firewood > other.firewood or self.T > other.T:
            return True
        else:
            return False

    def __ge__(self, other):
        if sorted([self.color, other.color])[0] == other.color or self.firewood >= other.firewood or self.T >= other.T:
            return True
        else:
            return False

    def __le__(self, other):
        if sorted([self.color, other.color])[0] == self.color or self.firewood <= other.firewood or self.T <= other.T:
            return True
        else:
            return False

    def __lt__(self, other):
        if sorted([self.color, other.color])[0] == self.color or self.firewood < other.firewood or self.T < other.T:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.color != other.color and self.firewood != other.firewood and self.T != other.T:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.color == other.color and self.firewood == other.firewood and self.T == other.T:
            return True
        else:
            return False

    def throw_wood(self, n):
        self.firewood += n
        self.T += n//10

    def change_color(self, arg):
        if len(arg) >= len(self.color):
            self.color = arg
            
    def __str__(self):
        return "Life-Giving Fire with color of {} by {} of wood, burning for {}".format(self.color, self.firewood,self.T)

lgf = LifeGivingFire("scarlet", 20, 5)
lgf1 = LifeGivingFire("orange", 20, 5)
print(lgf > lgf1, lgf == lgf1, lgf <= lgf1)
lgf.throw_wood(17)
print(lgf)