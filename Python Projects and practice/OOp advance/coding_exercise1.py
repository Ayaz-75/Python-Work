# ------------Program to create attributes in different classes----------------#

class BasicPlan:

    def __init__(self):
        self.can_stream = False
        self.can_download = False
        self.has_hd = True
        self.num_of_devices = 1
        self.price = 8


class StanderPlan(BasicPlan):

    def __init__(self):
        super().__init__()
        self.num_of_devices = 2
        self.price = 12
        self.can_stream = False
        self.can_download = False


class PremiumPlan(BasicPlan):

    def __init__(self):
        super().__init__()
        self.can_stream = True
        self.can_download = True
        self.has_hd = True
        self.num_of_devices = 8
        self.price = 15


# ---------- Creating objects of the three classes given above ----------

class_a = BasicPlan()
class_b = StanderPlan()
class_c = PremiumPlan()
