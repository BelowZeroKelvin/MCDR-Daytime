# coding: utf-8
from mcdreforged.api.types import PluginServerInterface, Info, CommandSource
from mcdreforged.api.command import Literal

daytime = 0
console_need = False
player_need = False


def daytime_format(daytime):
    daytime = (int(daytime) + 6000) % 24000
    hour = int(daytime / 1000)
    minute = int((daytime % 1000) / 1000 * 60)
    return "[游戏内时间] {:0>2d}:{:0>2d}".format(hour, minute)


def command_daytime(src: CommandSource):
    global player_need, console_need, daytime
    if src.is_console:
        console_need = True
    elif src.is_player:
        player_need = True
    src.get_server().execute("time query daytime")


def on_load(server: PluginServerInterface, prev_module):
    server.register_command(Literal("!!daytime").runs(command_daytime))


def on_info(server: PluginServerInterface, info: Info):
    global player_need, console_need, daytime
    if info.is_from_server and info.content.startswith("The time is "):
        daytime = info.content[12:]
        if player_need:
            server.say(daytime_format(daytime))
            player_need = False
        if console_need:
            server.logger.info(daytime_format(daytime))
            console_need = False
