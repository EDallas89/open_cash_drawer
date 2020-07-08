==================== Open Cash Drawer ====================

Abre el cajón portamonedas sin imprimir ticket.

Este repositorio fue probado con una impresora usb en windows 10.

- Pre-instalación (comprobar si esta parte es necesaria):
    - Crear una impresora "Generic / Text Only"
        (Panel de control > Añadir Impresora)
    - Añadir el comando de impresora "<1B>p<00>"
        (Propiedades de impresora > Comandos Impresora)
    - Poner la impresora en el mismo puerto que la impresora de tickets
        (Propiedades de impresora > Puertos)

- Instalación (necesario si no se utiliza la impresora "Generic / Text Only"):
    - Comprobar variable printer (fichero python) contiene
        el nombre correcto de la impresora.

- Acceso Directo en Barra de Tareas:
    - Explorador de Archivos > Vista > Extensión de nombre de archivo
    - Archivo.bat > Cambiar nombre > Archivo.exe
    - Archivo.exe > Anclar a la barra de tareas
    - Archivo.exe > Cambiar nombre > Archivo.bat
    - Acceso Directo Barra de Tareas > Shift + Click Derecho > Propiedades:
        - Destino > Archivo.bat
        - Cambiar Icono
