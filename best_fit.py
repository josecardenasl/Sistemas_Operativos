# Jose David Cardenas Lucas - Sistmeas Operativos Parcial 2


def best_fit(tabla, requerimiento, index):
    mejor_bloque = None
    mejor_tamaño = float('inf')
    longitud_tabla = len(tabla)
    inicio = index

    for _ in range(longitud_tabla):
        base, limite = tabla[index]
        tamaño_disponible = limite - requerimiento
        if tamaño_disponible >= 0 and tamaño_disponible < mejor_tamaño:
            mejor_tamaño = tamaño_disponible
            mejor_bloque = index

        index = (index + 1) % longitud_tabla 

        if index == inicio and mejor_bloque is not None:
            break

    if mejor_bloque is None:
        return tabla, None, None, index  

    base_asignada = tabla[mejor_bloque][0]
    limite_asignado = requerimiento

    
    tabla[mejor_bloque] = (base_asignada + requerimiento, tabla[mejor_bloque][1] - requerimiento)
    
    if tabla[mejor_bloque][1] == 0:
        tabla.pop(mejor_bloque)
        index = mejor_bloque % len(tabla) if tabla else 0  
    else:
        index = mejor_bloque 

    return tabla, base_asignada, limite_asignado, index

# Ejemplo de uso
tabla_memoria = [(0, 100), (200, 50), (300, 100)]  
indice_inicio = 0 

num_requerimientos = int(input("Ingrese el número de requerimientos: "))
requerimientos = [int(input(f"Ingrese el tamaño del requerimiento {i+1}: ")) for i in range(num_requerimientos)]

for requerimiento in requerimientos:
    resultado = best_fit(tabla_memoria, requerimiento, indice_inicio)
    nueva_tabla, base_asignada, limite_asignado, indice_inicio = resultado
    
    if base_asignada is not None:
        print("\nAsignación exitosa:")
        print("Nueva tabla de memoria:", nueva_tabla)
        print("Dirección base asignada:", base_asignada)
        print("Límite asignado:", limite_asignado)
        if nueva_tabla:
            print("Índice actual se encuentra en:", nueva_tabla[indice_inicio])
        else:
            print("Memoria completamente asignada, no quedan bloques disponibles.")
    else:
        print("\nNo se pudo asignar memoria suficiente para el requerimiento de tamaño", requerimiento)


