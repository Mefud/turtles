while 'name':
   name=input('What is your name?\n')
   if name =='stop': break
   Whois={'Nikita': 'Yes, you are Leonardo!',   
       'Egor': 'Eee boy! You - Donatello!',
       'Pavel': 'Fucking shit! You are Raf!',
       'Ivan': 'Yahoo!!!! You are Miky! KAVABANGA!!!'}
   if name in Whois:
      print(Whois[name])
   else:
      print('You are not a ninja turtle')
      
