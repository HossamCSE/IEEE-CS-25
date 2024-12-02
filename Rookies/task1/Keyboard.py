keyboard = {
    'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5, 'u': 6, 'i': 7, 'o': 8, 'p': 9,'[':10,']':11,
    'a': 12, 's': 13, 'd': 14, 'f': 15, 'g': 16, 'h': 17, 'j': 18, 'k': 19, 'l': 20,';':21,"'":22,
     'z': 23, 'x': 24, 'c': 25, 'v': 26, 'b': 27, 'n': 28, 'm': 29, ',': 30, '.': 31, '/': 32
}

dir = str(input())
word = str(input()).lower()

message = ""
for char in word:
  if char in keyboard:
      index = keyboard[char]
      if dir == 'R':

            if index > 0:
                message += list(keyboard.keys())[list(keyboard.values()).index(index - 1)]

      elif dir == 'L':

            if index < len(keyboard) - 1:
                message += list(keyboard.keys())[list(keyboard.values()).index(index + 1)]

      else:

            break
  else:

        break

print(message)

