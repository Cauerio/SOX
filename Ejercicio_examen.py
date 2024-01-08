if __name__ == '__main__':
    c1 = Coche ("Mercedes", "4x4", "120H")
    c2 = Coche ("Ferrari", "Deportivo", "320H")
    c3 = Coche ("Aston Martin", "Deportivo", "480H")

    array_de_coches = (c1, c2, c3)
    c = Carrera(array_de_coches)

    c.haz_carrera()
    c.muestra_resultado()