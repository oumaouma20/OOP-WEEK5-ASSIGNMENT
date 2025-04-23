
class Smartphone:
    """Base class representing a generic smartphone"""
    
    def __init__(self, brand, model, storage_gb, battery_mah):
        """Constructor to initialize smartphone attributes"""
        self._brand = brand  # Encapsulated attribute
        self._model = model  # Encapsulated attribute
        self._storage = storage_gb  # Encapsulated attribute
        self._battery = battery_mah  # Encapsulated attribute
        self._power_on = False  # Encapsulated attribute
        
    def power_on(self):
        """Turn the phone on"""
        if not self._power_on:
            self._power_on = True
            return f"{self.get_full_name()} is now powered on"
        return f"{self.get_full_name()} is already on"
    
    def power_off(self):
        """Turn the phone off"""
        if self._power_on:
            self._power_on = False
            return f"{self.get_full_name()} is now powered off"
        return f"{self.get_full_name()} is already off"
    
    def get_full_name(self):
        """Return the full name of the phone"""
        return f"{self._brand} {self._model}"
    
    def check_storage(self):
        """Check available storage"""
        return f"{self.get_full_name()} has {self._storage}GB storage"
    
    def check_battery(self):
        """Check battery capacity"""
        return f"{self.get_full_name()} has {self._battery}mAh battery"
    
    def make_call(self, number):
        """Make a phone call"""
        if self._power_on:
            return f"Calling {number} from {self.get_full_name()}"
        return f"Cannot call - phone is powered off"
    
    # Encapsulation with getters and setters
    @property
    def brand(self):
        return self._brand
    
    @property
    def model(self):
        return self._model
    
    @property
    def storage(self):
        return self._storage
    
    @storage.setter
    def storage(self, value):
        if value > 0:
            self._storage = value
        else:
            print("Storage must be positive")
    
    @property
    def battery(self):
        return self._battery
    
    @battery.setter
    def battery(self, value):
        if value > 0:
            self._battery = value
        else:
            print("Battery capacity must be positive")


class FlagshipPhone(Smartphone):
    """Inherited class representing a flagship smartphone with additional features"""
    
    def __init__(self, brand, model, storage_gb, battery_mah, camera_mp, has_5g):
        """Constructor for flagship phones with additional attributes"""
        super().__init__(brand, model, storage_gb, battery_mah)
        self._camera = camera_mp  # Encapsulated attribute
        self._has_5g = has_5g  # Encapsulated attribute
    
    # Polymorphism - override the make_call method
    def make_call(self, number):
        """Make a phone call with additional 5G capability check"""
        if not self._power_on:
            return f"Cannot call - phone is powered off"
        
        if self._has_5g:
            return f"Calling {number} from {self.get_full_name()} with 5G connectivity"
        else:
            return super().make_call(number)
    
    def take_photo(self):
        """Take a high-resolution photo"""
        if self._power_on:
            return f"Taking {self._camera}MP photo with {self.get_full_name()}"
        return f"Cannot take photo - phone is powered off"
    
    # Additional getters for new properties
    @property
    def camera(self):
        return self._camera
    
    @property
    def has_5g(self):
        return self._has_5g


# Demonstration of the classes
if __name__ == "__main__":
    # Create a basic smartphone
    basic_phone = Smartphone("Nokia", "3310", 1, 1200)
    print(basic_phone.power_on())
    print(basic_phone.make_call("123-456-7890"))
    print(basic_phone.check_storage())
    print(basic_phone.check_battery())
    print(basic_phone.power_off())
    print()
    
    # Create a flagship smartphone
    flagship = FlagshipPhone("Samsung", "Galaxy S23", 256, 3900, 108, True)
    print(flagship.power_on())
    print(flagship.make_call("987-654-3210"))
    print(flagship.take_photo())
    print(flagship.check_storage())
    print(f"Camera: {flagship.camera}MP")
    print(f"Has 5G: {'Yes' if flagship.has_5g else 'No'}")