
config = [
	(
		"Dual screen configuration (copy)",
		["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--same-as", "eDP1"],
		"video-television",
		False
	), (
		"Dual screen configuration (VGA on the right)",
		["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--right-of", "eDP1"],
		"video-television",
		True
	), (
		"Dual screen configuration (VGA on top)",
		["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--above", "eDP1"],
		"video-television",
		False
	), (
		"Single screen configuration",
		["xrandr", "--output", "eDP1", "--auto", "--output", "VGA1", "--off"],
		"computer-laptop",
		False
	), None, (
		"Roubaix Wi-Fi",
		["kdesudo", "/sbin/iwconfig", "wlan0", "essid", "NUMERICABLE-CD62"],
		"network-wireless-100",
		False
	), None, (
		"Ensembl Compara release coordination",
		["kwrite", "/home/matthieu/workspace/cvs/head/ensembl-compara/docs/ReleaseCoordination.txt"],
		"/home/matthieu/src/ebang-400dpi.png",
		False
	),
]

