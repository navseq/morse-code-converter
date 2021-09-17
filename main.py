import pandas as pd

text = input('Type the text you want to convert: ')

df = pd.read_csv('morse-code.csv')

# Convert dataframe to dictionary
morse_dict = {row.CHARACTER: row.CODE for (index, row) in df.iterrows()}

result = [morse_dict[letter] for letter in text.upper()]

# Convert list to string
morse_code = ""

for _ in result:
    morse_code += _

print(f"The morse code is: {morse_code}")

