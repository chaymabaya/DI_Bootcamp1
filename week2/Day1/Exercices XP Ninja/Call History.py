class phone :
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.add = []
    def call(self , other_phone):
        call_message = f'{self.phone_number} is calling {other_phone.phone_number}'
        print(call_message)
        self.call_history.append(call_message)
    def show_history(self):
        print(self.call_history)
    def send_message(self, other_phone, content):
         message = {
        "to": other_phone.phone_number,
        "from": self.phone_number,
        "content": content
         }
         self.add.append(message)
         other_phone.add.append(message)
         print(f"Message sent from {self.phone_number} to {other_phone.phone_number}")
    def show_outgoing_messages(self):
        print("Outgoing messages:")
        for msg in self.add:
            if msg["from"] == self.phone_number:
                print(f" - To {msg['to']}: {msg['content']}")
    def show_incoming_messages(self):
        print("Incoming messages:")
        for msg in self.add:
            if msg["to"] == self.phone_number:
                print(f" - From {msg['from']}: {msg['content']}")
    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number}:")
        for msg in self.add:
            if msg["from"] == other_phone.phone_number:
                print(f" - {msg['content']}")
p1 = phone("0611111111")
p2 = phone("0622222222")

p1.send_message(p2, "Salut !")
p2.send_message(p1, "Bonjour, ça va ?")
p1.send_message(p2, "Oui ça va, merci !")

print("\n--- Messages sortants P1 ---")
p1.show_outgoing_messages()

print("\n--- Messages entrants P2 ---")
p2.show_incoming_messages()

print("\n--- Messages reçus par P1 de P2 ---")
p1.show_messages_from(p2)