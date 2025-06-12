def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre cero"

def calculadora():
    print("=== CALCULADORA BÁSICA ===")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")
    print("=" * 27)
    
    while True:
        try:
            opcion = input("\nSelecciona una operación (1-5): ")
            
            if opcion == '5':
                print("¡Gracias por usar la calculadora!")
                break
            
            if opcion not in ['1', '2', '3', '4']:
                print("Opción no válida. Por favor, selecciona un número del 1 al 5.")
                continue
            
            # Solicitar los números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            # Realizar la operación según la opción seleccionada
            if opcion == '1':
                resultado = suma(num1, num2)
                operador = "+"
            elif opcion == '2':
                resultado = resta(num1, num2)
                operador = "-"
            elif opcion == '3':
                resultado = multiplicacion(num1, num2)
                operador = "*"
            elif opcion == '4':
                resultado = division(num1, num2)
                operador = "/"
            
            # Mostrar el resultado
            print(f"\nResultado: {num1} {operador} {num2} = {resultado}")
            
            # Preguntar si desea continuar
            continuar = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
            if continuar != 's':
                print("¡Gracias por usar la calculadora!")
                break
                
        except ValueError:
            print("Error: Por favor, ingresa números válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Versión simplificada para una sola operación
def calculadora_simple():
    print("=== CALCULADORA SIMPLE ===")
    try:
        num1 = float(input("Ingresa el primer número: "))
        operador = input("Ingresa la operación (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División entre cero"
        else:
            resultado = "Operador no válido"
        
        print(f"Resultado: {num1} {operador} {num2} = {resultado}")
        
    except ValueError:
        print("Error: Por favor, ingresa números válidos.")


if __name__ == "__main__":
    
    calculadora()  
    