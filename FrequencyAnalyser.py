def FrequencyAnalyser(plain_text):
    unique_letters = set(plain_text)
    plain_text = list(plain_text)

    for letter in unique_letters:
        count_letter = plain_text.count(letter)
        print(f'The frequency of {letter} is {((count_letter/len(plain_text))*100)} %.')

def inputFunction():
    plain_text = input("Enter the plain text: ")
    return plain_text


plain_text = inputFunction()

print("----------------------------------------------")
print(f'Plain Text: {plain_text}')

print("----------------------------------------------")
FrequencyAnalyser(plain_text)
