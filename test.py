import requests

class PasswordGen:
    def __init__(self, char, caps, sim):
        self.caps = caps
        #self.num = num
        self.sim = sim
        self.char = char
        self.generated_password = None  # Initialize generated_password attribute

    def set_parameters(self,caps, char, sim):
        self.caps = caps
        #self.num = num
        self.sim = sim
        self.char = char

    def pass_gen(self):
        url = f"https://passwordinator.onrender.com?num=true{self.sim}{self.caps}&len={self.char}"
        response = requests.get(url)
        self.generated_password = response.text  # Store the generated password
        return self.generated_password

# Example usage:
password_generator = PasswordGen(sim='&char=true',caps= '&caps=true',char=12)
password_generator.pass_gen()  # Generates and stores the password
print(password_generator.generated_password)  # Access the generated password

# Update parameters and generate a new password
password_generator.set_parameters(sim='', caps= '',char=15)
password_generator.pass_gen()
print(password_generator.generated_password)
