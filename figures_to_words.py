from num2words import num2words

def figures_to_words(number):
    try:
        return num2words(number)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    num = input("Enter a number: ")
    try:
        num = int(num)
        print(figures_to_words(num))
    except ValueError:
        print("Please enter a valid integer.")
