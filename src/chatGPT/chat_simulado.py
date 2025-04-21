import os
import sys

# Intentar importar readline (Linux/macOS) o pyreadline3 (Windows)
try:
    import readline  # Para historial de comandos en Linux/macOS
except ImportError:
    try:
        import pyreadline3 as readline  # Para historial de comandos en Windows
    except ImportError:
        print("Advertencia: readline no est谩 disponible. Las funciones de historial podr铆an no funcionar.")

from dotenv import load_dotenv  # Permite cargar variables desde el archivo .env
from openai import OpenAI  # Cliente oficial de OpenAI

# Cargar variables del archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # Obtener la clave de API

# Verificaci贸n de la API Key
if not api_key:
    # Si no se encuentra la API Key, mostrar mensaje y salir
    print(" error: no se encontr贸 la clave de API.")
    print(" Asegurate de tener un archivo .env con la variable:")
    print("OPENAI_API_KEY=tu_clave_aqui")
    sys.exit(1)

# Crear cliente OpenAI con la API Key cargada
client = OpenAI(api_key=api_key)

# Funci贸n que realiza la consulta al modelo de lenguaje
def hacer_consulta(userquery):
    """
    Env铆a la consulta del usuario al modelo de OpenAI y devuelve la respuesta.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",  # Modelo utilizado
            messages=[
                {"role": "system", "content": "Sos un asistente que responde en español."},  # Instrucci贸n inicial
                {"role": "user", "content": userquery}  # Consulta del usuario
            ],
            temperature=1,
            max_tokens=16384,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extraer y mostrar respuesta del modelo
        jsonStr = response.choices[0].message.content
        print(f"\nchatGPT: {jsonStr}\n")
        return userquery

    except Exception as e:
        # En caso de error, mostrarlo por consola
        print("\nchatGPT:  Ocurrio un error al invocar la API:")
        print(e)
        return None

# Funci贸n principal que gestiona el ciclo de preguntas y respuestas
def main():
    """
    Funci贸n principal del programa. Permite al usuario ingresar consultas.
    """
    ultima_consulta = ""  # Guarda la altima consulta para poder repetirla

    print(" Simulador de ChatGPT. Escribe una consulta o presione 'Flecha Arriba' para repetir la altima.")
    while True:
        try:
            entrada = input("You: ")  # Solicita entrada al usuario
            if not entrada.strip():
                continue
            if entrada == '\x1b[A' and ultima_consulta:  # Repetir altima consulta si se presiona flecha arriba
                entrada = ultima_consulta
            ultima_consulta = hacer_consulta(entrada)
        except KeyboardInterrupt:
            # Termina el programa con Ctrl+C
            print("\n馃憢 Programa terminado por el usuario.")
            sys.exit()

# Ejecutar la funcion principal si el script se corre directamente
if __name__ == "__main__":
    main()