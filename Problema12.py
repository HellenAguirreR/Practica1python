def obtener_tipo_mime(nombre_archivo):
    # Obtener la extensión del archivo
    if '.' in nombre_archivo:
        extension = nombre_archivo.split('.')[-1].lower()
    else:
        extension = ""

    tipos_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

    return tipo_mime

nombre_archivo = input("Ingrese el nombre del archivo: ")

tipo_mime = obtener_tipo_mime(nombre_archivo)
print("Tipo MIME:", tipo_mime)
