def main():
    outfile = open("notas.txt","w")
    fname = input("Introduzca su nombre de usuario: ")
    outfile.write(fname)
    outfile.write("\t")
    outfile.close()
main()