# Item 2 — Saves and restores named versions of the tree
import json
import os

class VersionManager:

    def __init__(self):
        self.versions = {}
        # Load versions from disk if the file already exists
        if os.path.exists("versions.json"):
            with open("versions.json", "r", encoding="utf-8") as f:
                self.versions = json.load(f)

    def _persist(self):
        # Write the versions dictionary to disk
        with open("versions.json", "w", encoding="utf-8") as f:
            json.dump(self.versions, f, indent=4, ensure_ascii=False)

    def save(self, name: str, tree):
        # Save current tree structure and depth limit under the given name
        self.versions[name] = {
            "copy": tree.toJSON(tree.root),
            "limite": tree.limite
        }
        self._persist()
        print(f"Version '{name}' saved.")

    def restore(self, name: str, tree):
        if name not in self.versions:
            print(f"Version '{name}' not found.")
            return
        from loader import buildByTopology
        entry = self.versions[name]
        # Rebuild tree from saved copy and restore depth limit
        tree.root = buildByTopology(entry["copy"])
        tree.limite = entry["limite"]
        tree.recalculatePrices()
        print(f"Version '{name}' restored.")

    def list_versions(self):
        if not self.versions:
            print("No saved versions.")
            return
        for name in self.versions:
            print(f"- {name} (limit: {self.versions[name]['limite']})")

    def delete_version(self, name: str):
        if name not in self.versions:
            print(f"Version '{name}' not found.")
            return
        del self.versions[name]
        self._persist()
        print(f"Version '{name}' deleted.")

# End Item 2