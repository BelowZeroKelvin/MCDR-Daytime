daytime = 0
daytime_updated = True


def daytime_format(daytime):
    daytime = (int(daytime) + 6000) % 24000
    hour = int(daytime / 1000)
    minute = int((daytime % 1000) / 1000 * 60)
    return '[游戏内时间] {:0>2d}:{:0>2d}'.format(hour, minute)


def on_info(server, info):
    global daytime_updated, daytime
    if info.source == 0 and not info.is_player and info.content.startswith(
            'The time is'):
        daytime = info.content[12:]
        daytime_updated = True
    elif info.is_player and info.content == '!!daytime':
        daytime_updated = False
        server.execute('time query daytime')
        while not daytime_updated:
            pass
        server.say(daytime_format(daytime))
