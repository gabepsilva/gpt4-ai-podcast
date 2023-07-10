from core.person import Person

class Host(Person):
    def __init__(self):
        super().__init__()

        self.persona = "Host"
    

    def introduce_guest(self) -> str:

        ctx = {
            "role": "user",
            "content": "Host: Introduce your guest in 15 seconds"
        }

        self.chat_memory.append(ctx)

        return self.say()



