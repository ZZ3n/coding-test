def solution(phone_book):
    
    M = {}
    for phone in phone_book:
        M[phone] = 1
    
    for phone in phone_book:
        arr = ""
        for digit in phone:
            arr += digit
            if arr in M and arr != phone:
                return False
    return True
    