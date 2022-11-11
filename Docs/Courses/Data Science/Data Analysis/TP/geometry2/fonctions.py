class carre(object):
    def __init__(self,a):
        self.a = a
def aire(obj):
    if type(obj) == carre:
        return obj.a**2