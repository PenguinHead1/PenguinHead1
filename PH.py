

from pyfiglet import Figlet

def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def create_ascii_art(text, font='slant'):
    figlet = Figlet(font=font)
    return figlet.renderText(text)

def main():
    print("Generating a cool password:")
    password = generate_password()
    print(password)

    print("\nCool ASCII Art:")
    ascii_art_text = "Cool Password"
    ascii_art = create_ascii_art(ascii_art_text)
    print(ascii_art)

if __name__ == "__main__":
    main()
