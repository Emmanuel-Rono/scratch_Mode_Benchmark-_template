from abc import ABC, abstractmethod


class ArtifactAdapter(ABC):
    @abstractmethod
    def get(self, selector: str):
        raise NotImplementedError

    def exists(self, selector: str) -> bool:
        try:
            self.get(selector)
            return True
        except Exception:
            return False
