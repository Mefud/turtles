program turtles;
var
   m: string;
begin
   writeln('What is your name?');
   read(m);
   case m of
   'Nikita':
      writeln('Yes, you are Leonardo!');   
   'Egor':
      writeln('Eee boy! You - Donatello!');
   'Pavel':
      writeln('Fucking shit! You are Raf!');
   'Ivan':
      writeln('Yahoo!!!! You are Miky! KAVABANGA!!!')
   else
      writeln('You are not a ninja turtle')
   end
end.
