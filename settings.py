LEVEL_MAP = [
'                            ',
'                            ',
'                            ',
'       XXXX           XX    ',
'   P        E               ',
'XXXXXXXXXXXXXXXX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

TILE_SIZE = 64
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TARGET_FPS = 60 

# colors 
BG_COLOR = '#060C17'
PLAYER_COLOR = '#C4F7FF'
TILE_COLOR = '#94D7F2'

# camera
CAMERA_BORDERS = {
	'left': 200,
	'right': 300,
	'top':150,
	'bottom': 250
}

MONSTER_DATA = {
	'test': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'boss': {'health': 300,'exp':250,'damage':12,'attack_type': 'claw',  'attack_sound':'audio/attack/claw.wav','speed': 1, 'resistance': 1, 'attack_radius': 20, 'notice_radius': 100},
	'spirit': {'health': 100,'exp':110,'damage':10,'attack_type': 'thunder', 'attack_sound':'audio/attack/fireball.wav', 'speed': 1, 'resistance': 3, 'attack_radius': 16, 'notice_radius': 60},
	'ninja': {'health': 120,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'audio/attack/slash.wav', 'speed': 1, 'resistance': 3, 'attack_radius': 16, 'notice_radius': 60}}

WEAPON_DATA = {
	'blaster':{'damage':10},
	'shotgun':{'damage':10}
}