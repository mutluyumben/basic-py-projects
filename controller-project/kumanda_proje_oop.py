import random 

class Controller():

    def __init__(self, current_pos = "Close", volume = 0, channel_index = 1, channel_list = ["TRT", "AHaber", "HalkTV"], channel = "TRT" ):
        
        self.current_pos = current_pos
        self.volume = volume
        self.channel_list = channel_list
        self.channel_index = channel_index

    def set_volume(self):
        while True:
            vol_choice = input("Press < for vol_down\nPress > for vol_up\nPress q for end.")

            if vol_choice == '<':
                if (self.volume != 0):
                    self.volume -= 1
                    print(self.volume)
            elif vol_choice == '>':
                if self.volume != 100:
                    self.volume += 1
                    print(self.volume)
            else:
                print(f"Volume is: {self.volume}")
                break
    
    def tv_ac_kapat(self):
        if self.current_pos == 'Close':
            self.current_pos = 'Open'
            print("Tv is opening")

        elif self.current_pos == "Open":
            self.current_pos = 'Close'
            print("Tv is closing")
        
        else:
            print(f"TV is {self.current_pos}")

    def channel_change(self, direction):
        if direction == '-':
            self.channel_index != 0
            self.channel_index -= 1
            print(self.channel_index)
        elif direction == '+':
            self.channel_index != 100
            self.channel_index += 1
            print(self.channel_index)
    
    def random_channel(self):
        self.random_channel = random.randint(0, len(self.channel_list) - 1)
        self.current_pos = self.random_channnel
        print(self.current_pos)

    def add_channel(self, kanal):
        self.add_ch = input(("Add channel name: "))
        self.channel_list.append(self.add_ch)
        
        print("Channel is added")
    
controller = Controller()

print('''
--------------------
    -Controller List-
      
      1- TV Open

      2- TV Close

      3- Volume Up

      4- Volume Down

      5- Channel Up 

      6- Channel Down 

      7- Add Channel

      8- Current Channel

      9- Go to the random channel

      10- Go to the Channel List

''')

while True:

    choice = input("Select the option: ")

    if choice == 'q':
        print("Exiting the controller...")

    if choice == '1':
        controller.tv_ac_kapat()
    
    elif choice == '2':
        controller.tv_ac_kapat()
        
    elif choice == '3':
        controller.set_volume()

    elif choice == '4':
        controller.set_volume()

    elif choice == '5':
        direction = input("If you want to go up == '+'\nIf you want to go down == '-'")
        controller.channel_change(direction)

    elif choice == '6':
        direction = input("If you want to go up == '+'\nIf you want to go down == '-'")
        controller.channel_change(direction)

    elif choice == '7':
        controller.add_channel()

    elif choice == '8':
        ch = controller.channel_list[controller.channel_index]
        print(ch)

    elif choice == '9':
        controller.random_channel()

    elif choice == '10':
        print(controller.channel_list)
    
    else: 
        break



