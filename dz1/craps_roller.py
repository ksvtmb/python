# кости. бросок костей бай рандом

import random
# создаеи случайные числа из диапазона 1-6
die1=random.randint(1,6)
die2=random.randrange(6)+1
total=die1+die2
# выводим результат
print ("При вашем броске выпало",die1, "и",die2, "очков", "в сумме", total)