import platform
import sys

def show_system_info():
    """Выводит имя и версию ОС, а также версию Python"""
    print("=" * 50)
    print("ИНФОРМАЦИЯ О СИСТЕМЕ")
    print("=" * 50)

    # Имя операционной системы
    os_name = platform.system()          # Windows / Linux / Darwin
    os_release = platform.release()      # версия
    os_version = platform.version()      # подробная версия

    print(f"Операционная система : {os_name}")
    print(f"Версия               : {os_release}")
    print(f"Подробная версия     : {os_version}")
    print(f"Полная платформа     : {platform.platform()}")
    print(f"Архитектура          : {platform.machine()}")
    print(f"Процессор            : {platform.processor()}")

    # Версия Python
    print("-" * 50)
    print(f"Версия Python        : {platform.python_version()}")
    print(f"Реализация           : {platform.python_implementation()}")
    print(f"Путь к интерпретатору: {sys.executable}")
    print("=" * 50)


if __name__ == "__main__":
    show_system_info()
