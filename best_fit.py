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
        return None  

    base_asignada = tabla[mejor_bloque][0]
    limite_asignado = requerimiento

    tabla[mejor_bloque] = (base_asignada + requerimiento, tabla[mejor_bloque][1] - requerimiento)

    cabezal = tabla[mejor_bloque]

    return tabla, base_asignada, limite_asignado, mejor_bloque

# Ejemplo de uso
tabla_memoria = [(0, 100), (200, 50), (300, 100)]  
requerimiento_tamaño = 100
indice_inicio = 1 # La tabla se empieza contar desde la posicion 0, es decir 0, 1, 2

resultado = best_fit(tabla_memoria, requerimiento_tamaño, indice_inicio)

if resultado:
    nueva_tabla, base_asignada, limite_asignado, bloque = resultado
    print("Asignación exitosa:")
    print("Nueva tabla de memoria:", nueva_tabla)
    print("Dirección base asignada:", base_asignada)
    print("Límite asignado:", limite_asignado)
    if nueva_tabla[bloque][1] == 0:
        bloque = (bloque + 1) % len(nueva_tabla)
        print("Indice actual se encuentra en:", nueva_tabla[bloque])
    else:
        print("Indice actual se encuentra en:", nueva_tabla[bloque])

    
else:
    print("No se pudo asignar memoria suficiente después de la búsqueda.")