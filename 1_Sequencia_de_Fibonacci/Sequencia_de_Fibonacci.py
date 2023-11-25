def fibonacci(n):
    fibonacci_terms = [0,1]
    
    for i in range(2, n):
        fibonacci_terms.append(fibonacci_terms[i-1] + fibonacci_terms[i-2])
        
    return fibonacci_terms

print (fibonacci(15))


# result -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]