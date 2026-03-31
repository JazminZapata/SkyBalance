from ..models.node import Node
from ..models.flight import Flight
from ..models.avl import AVL

# =========================
# ACTIONS (Command Pattern)
# =========================

class Action:
    def undo(self, tree: AVL):
        pass


class CreateAction(Action):
    def __init__(self, node):
        self.node = node

    def undo(self, tree: AVL):
        tree.delete(self.node.getValue())


class DeleteAction(Action):
    def __init__(self, node):
        self.node = node

    def undo(self, tree: AVL):
        tree.insert(self.node)


class UpdateAction(Action):
    def __init__(self, node, old_data):
        self.node = node
        self.old_data = old_data

    def undo(self, tree: AVL):
        self.node.value = self.old_data


class CancelAction(Action):
    def __init__(self, nodes):
        self.nodes = nodes  # lista de nodos del subárbol

    def undo(self, tree: AVL):
        for node in self.nodes:
            tree.insert(node)


# =========================
# HISTORY MANAGER
# =========================

class HistoryManager:
    def __init__(self):
        self.stack = []

    def push(self, action: Action):
        self.stack.append(action)

    def undo(self, tree: AVL):
        if not self.stack:
            print("No hay acciones para deshacer")
            return

        action = self.stack.pop()
        action.undo(tree)


# =========================
# FLIGHT SERVICE
# =========================

class FlightService:

    def __init__(self):
        self.tree = AVL()
        self.history = HistoryManager()

    # -------------------------
    # CREATE
    # -------------------------
    def create_flight(self, flight: Flight):
        node = Node(flight)
        self.tree.insert(node)

        self.history.push(CreateAction(node))

    # -------------------------
    # DELETE (eliminación normal)
    # -------------------------
    def delete_flight(self, codigo):
        node = self.tree.search(codigo)

        if node:
            self.tree.delete(codigo)
            self.history.push(DeleteAction(node))
        else:
            print("Vuelo no encontrado")

    # -------------------------
    # UPDATE
    # -------------------------
    def update_flight(self, codigo, new_data: dict):
        node = self.tree.search(codigo)

        if node:
            old_data = node.getValue()

            # hacemos una copia (importante)
            old_copy = Flight(
                old_data.codigo,
                old_data.origen,
                old_data.destino,
                old_data.horaSalida,
                old_data.precioBase,
                old_data.pasajeros,
                old_data.promocion,
                old_data.alerta
            )

            # actualizar atributos
            for key, value in new_data.items():
                setattr(node.getValue(), key, value)

            self.history.push(UpdateAction(node, old_copy))
        else:
            print("Vuelo no encontrado")

    # -------------------------
    # CANCEL (subárbol completo)
    # -------------------------
    def cancel_flight(self, codigo):
        node = self.tree.search(codigo)

        if node:
            subtree_nodes = self.__get_subtree(node)

            # eliminar todos los nodos
            for n in subtree_nodes:
                self.tree.delete(n.getValue())

            self.history.push(CancelAction(subtree_nodes))
        else:
            print("Vuelo no encontrado")

    # -------------------------
    # UNDO
    # -------------------------
    def undo(self):
        self.history.undo(self.tree)

    # -------------------------
    # SEARCH (opcional helper)
    # -------------------------
    def find_flight(self, codigo):
        node = self.tree.search(codigo)
        return node.getValue() if node else None

    # -------------------------
    # AUXILIAR
    # -------------------------
    def __get_subtree(self, node):
        nodes = []

        def traverse(n):
            if n:
                nodes.append(n)
                traverse(n.getLeftChild())
                traverse(n.getRightChild())

        traverse(node)
        return nodes