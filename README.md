# 1er_entrega_diplo_PY

Descripción.
La interface gráfica de la aplicación está realizada con Tkinter. Para la ubicación de los objetos en la ventana creada se utilizó el modo grilla. Se implementaron botones que llaman a las funciones específicas al fin para el cual fueron pensados. La presentación de los datos se realiza mediante el método Tree.
Se optó por implementar la base de datos Sqlite3 dado que tiene métodos nativos en Python, para el manejo de los datos de la aplicación se implementaron funciones de creación de la base de datos, lectura y presentación de los datos guardados, actualización y modificación de los datos y eliminación (CRUD). En los comentarios en el código se identifica cada una de las funciones mencionadas anteriormente.
Se realizó la validación de cada uno de los campos para ingresar información. Los campos nombre y ciudad de residencia no pueden contener números ni estar vacíos, el campo dirección admite letras y números, el campo correo electrónico valida todo tipo de dirección de correo electrónico posible y valido y por último el campo fecha de nacimiento valida cualquier fecha ingresada en el formato DD/MM/AAAA.
Se utilizaron ciclos for y condicionales if – else, así como también se implementó el manejo de excepciones con el bloque Try – Except para poder dar avisos personalizados en casos de error o de no cumplir con la validación de los campos.

Uso.
 Fue inspirado en la página para el registro de la campaña de vacunación contra el Covid-19. Su uso esta aplicado a formar un registro para los candidatos a vacunar. 
Una vez ejecutado el programa deberemos conectarnos con la base de datos. Para ello debemos ir al menú "INICIO" y la opción "Crear / Conectar base de datos". Una vez realizado tendremos las opciones:
  •	Ingresar datos: Los datos de la persona ingresan en los campos: Nombre Completo, Fecha de Nacimiento en el formato DD/MM/AAAA, Lugar de residencia, Domicilio y correo electrónico. Una vez completo, haremos click en el botón "Cargar Registro". Veremos los datos ingresados en el registro. 
  •	Modificar el registro: Este botón nos da la opción de modificar los campos de registro previamente seleccionado.
  •	Eliminar el registro: Nos permite eliminar el registro seleccionado.
  •	Mostrar lista: Nos da la opción de cargar todos los registros guardados en la base de datos cuando se inicia el programa.
