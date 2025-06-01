def ExportarGraphviz(grafo, nombre_archivo="mst.dot"):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write("graph MST {\n")
        for v in grafo:
            if v.predecesor:
                origen = v.predecesor.id
                destino = v.id
                peso = v.obtener_ponderacion(v.predecesor)
                f.write(f'    "{origen}" -- "{destino}" [label={peso}];\n')
        f.write("}\n")
