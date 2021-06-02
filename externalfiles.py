# ==========================
# externalfiles.py
# Mark Balagtas
# A sample program that interacts with external files
# reads names and prints it.
# ===========================

# ================== funcs

def main():
    file = open('names.txt', 'r')
    allnames = file.readlines()
    n = 0
    for i in range(len(allnames)):
        name = (allnames[n])
        n += 1
        print('His name is', name)
    file.close()
    
# ========= main
main()