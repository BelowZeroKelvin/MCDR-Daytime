#coding: utf-8

PLUGIN_METADATA = {
	'id': 'daytime',
	'version': '1.0.0',
	'name': 'Daytime',  # RText component is allowed
	'description': 'show time in minecraft',  # RText component is allowed
	'author': 'ZeroKelvin',
	'link': 'https://github.com/BelowZeroKelvin/MCDR-Daytime/blob/master/Daytime.py',
	'dependencies': {
		'mcdreforged': '>=0.9.0',
	}
}

daytime = 0
daytime_updated = True


def daytime_format(daytime):
    daytime = (int(daytime) + 6000) % 24000
    hour = int(daytime / 1000)
    minute = int((daytime % 1000) / 1000 * 60)
    return '[游戏内时间] {:0>2d}:{:0>2d}'.format(hour, minute)


def on_info(server, info):
    global daytime_updated, daytime
    if info.source == 0 and daytime_updated==False and not info.is_player and info.content.startswith(
            'The time is'):
        daytime = info.content[12:]
        server.say(daytime_format(daytime))
        daytime_updated = True
    elif info.is_player and info.content == '!!daytime':
        daytime_updated = False
        server.execute('time query daytime')
