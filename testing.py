#%% 
class Gates:

    def __init__(self):
        pass

    def NOT(self, i):
        return not i
    def AND(self, i1, i2):
        return i1 and i2
    def NAND(self, i1, i2):
        return not(i1 and i2)
    def OR(self, i1, i2):
        return i1 or i2
    def NOR(self, i1, i2):
        return not(i1 or i2)
    def XOR(self, i1, i2):
        return i1 ^ i2
    def XNOR(self, i1, i2):
        return self.NOT(i1 ^ i2)
    def TriState(self, A, enable):
        if(enable): return A
        else: return None
    
    def HalfAdder(self, A,B):
        carry = self.AND(A,B)
        summation = self.XOR(A,B)
        return [carry, summation]
    
    def FullAdder(self, A,B,C):
        carry1, sum1 = self.HalfAdder(A,B)
        carry2, sum2 = self.HalfAdder(sum1, C)
        return [g.OR(carry1, carry2), sum2]
    
    def AddNumbers(self, A, B):
        numbers = [*zip(A,B)]
        carry = False
        value = []
        for An, Bn in numbers[::-1]:
            carry, summation = self.FullAdder(An,Bn, carry)
            value.append(summation)
        return [carry, *value[::-1]]

g = Gates()
g.AddNumbers([True,False,False,True],[True,False, False, False])
# %%
class Memory:

    def __init__(self):
        self.g2_old = False
        self.gates = Gates()
    
    def run(self, E, D):
        
        R = self.gates.AND(self.gates.NOR(D), E)

        S = self.gates.AND(D, E)

        g1 = self.gates.NOR(R, self.g2_old)
        g2 = self.gates.NOR(S, g1)
        self.g2_old = g2
        return g1
memory = Memory()
# %%
memory.run(False, False)
# %%
