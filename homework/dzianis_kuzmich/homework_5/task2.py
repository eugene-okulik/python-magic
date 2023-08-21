stored_number = 7  # You can change this number to any other from 0 to 9.

while True:
    guess = input("Угадайте цифру от 0 до 9: ")
    if int(guess) == stored_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова.")
