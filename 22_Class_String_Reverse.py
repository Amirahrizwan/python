class String:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        return self.text[::-1]


text = input("Enter a string: ")

string = String(text)

print("Original string:", text)
print("Reversed string:", string.reverse())
