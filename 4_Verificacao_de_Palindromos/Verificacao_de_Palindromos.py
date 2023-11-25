def validate_palindromes(word):
    
    word_lower = word.lower()
    cont_indexes = len(word)
    
    for i in range(cont_indexes // 2):
        if word_lower[i] != word_lower[cont_indexes - 1 - i]:
            return False
        
    return True

print(validate_palindromes('Ada'))