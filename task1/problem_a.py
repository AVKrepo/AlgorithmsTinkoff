text = input()
postfix_transcription = text.strip().split()

while len(postfix_transcription) > 1:
    for i, symbol in enumerate(postfix_transcription):
        if not symbol in ["+", "-", "*"]:
            continue
        operation = postfix_transcription.pop(i)
        b = int(postfix_transcription.pop(i - 1))
        a = int(postfix_transcription.pop(i - 2))
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        else:
            result = a * b
        postfix_transcription.insert(i - 2, result)
        break
print(result)
