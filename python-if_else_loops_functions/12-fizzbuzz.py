#!/usr/bin/python3
def fizzBuzz(n):
    res = [] 

    for i in range(1, n + 1):
      
        # Initialize an empty string for the current result
        s = "" 

        # Divides by 3, add Fizz
        if i % 3 == 0:
            s += "Fizz"
            
        # Divides by 5, add Buzz
        if i % 5 == 0:
            s += "Buzz"
            
        # Not divisible by 3 or 5, add the number
        if not s:
            s += str(i)
		
        # Append the current result to the list
        res.append(s) 

    return res

if __name__ == "__main__":
    n = 20 
    res = fizzBuzz(n) 

    for s in res:
        print(s, end=" ")
