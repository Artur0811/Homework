class EternityBell:
    def __init__(self, ri, size, vol):
        self.ri = ri
        self.size = size
        self.vol = vol
    def __iadd__(self, other):
        return "A bell of size {} rings loudly ({}): ringing {}".format(self.size, self.vol, self.ri.capitalize()+"-"+other)

    def __sub__(self, other):
        if len(self.ri) < len(other.ri):
            a = self.ri
        if len(self.ri) == len(other.ri):
            a = sorted([self.ri, other.ri])[0]
        else:
            a = other.ri
        return EternityBell(a, round((self.size+other.size)/2)-1, max(self.vol, other.vol))
    def __mul__(self, num):
        a = self.size//num
        b = self.vol//num
        if a < 1:
            a = 1
        if b == 0:
            b = 1
        return([EternityBell(self.ri,a, b)]*num)

    def __str__(self):
        return "A bell of size {} rings loudly ({}): ringing {}".format(self.size, self.vol, self.ri.capitalize())

    def __repr__(self):
        return "EternityBell({},{},{})".format(self.ri, self.size, self.vol)


etb = EternityBell("ding", 50, 16)
etb1 = EternityBell("Dong", 33, 13)
etb2 = etb - etb1
print(etb, etb1, etb2, sep="\n")
print()
etb += "Dong"
print(etb)