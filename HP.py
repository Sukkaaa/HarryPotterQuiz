# 🦁 🦅 🦡 🐍

Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
answer1=int(input("Q1) Do you like Dawn or Dusk? \n 1)Dawn \n 2)Dusk"))
if answer1==1:
  Gryffindor+=1
  Ravenclaw+=1
elif answer1==2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print("Wrong input")

answer2=int(input("Q2) When I'm dead, I want people to remember me as:\n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold"))
if answer2==1:
  Hufflepuff+=2
elif answer2==2:
  Slytherin+=2
elif answer2==3:
  Ravenclaw+=2
elif answer2==4:
  Gryffindor+=2
else:
  print("Wrong input")

answer3=int(input("Q3) Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum"))
if answer3==1:
  Slytherin+=4
elif answer3==2:
  Hufflepuff+=4
elif answer3==3:
  Ravenclaw+=4
elif answer3==4:
  Gryffindor+=4
else:
  print("Wrong input.")

house="Gryffindor"
max=Gryffindor
if Ravenclaw>Gryffindor:
  max=Ravenclaw
  house="Ravenclaw"
if Hufflepuff>max:
  max=Hufflepuff
  house="Hufflepuff"
if Slytherin>max:
  max=Slytherin
  house="Slytherin"

print("The house you belong to is "+str(house))




  


