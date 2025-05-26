import hashlib


def hmm():
    password = input("Nhập password: ")
    pas_has = hashlib.sha256(password.encode()).hexdigest()
    print(pas_has)
    
hmm()