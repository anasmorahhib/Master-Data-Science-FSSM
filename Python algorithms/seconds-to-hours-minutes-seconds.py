second = input('Give a number in seconds:')
hours =int(second)/3600
minutes = (int(second)%3600)/60
seconds = (int(second)%3600)%60
print(int(hours),'hours, ', int(minutes), ' minutes and', int(seconds),' seconds')
