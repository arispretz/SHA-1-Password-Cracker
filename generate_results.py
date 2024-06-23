import password_cracker

cracked_password1 = password_cracker.crack_sha1_hash("fbbe7e952d1050bfb09dfdb71d4c2ff2b3d845d2")
cracked_password2 = password_cracker.crack_sha1_hash("dcc466796201f7232b22a03781110a8871fd038c", use_salts=True)

results = [
    "Hash 1: " + cracked_password1,
    "Hash 2: " + cracked_password2
]

with open('results.txt', 'w') as file:
    for result in results:
        file.write(result + '\n')
