program FODejercicio3;
type
cadena = String[20];

empleados = record
   num_e: integer;
   apellido: cadena;
   nombre: cadena;
   edad: integer;
   dni: integer;
end;
archivo1 = file of empleados;

procedure agregarEmp(var emp_a:archivo1);
var
 emp:empleados;
begin
   writeln('ingrese apellido del empleado: ');
   readln(emp.apellido);
   while (emp.apellido<>'1') do
      begin
        writeln('ingrese nombre');
        readln(emp.nombre);
        writeln('ingresar numero de empleado');
        readln(emp.num_e);
        writeln('ingresar edad');
        readln(emp.edad);
        writeln('ingrsar DNI');
        readln(emp.dni);
        write(emp_a, emp);
        writeln('ingrese apellido del empleado: ');
        readln(emp.apellido);
      end;
end;
var
arch_emp: archivo1;
nombreA:cadena;
x:integer;
apellido: cadena;
nombre: cadena;
reg_e:empleados;
begin
 writeln('Menu de empleados: ');
 writeln('');
 writeln('Ingrese (1) si desea crear un Archivo de Empleados');
 writeln('Si desea Buscar dentro de un archivo de empleados ya creado:');
 writeln('   Ingrese (2) para recibir los datos de X empleado');
 writeln('   Ingrese (3) para listar en pantalla todos los empleados');
 writeln('   Ingrese (4) para conocer los empleados proximos a jubilarse');
 readln(x);
 if (x=1) then
  begin
    writeln('ingrese nombre del archivo de empleados');
    readln(nombreA);
    assign(arch_emp, nombreA);
    rewrite(arch_emp);
    agregarEmp(arch_emp);
    close(arch_emp);
  end
 else
  begin
    writeln('Seleccione el archivo de empleado que desea revisar');
    readln(nombreA);
    assign(arch_emp,'C:\Dev-Pas\Archivo_Empleados');
    reset(arch_emp);
    if(x=2) then
     begin
       writeln('ingrese el apellido: ');
       readln(apellido);
       writeln(' y nombre del empleado a buscar');
       readln(nombre);
       read(arch_emp, reg_e);
       while (reg_e.apellido <> apellido) and (reg_e.nombre <> nombre) or (not eof(arch_emp)) do
        begin
         read(arch_emp,reg_e);
        end;
       writeln('Los datos de: ',reg_e.apellido,' ', reg_e.nombre, 'son:');
       writeln('numero de empleado: ',reg_e.num_e);
       writeln('edad: ',reg_e.edad);
       writeln('dni: ',reg_e.dni);
       if (eof(arch_emp)) then
          writeln('No existe el empleado');
     end
   else
     begin
       if(x=3) then
         begin
           while (not eof(arch_emp)) do
            begin
             read(arch_emp,reg_e);
             writeln('Los datos de: ',reg_e.apellido,' ', reg_e.nombre, 'son:');
             writeln('numero de empleado: ',reg_e.num_e);
             writeln('edad: ',reg_e.edad);
             writeln('dni: ',reg_e.dni);
             writeln('');
            end;
         end
       else
         begin
           while (not eof(arch_emp)) do
             begin
               read(arch_emp,reg_e);
               if (reg_e.edad >= 60) then
                 begin
                   writeln('Los datos de: ',reg_e.apellido,' ', reg_e.nombre, 'son:');
                   writeln('numero de empleado: ',reg_e.num_e);
                   writeln('edad: ',reg_e.edad);
                   writeln('dni: ',reg_e.dni);
                   writeln('');
                 end;
             end;
        end;
     end;
   end;
readln(nombreA);
end.





