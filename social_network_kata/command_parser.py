class CommandParser:
    
    def parse_command(self, command):
        if "->" in command:
            action = "POST"
            args = command.split(" -> ")
        
        return (action, args)