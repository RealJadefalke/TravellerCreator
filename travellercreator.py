import random


attribute = {
  "Stärke" : None,
  "Geschicklichkeit" : None,
  "Ausdauer" : None,
  "Intelligenz" : None,
  "Bildung" : None,
  "Sozialstatus" : None,
  }



def grundwerte():
  attribute["Stärke"] = random.randrange(2, 12)
  attribute["Geschicklichkeit"] = random.randrange(2, 12)
  attribute["Ausdauer"] = random.randrange(2, 12)
  attribute["Intelligenz"] = random.randrange(2, 12)
  attribute["Bildung"] = random.randrange(2, 12)
  attribute["Sozialstatus"] = random.randrange(2, 12)

def einstellung(x):
  if x == 1 :
    wurf = random.randrange(2,12)
    print(wurf)
    if attribute["Intelligenz"] >= 8 :
      wurf += 1
    if attribute["Bildung"] >= 9 :
      wurf += 2
    if wurf >= 8 :
      print("Erfolg")
    else :
     print("Leider nicht!")
  elif x == 2:
    wurf = random.randrange(2,12)
    print(wurf)
    if attribute["Intelligenz"] >= 8 :
      wurf += 1
    if attribute["Stärke"] >= 8 :
      wurf += 2
    if wurf >= 9 :
      print("Erfolg")
    else :
     print("Leider nicht!")
  elif x == 3:
    wurf = random.randrange(2,12)
    print(wurf)
    if attribute["Geschicklichkeit"] >= 6 :
      wurf += 1
    if attribute["Ausdauer"] >= 5 :
      wurf += 2
    if wurf >= 5 :
      print("Erfolg")
    else :
     print("Leider nicht!")
  elif x == 4:
    wurf = random.randrange(2,12)
    print(wurf)
    if attribute["Intelligenz"] >= 6 :
      wurf += 1
    if attribute["Stärke"] >= 8 :
      wurf += 2
    if wurf >= 7 :
      print("Erfolg")
    else :
     print("Leider nicht!")
  elif x == 5:
    wurf = random.randrange(2,12)
    print(wurf)
    if attribute["Stärke"] >= 7 :
      wurf += 1
    if attribute["Intelligenz"] >= 6 :
      wurf += 2
    if wurf >= 7 :
      print("Erfolg")
    else :
     print("Leider nicht!")
  else:
    wurf = random.randrange(2,12)
    if wurf >= 3:
      print("Erfolg")
    else:
      print("Leider nicht!")
    
 

print("Willkommen beim TRAVELLER Generator")
grundwerte()
print("Wähle deine Dienstgattung:")
print("[1] Raumflotte")
print("[2] Raumgarde")
print("[3] Heer")
print("[4] Scoutdienst")
print("[5] Handelsflotte")
print("[6] Andere")
einstellung(int(input()))
print(attribute)
#print(dienstgattung)
