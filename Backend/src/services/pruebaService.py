from .flightService import FlightService
from ..models.flight import Flight


def main():
    print("=== PRUEBA FLIGHT SERVICE ===\n")

    service = FlightService()

    # -------------------------
    # CREAR VUELOS
    # -------------------------
    print("Creando vuelos...\n")

    f1 = Flight("SB100", "BOG", "MED", "10:00", 100, 50, False, False)
    f2 = Flight("SB200", "BOG", "CALI", "12:00", 120, 60, False, False)
    f3 = Flight("SB150", "BOG", "CTG", "11:00", 110, 55, False, False)

    service.create_flight(f1)
    service.create_flight(f2)
    service.create_flight(f3)

    print("Vuelos creados.\n")

    # -------------------------
    # BUSCAR
    # -------------------------
    print("Buscando vuelo SB150...")
    vuelo = service.find_flight("SB150")
    print("Resultado:", vuelo, "\n")

    # -------------------------
    # ELIMINAR
    # -------------------------
    print("Eliminando vuelo SB100...")
    service.delete_flight("SB100")

    print("Buscando SB100 después de eliminar...")
    vuelo = service.find_flight("SB100")
    print("Resultado:", vuelo, "\n")

    # -------------------------
    # UNDO DELETE
    # -------------------------
    print("Deshaciendo eliminación...")
    service.undo()

    print("Buscando SB100 después de undo...")
    vuelo = service.find_flight("SB100")
    print("Resultado:", vuelo, "\n")

    # -------------------------
    # ACTUALIZAR
    # -------------------------
    print("Actualizando precio de SB200...")
    service.update_flight("SB200", {"precioBase": 999})

    vuelo = service.find_flight("SB200")
    print("Nuevo precio:", vuelo.precioBase, "\n")

    print("Deshaciendo actualización...")
    service.undo()

    vuelo = service.find_flight("SB200")
    print("Precio restaurado:", vuelo.precioBase, "\n")

    # -------------------------
    # CANCELAR (subárbol)
    # -------------------------
    print("Cancelando vuelo SB150 (subárbol)...")
    service.cancel_flight("SB150")

    print("Buscando SB150 después de cancelar...")
    vuelo = service.find_flight("SB150")
    print("Resultado:", vuelo, "\n")

    print("Deshaciendo cancelación...")
    service.undo()

    print("Buscando SB150 después de undo...")
    vuelo = service.find_flight("SB150")
    print("Resultado:", vuelo, "\n")

    print("=== FIN DE PRUEBA ===")


if __name__ == "__main__":
    main()
