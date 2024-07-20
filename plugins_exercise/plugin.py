from abc import abstractmethod, ABC

class Plugin(ABC):
    @abstractmethod
    def connectivity_test(self):
        raise NotImplementedError()

    @abstractmethod
    def collect(self):
        raise NotImplementedError()

    def run(self):
        try:
            if self.connectivity_test():
                self.collect()

        except Exception:
            print("Ended with error")