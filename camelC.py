def snake(text):
    newT = text.lower()
    no = "_"
    result = ""
    for i in range(len(newT)):
        if newT[i] not in no:
            result += newT[i]
        elif i < len(newT) - 1 and newT[i + 1] not in no:
            result += no + newT[i]
        else:
            result += newT[i]
    return result

text = input("camelCase: ")
newtext = snake(text)
print(f"snake_case: {newtext}")