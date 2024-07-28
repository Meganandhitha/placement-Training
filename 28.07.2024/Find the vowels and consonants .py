string = input("Enter a string: ").lower()
vowels = "aeiouAEIOU"
num_vowels = sum(1 for char in string if char in vowels)
num_consonants = sum(1 for char in string if char.isalpha() and char not in vowels)
print(f"Number of vowels: {num_vowels}")
print(f"Number of consonants: {num_consonants}")
