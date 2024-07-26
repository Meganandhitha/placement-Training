if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        try:
            a, b = input().split()
            
            result = int(a) // int(b)
            print(result)
        
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        
        except ValueError as e:
            print(f"Error Code: {e}")
