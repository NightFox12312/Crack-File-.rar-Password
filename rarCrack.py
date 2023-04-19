import rarfile
import itertools

def generate_keyboard_combinations(a):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;:,.<>?`~'
    combinations = itertools.product(characters, repeat=a)
    for comb in combinations:
        yield ''.join(comb)

def crack_rar_password(rar_file, a):
    rf = rarfile.RarFile(rar_file)
    combinations = generate_keyboard_combinations(a)
    for password in combinations:
        if rf.testrar(pwd=password):
            print(f'Success! Password found: {password}')
            return password
        else:
            print(f'Incorrect password: {password}')
            continue
    print('Password not found.')
    return None

a = 8  # Replace with the desired length of the password
rar_file = 'C:\\SoftHSM2\\bin\\conf.rar'  # Replace with your RAR file path

crack_rar_password(rar_file, a)
