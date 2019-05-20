movie = input('Tytuł filmu:')
grade = int(input('Ocena filmu w skali 1-10:'))
grade2 = int(input('Ocena gry aktorskiej:'))
grade3 = int(input('Ocena muzyki:'))
mean = (grade + grade2 + grade3) / 3
print("Średnia ocena filmu", movie, "to", int(mean))
