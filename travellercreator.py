import random

#Dictionary um die sechs Grundcharakteristika für den Charakter zu speichern
attribute = {
  "Stärke" : None,
  "Geschicklichkeit" : None,
  "Ausdauer" : None,
  "Intelligenz" : None,
  "Bildung" : None,
  "Sozialstatus" : None,
  }


laufbahn = None #Laufbahn des Charakters
eingezogen = False #Variable um festzustellen ob der Charakter eingezogen wurde
dienstrang = None #Dienstrang des Charakters
offizierspatent = False #Hat der Charakter ein Offizierspatent oder nicht

#Grundcharakteristika auswürfeln
def grundwerte():
  attribute["Stärke"] = random.randrange(2, 12)
  attribute["Geschicklichkeit"] = random.randrange(2, 12)
  attribute["Ausdauer"] = random.randrange(2, 12)
  attribute["Intelligenz"] = random.randrange(2, 12)
  attribute["Bildung"] = random.randrange(2, 12)
  attribute["Sozialstatus"] = random.randrange(2, 12)

#Charakterlaufbahn festlegen
def einstellung(x):
  wurf = random.randrange(2,12)
  print(f"Dein Wurf:{wurf}")
  match x :
    case 1 : #Raumflotte
      if attribute["Intelligenz"] >= 8 :
        wurf += 1
      if attribute["Bildung"] >= 9 :
        wurf += 2
      if wurf >= 8 :
        print("Erfolg")
        return "Raumflotte"
      else :
        print("Leider nicht!")
        return None
    case 2: #Raumgarde
      if attribute["Intelligenz"] >= 8 :
        wurf += 1
      if attribute["Stärke"] >= 8 :
        wurf += 2
      if wurf >= 9 :
        print("Erfolg")
        return "Raumgarde"
      else :
        print("Leider nicht!")
        return None
    case 3: #Heer
      if attribute["Geschicklichkeit"] >= 6 :
        wurf += 1
      if attribute["Ausdauer"] >= 5 :
        wurf += 2
      if wurf >= 5 :
        print("Erfolg")
        return "Heer"
      else :
        print("Leider nicht!")
        return None
    case 4: #Scoutdienst
      if attribute["Intelligenz"] >= 6 :
        wurf += 1
      if attribute["Stärke"] >= 8 :
        wurf += 2
      if wurf >= 7 :
        print("Erfolg")
        return "Scoutdienst"
      else :
        print("Leider nicht!")
        return None
    case 5: #Handelsflotte
      if attribute["Stärke"] >= 7 :
        wurf += 1
      if attribute["Intelligenz"] >= 6 :
        wurf += 2
      if wurf >= 7 :
        print("Erfolg")
        return "Handelsflotte"
      else :
        print("Leider nicht!")
        return None
    case 6: #Andere
      if wurf >= 3:
        print("Erfolg")
        return "Andere"
      else:
        print("Leider nicht!") 
        return None

#Bei abgelehntem Karrierewurf Einziehungswurf
def einziehung(eingezogen) :
  wurf = random.randrange(1,6)
  match wurf:
    case 1:
      eingezogen = True
      return "Raumflotte"
    case 2:
      eingezogen = True
      return "Raumgarde"
    case 3:
      eingezogen = True
      return "Heer"
    case 4:
      eingezogen = True
      return "Scoutdienst"
    case 5:
      eingezogen = True
      return "Handelsflotte"
    case 6:
      eingezogen = True
      return "Andere"


#Überlebenswurf um festzustellen ob der Charakter überlebt
def ueberlebt(x) :
  wurf = random.randrange(2,12)
  match x:
    case "Raumflotte":
      if attribute["Intelligenz"] >= 7 :
        wurf += 2
      if wurf >= 5 :
        print("Überlebt!")
      else:
        print("Leider gestorben! Versuch es nochmal!")
        quit()
    case "Raumgarde":
      if attribute["Ausdauer"] >= 8 :
        wurf += 2
      if wurf >= 6 :
        print("Überlebt!")
      else:
        print("Leider gestorben! Versuch es nochmal!")
        quit()
    case "Heer":
      if attribute["Bildung"] >= 6 :
        wurf += 2
      if wurf >= 5 :
        print("Überlebt!")
      else:
        print("Leider gestorben! Versuch es nochmal!")
        quit()
    case "Scoutdienst":
      if attribute["Ausdauer"] >= 9 :
        wurf += 2
      if wurf >= 7 :
        print("Überlebt!")
      else:
        print("Leider gestorben! Versuch es nochmal!")
        quit()
    case "Handelsflotte":
      if attribute["Intelligenz"] >= 7 :
        wurf += 2
      if wurf >= 5 :
        print("Überlebt!")
      else:
        print("Leider gestorben! Versuch es nochmal!")
        quit()
    case "Andere":
      if attribute["Intelligenz"] >= 9 :
        wurf += 2
      if wurf >= 5 :
        print("Überlebt!")
      else:
        print("Leider gestorben! Versuch es nochmal!")
        quit()


#Beförderungswurf in der ersten Periode nur möglich wenn nicht eingezogen
def befoerderung() :
  if eingezogen == True :
    eingezogen = False
  else:
    if offizierspatent == False:
      wurf = random.randrange(2,12)
      match laufbahn:
        case "Raumflotte":
          if attribute["Sozialstatus"] >=9 :
            wurf +=1
          if wurf >= 10:
            offizierspatent == True
            print("Glückwunsch zum Offizierspatent!")
          else:
            print("Leider kein Patent, versuch es nächstes Jahr nochmal!")
        case "Raumgarde":
          if attribute["Bildung"] >=7 :
            wurf +=1
          if wurf >= 9:
            offizierspatent == True
            print("Glückwunsch zum Offizierspatent!")
          else:
            print("Leider kein Patent, versuch es nächstes Jahr nochmal!")
        case "Heer":
          if attribute["Ausdauer"] >=9 :
            wurf +=1
          if wurf >= 5:
            offizierspatent == True
            print("Glückwunsch zum Offizierspatent!")
          else:
            print("Leider kein Patent, versuch es nächstes Jahr nochmal!")
        case "Scoutdienst":
          pass
        case "Handelsflotte":
          if attribute["Intelligenz"] >=6 :
            wurf +=1
          if wurf >= 4:
            offizierspatent == True
            print("Glückwunsch zum Offizierspatent!")
          else:
            print("Leider kein Patent, versuch es nächstes Jahr nochmal!")
        case "Andere":
          pass










print("Willkommen beim TRAVELLER Generator")
grundwerte()
print("Dein UPP:")
for key, value in attribute.items() :
  print (f"{key:<17}: {value:>2}")
print("Wähle deine Dienstgattung:")
print("[1] Raumflotte")
print("[2] Raumgarde")
print("[3] Heer")
print("[4] Scoutdienst")
print("[5] Handelsflotte")
print("[6] Andere")
laufbahn = einstellung(int(input()))
if laufbahn == None :
  laufbahn = einziehung()
print(laufbahn)
ueberlebt(laufbahn)
befoerderung()
