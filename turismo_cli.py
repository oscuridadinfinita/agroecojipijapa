"""Sistema de gestión de datos para turismo comunitario en Jipijapa."""

import csv
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Iterable, Tuple

DB_NAME = "turismo.db"


def inicializar_bd(db_path: Path) -> None:
    """Crear tablas requeridas en la base de datos si no existen."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS comunidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                provincia TEXT NOT NULL,
                canton TEXT NOT NULL,
                poblacion INTEGER NOT NULL
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS atractivos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comunidad_id INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                FOREIGN KEY (comunidad_id) REFERENCES comunidades(id)
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS guias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comunidad_id INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                especialidad TEXT NOT NULL,
                contacto TEXT NOT NULL,
                FOREIGN KEY (comunidad_id) REFERENCES comunidades(id)
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS visitas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                atractivo_id INTEGER NOT NULL,
                guia_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                numero_visitantes INTEGER NOT NULL,
                FOREIGN KEY (atractivo_id) REFERENCES atractivos(id),
                FOREIGN KEY (guia_id) REFERENCES guias(id)
            )
            """
        )
        conn.commit()


def agregar_comunidad(db_path: Path, nombre: str, provincia: str, canton: str, poblacion: int) -> None:
    """Insertar una nueva comunidad en la base de datos."""
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT INTO comunidades (nombre, provincia, canton, poblacion) VALUES (?, ?, ?, ?)",
            (nombre, provincia, canton, poblacion),
        )
        conn.commit()


def agregar_atractivo(
    db_path: Path,
    comunidad_id: int,
    nombre: str,
    tipo: str,
    descripcion: str,
) -> None:
    """Registrar un nuevo atractivo asociado a una comunidad."""
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT INTO atractivos (comunidad_id, nombre, tipo, descripcion) VALUES (?, ?, ?, ?)",
            (comunidad_id, nombre, tipo, descripcion),
        )
        conn.commit()


def agregar_guia(db_path: Path, comunidad_id: int, nombre: str, especialidad: str, contacto: str) -> None:
    """Registrar un nuevo guía turístico para una comunidad específica."""
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT INTO guias (comunidad_id, nombre, especialidad, contacto) VALUES (?, ?, ?, ?)",
            (comunidad_id, nombre, especialidad, contacto),
        )
        conn.commit()


def agregar_visita(
    db_path: Path,
    atractivo_id: int,
    guia_id: int,
    fecha: str,
    numero_visitantes: int,
) -> None:
    """Registrar una visita a un atractivo turístico con su guía responsable."""
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT INTO visitas (atractivo_id, guia_id, fecha, numero_visitantes) VALUES (?, ?, ?, ?)",
            (atractivo_id, guia_id, fecha, numero_visitantes),
        )
        conn.commit()


def listar_registros(db_path: Path, tabla: str) -> Iterable[Tuple]:
    """Obtener todos los registros de una tabla específica."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(f"SELECT * FROM {tabla}")
        yield from cursor.fetchall()


def exportar_a_csv(db_path: Path, carpeta_destino: Path) -> None:
    """Exportar las tablas disponibles a archivos CSV dentro de una carpeta destino."""
    carpeta_destino.mkdir(parents=True, exist_ok=True)
    tablas = {
        "comunidades": ["id", "nombre", "provincia", "canton", "poblacion"],
        "atractivos": ["id", "comunidad_id", "nombre", "tipo", "descripcion"],
        "guias": ["id", "comunidad_id", "nombre", "especialidad", "contacto"],
        "visitas": ["id", "atractivo_id", "guia_id", "fecha", "numero_visitantes"],
    }

    with sqlite3.connect(db_path) as conn:
        for tabla, columnas in tablas.items():
            ruta_archivo = carpeta_destino / f"{tabla}.csv"
            with closing(conn.cursor()) as cursor:
                cursor.execute(f"SELECT * FROM {tabla}")
                filas = cursor.fetchall()

            with ruta_archivo.open("w", newline="", encoding="utf-8") as archivo_csv:
                escritor = csv.writer(archivo_csv)
                escritor.writerow(columnas)
                escritor.writerows(filas)


def pedir_entero(mensaje: str) -> int:
    """Solicitar un número entero válido al usuario."""
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Por favor, introduce un número válido.")


def menu() -> None:
    """Ejecutar el menú principal de la aplicación en la línea de comandos."""
    db_path = Path(DB_NAME)
    inicializar_bd(db_path)

    opciones = {
        "1": "Añadir comunidad",
        "2": "Listar comunidades",
        "3": "Añadir atractivo",
        "4": "Listar atractivos",
        "5": "Añadir guía",
        "6": "Listar guías",
        "7": "Registrar visita",
        "8": "Listar visitas",
        "9": "Exportar datos a CSV",
        "0": "Salir",
    }

    while True:
        print("\nSistema de turismo comunitario")
        for clave, descripcion in opciones.items():
            print(f"{clave}. {descripcion}")

        seleccion = input("Selecciona una opción: ").strip()

        if seleccion == "1":
            nombre = input("Nombre de la comunidad: ")
            provincia = input("Provincia: ")
            canton = input("Cantón: ")
            poblacion = pedir_entero("Población estimada: ")
            agregar_comunidad(db_path, nombre, provincia, canton, poblacion)
            print("Comunidad registrada correctamente.")
        elif seleccion == "2":
            registros = listar_registros(db_path, "comunidades")
            print("\nComunidades registradas:")
            for registro in registros:
                print(registro)
        elif seleccion == "3":
            comunidad_id = pedir_entero("ID de la comunidad: ")
            nombre = input("Nombre del atractivo: ")
            tipo = input("Tipo de atractivo: ")
            descripcion = input("Descripción: ")
            agregar_atractivo(db_path, comunidad_id, nombre, tipo, descripcion)
            print("Atractivo registrado correctamente.")
        elif seleccion == "4":
            registros = listar_registros(db_path, "atractivos")
            print("\nAtractivos registrados:")
            for registro in registros:
                print(registro)
        elif seleccion == "5":
            comunidad_id = pedir_entero("ID de la comunidad: ")
            nombre = input("Nombre del guía: ")
            especialidad = input("Especialidad del guía: ")
            contacto = input("Información de contacto: ")
            agregar_guia(db_path, comunidad_id, nombre, especialidad, contacto)
            print("Guía registrado correctamente.")
        elif seleccion == "6":
            registros = listar_registros(db_path, "guias")
            print("\nGuías registrados:")
            for registro in registros:
                print(registro)
        elif seleccion == "7":
            atractivo_id = pedir_entero("ID del atractivo: ")
            guia_id = pedir_entero("ID del guía: ")
            fecha = input("Fecha de la visita (AAAA-MM-DD): ")
            numero_visitantes = pedir_entero("Número de visitantes: ")
            agregar_visita(db_path, atractivo_id, guia_id, fecha, numero_visitantes)
            print("Visita registrada correctamente.")
        elif seleccion == "8":
            registros = listar_registros(db_path, "visitas")
            print("\nVisitas registradas:")
            for registro in registros:
                print(registro)
        elif seleccion == "9":
            carpeta = input("Carpeta destino para CSV (por defecto 'exportaciones'): ").strip() or "exportaciones"
            exportar_a_csv(db_path, Path(carpeta))
            print(f"Datos exportados en la carpeta '{carpeta}'.")
        elif seleccion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()

# Este sistema puede sincronizarse con una aplicación móvil almacenando temporalmente los registros en la app, y usando una rutina de sincronización que suba los datos al servidor cuando el dispositivo detecte conexión estable.
