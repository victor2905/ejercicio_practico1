print("******************************")
print("Sistema de vacaciones, Rappi")
print("******************************\n")
print("Definición de datos:\n")
nombre_empleado = input("Defina su nombre: ")
clave_departamento = int(input("Cuál es su clave: "))
anio_antiguedad = int(input("Defina sus años de antiguedad: "))

#Clave 1: Departamento de atención al cliente
if clave_departamento == 1:
    if anio_antiguedad == 1:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 6 dias de Vacaciones")
    elif anio_antiguedad >= 2 and anio_antiguedad <=6:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 14 dias de Vacaciones")
    elif anio_antiguedad >= 7:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 20 dias de Vacaciones")
        
#Clave 2: Departamento de logística
elif clave_departamento == 2:
    if anio_antiguedad == 1:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 7 dias de Vacaciones")
    elif anio_antiguedad >= 2 and anio_antiguedad <=6:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 15 dias de Vacaciones")
    elif anio_antiguedad >= 7:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 22 dias de Vacaciones")

#Clave 3: Departamento de Gerencia
elif clave_departamento == 3:
    if anio_antiguedad == 1:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 10 dias de Vacaciones")
    elif anio_antiguedad >= 2 and anio_antiguedad <=6:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 20 dias de Vacaciones")
    elif anio_antiguedad >= 7:
        print("Estimado: ",nombre_empleado," Ud. tiene "," 30 dias de Vacaciones")
 
else:
    print("No existe código de clave ingresado")
