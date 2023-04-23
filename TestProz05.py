def encontrar_elemento(arr,el_procurado):
    verificador = False

    for i in range(len(arr)):
        if el_procurado == arr[i]:
            verificador = True


    if verificador == False:
        print(f' Elemento buscado {el_procurado} não existe no array {arr}')
    else:
        print(f'Encontramos o elemento {el_procurado} dentro do array {arr}')


arr_de_numeros = [5,18,13,15]
arr_de_nomes = ["luth", "Carine", "Jonatas"]

encontrar_elemento(arr_de_nomes,"Carine")