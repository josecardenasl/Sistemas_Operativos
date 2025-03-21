# Parcial 2 sistemas operativos - Jose David cardenas Lucas - Best_Fit

def best_fit(work_memory, req, index):
    if not work_memory:
        return None  

    best_index = None
    best_size = float('inf')
    best_block = None
    
    for i, (base, size) in enumerate(work_memory):
        if size >= req and size < best_size:
            best_size = size
            best_index = i
            best_block = (base, size)
    
    if best_index is None:
        return None

    base_asignada = best_block[0]
    new_size = best_block[1] - req

    new_memory = work_memory[:]
    if new_size == 0:
        del new_memory[best_index]
        best_index = best_index % len(new_memory)
    else:
        new_memory[best_index] = (base_asignada + req, new_size)

    return new_memory, base_asignada, req, best_index
