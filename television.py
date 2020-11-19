# implementation of a class that describes a television

upper_limit=100
inferior_limit=1
channel=4

class Television:
    def __init__(self):
        self.turn_on= True # initialized with the television turned off
        self.channel=4 # channel initial
        self.upper_limit=100 # higher channel(frequency) supported by television
        self.inferior_limit=1 # lower channel(frequency) supported by television
    
    def power(self): # turn the tv off or on
        not self.turn_on
    
    def channel_up(self): # increase the channel
        if channel>upper_limit:
            print('error: sorry, channel not suported')
            channel=inferior_limit
        else:
            channel +=1
    
    def channel_down(self): # decrease the channel
        if channel <inferior_limit:
            print('error: sorry, channel not suported')
            channel=upper_limit
        else:
            channel -=1
    def channel_change(self, chosen_channel):
        if chosen_channel<1 or chosen_channel>100:
            print('error: sorry, channel not suported')
        else:
            channel=chosen_channel

tv=Television()
tv.power()
#choice=input('please type w to advance the channel, s to rewind the channel, p to turn off the tv or another letter to choose the channel you prefer: ')

while(tv.turn_on==True):
    #choice=input('please type p to turn off the tv, w to advance the channel, s to rewind the channel or the channel number of your choice: ')
    choice=input('please type w to advance the channel, s to rewind the channel, p to turn off the tv or another letter to choose the channel you prefer:')
    
    if choice =='w':
        tv.channel_up()
        print('you are watching channel {}'.format(tv.channel))
    elif choice =='s':
        tv.channel_down()
        print('you are watching channel {}'.format(tv.channel))
    elif choice=='p':
        tv.power()
        print('thanks for watching me')
    else:
        number_channel=int(input('please enter the number of the channel you want to watch'))
        tv.channel_change(number_channel)
        print('you are watching channel {}'.format(tv.channel))