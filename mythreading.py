import mythreading

# applicable for send and receive message
class AndMessage(mythreading.Thread):
    def run(self):
        for _ in range(10):
            print(mythreading.currentThread().getName())

x = AndMessage(name = 'Send out message')
y = AndMessage(name = 'Receive message')

x.start()
y.start()