from endstone.plugin import Plugin
from endstone.command import Command, CommandSender
from endstone import Server

class TPS(Plugin):
    api_version = "0.10"
    average_tps: float

    commands = {
        "tps": {
            "description": "Show server's TPS.",
            "usages": ["/tps"],
        }
    }
    def on_command(self, sender: CommandSender, command: Command, args: list[str]) -> bool:
        if command.name == "tps":
            tps = self.server.average_tps
            sender.send_message(f"§aServer TPS: §f{tps:.2f}")

        return True

    def on_load(self) -> None:
        self.logger.info("on_load is called!")
    def on_enable(self) -> None:
        self.logger.info("on_enable is called!")
    def on_disable(self) -> None:
        self.logger.info("on_disable is called!")
