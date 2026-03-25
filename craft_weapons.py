class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        combo = {self.sword_type, other.sword_type}
        if combo == {"bronze"}: 
            return Sword("iron")
        elif combo == {"iron"}:     
            return Sword("steel")
        else:
            raise ValueError("cannot craft")
        
    def __repr__(self):
        return f"Sword({self.sword_type})"
