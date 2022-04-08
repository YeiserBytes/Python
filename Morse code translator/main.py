text = input("Escribe lo que quieres traducir: ")

alpha = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}

sound = {
    ".": "beep",
    " ": " ",
    "-": "beeeeep",
    "/": "/"
}

list_up = text.upper()
words = list_up.split(" ")

morse = []
noise = []

y = len(words) - 1
z = 0

for i in words:
    for j in i:
        morse.append(alpha[j])
    
    if z == y:
        break

    if z <= y:
        morse.append("/")
        z += 1

w = " ".join(morse)
print(w)

for h in w:
    noise.append(sound[h])

print(" ".join(noise))