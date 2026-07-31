class Buff:
    def __init__(self, name, buff_type, buff_value, duration, description):
        self.name = name
        self.buff_type = buff_type
        self.buff_value = buff_value
        self.duration = duration
        self.description = description
    def __str__(self):
        base = (f"Buff(name={self.name}, type={self.buff_type}, "
                f"value={self.buff_value}, duration={self.duration}, "
                f"description={self.description})")
        return base

    def __repr__(self):
        return self.__str__() 


# buff模板，后面可以放另外的文件里保管
POISON     = Buff("中毒", "poison", 5, 3, "每回合损失 5 点生命")
WEAK       = Buff("虚弱", "weak", 25, 2, "造成的伤害 -25%")
VULNERABLE = Buff("易伤", "vulnerable", 50, 2, "受到的伤害 +50%")
