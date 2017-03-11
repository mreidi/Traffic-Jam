# the Car class

class Car(object):
# __init__
    def __init__(self, x, v, min_dist, target_v):
        self.x_ = x;
        self.min_dist_ = min_dist
        self.v_ = v
        self.target_v_ = target_v 

# methods
    @property
    def x(self):
        return self.x_

    @property
    def v(self):
        return self.v_

    def set_v(self, v):
        self.v_ = v


    def update(self, next_car = None):
        #print "******", self.v

        if next_car == None:
            self.v_ = self.target_v_
            #print "vv ===>", self.v_
            print "true"

        else:
            print "false"
            self.v_ = min( self.target_v_, float(next_car.x - self.min_dist_ - self.x_)/dt )
            # here we assume that the front car is moved before; but even if it
            # hasn't, we take the worst case in which we assume the fron car's
            # velocity will be set to 0, and that again results the same equation.

        self.x_ = self.x_ + self.v_ * dt


# ===== The following lines are for testing how the Car class works =====
"""
t = 0.0
dt = 0.1

c1 = Car(2.0, 0.3, 0.4, 15.0)
#print c1.target_v_
c2 = Car(0.15,0.1, 0.04, 16.0)
#print c2.target_v_


for i in range(25):
    c1.update()
    print "C1 -->", c1.x, c1.v
    c2.update(c1)
    print "C2 -->", c2.x, c2.v
    print " -------------------------------------", c1.x - c2.x, "------------------------------------------"
    print "\n"

"""
