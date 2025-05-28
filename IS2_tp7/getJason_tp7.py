
"""
getJason.py - versión 1.1

Copyright UADER FCyT-IS2©2024 todos los derechos reservados.

Este programa permite recuperar una clave específica desde un archivo JSON.
Refactorizado aplicando Programación Orientada a Objetos, patrón Singleton y control robusto de errores.
"""

import json
import sys
import os


class JSONReaderSingleton:
    """Clase Singleton para lectura de archivos JSON."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(JSONReaderSingleton, cls).__new__(cls)
        return cls._instance

    def read_json(self, filename):
        """Lee el contenido de un archivo JSON."""
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"Archivo '{filename}' no encontrado.")
        with open(filename, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                raise ValueError(f"El archivo '{filename}' no contiene JSON válido.")

    def get_value(self, data, key):
        """Devuelve el valor asociado a la clave, o lanza excepción."""
        if key not in data:
            raise KeyError(f"La clave '{key}' no existe en el archivo JSON.")
        return data[key]


class JSONApp:
    """Clase principal de la aplicación."""

    VERSION = "1.1"

    def __init__(self, args):
        self.args = args
        self.json_file = None
        self.key = "token1"

    def parse_args(self):
        """Procesa y valida los argumentos de línea de comandos."""
        if "-v" in self.args or "--version" in self.args:
            print(f"Versión: {self.VERSION}")
            sys.exit(0)

        if len(self.args) < 2:
            self.usage_error("Faltan argumentos. Uso correcto: python getJason.py <archivo_json> [clave]")

        self.json_file = self.args[1]
        if len(self.args) > 2:
            self.key = self.args[2]

    def usage_error(self, message):
        """Muestra un error controlado y termina el programa."""
        print(f"Error: {message}")
        print("Uso: python getJason.py <archivo_json> [clave]")
        sys.exit(1)

    def run(self):
        """Ejecuta la lógica del programa con control de errores."""
        self.parse_args()
        reader = JSONReaderSingleton()
        try:
            data = reader.read_json(self.json_file)
            value = reader.get_value(data, self.key)
            print(value)
        except (FileNotFoundError, ValueError, KeyError) as e:
            print(f"Error: {e}")
            sys.exit(1)


def main():
    """Punto de entrada principal."""
    app = JSONApp(sys.argv)
    app.run()


if __name__ == "__main__":
    main()
