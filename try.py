
class Car:
    def __init__(self, color):

        self.color = color
        self.status = 'off'
    
    def start(self):

        if self.status == 'off':
            self.status = 'on'
        else:
            print('already on!!!!')


    
car1 = Car(color='RED')

print(car1.color)
car1.start()
