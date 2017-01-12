import os
import string
import sys

# Parse commands
commands = sys.argv
command = ''
base = 'List of devices attached'

if len(commands) >= 2:
	commands = commands[1:]
	for line in commands:
		command = command + ' ' + str(line)


# Parse device name
devices = os.popen('adb devices').read()
if '* daemon started successfully *' in devices:
	base = '* daemon started successfully *'
devices = devices.splitlines()

i = 0
while i < len(devices):
	line = devices[i]

	if base in line:
		devices.remove(line)
		break

	devices.remove(line)

for device_name in devices:
	if not device_name:
		continue

	device_name = device_name.split('\t')[0]

	# Execute adb command for every connected device
	print device_name
	os.system('adb -s ' + device_name + command)
