name=input('What is your name?\n')
Whois={'Nikita': 'Yes, you are Leonardo!',   
       'Egor': 'Eee boy! You - Donatello!',
       'Pavel': 'Fucking shit! You are Raf!',
       'Ivan': 'Yahoo!!!! You are Miky! KAVABANGA!!!'}
try:
   print(Whois[name])
except:
   print('You are not a ninja turtle')
