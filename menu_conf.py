
import menu_conf_type

config = menu_conf_type.tc_menu(
	title = 'Useful commands',
	icon  = 'favorites',
	items = [
		menu_conf_type.tc_menu(
			title = 'System commands',
			icon = 'preferences-system',
			items = [
				menu_conf_type.tc_item(
					name = "Dual screen configuration (copy)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--same-as", "eDP1"],
					do_exec = False,
				), menu_conf_type.tc_item(
					name = "Dual screen configuration (VGA on the right)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--right-of", "eDP1"],
					do_exec = True,
				), menu_conf_type.tc_item(
					name = "Dual screen configuration (VGA on top)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--above", "eDP1"],
					do_exec = False,
				), menu_conf_type.tc_item(
					name = "Single screen configuration",
					icon = "computer-laptop",
					command = ["xrandr", "--output", "eDP1", "--auto", "--output", "VGA1", "--off"],
					do_exec = False,
				), None, menu_conf_type.tc_item(
					name = "Roubaix Wi-Fi",
					icon = "network-wireless-100",
					command = ["kdesudo", "/sbin/iwconfig", "wlan0", "essid", "NUMERICABLE-CD62"],
					do_exec = False,
				)]
		), menu_conf_type.tc_menu(
			title = "Compara documentation",
			icon = "/home/matthieu/src/ebang-400dpi.png",
			items = [
				menu_conf_type.tc_item(
					name = "Protein-side schema",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/schema/diagrams/protein_schema.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "Genomic-side schema",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/schema/diagrams/genomic_schema.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "eHive schema",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-hive/docs/hive_schema.png",
					do_exec = False
				), None, menu_conf_type.tc_item(
					name = "Protein-tree pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams/ProteinTrees.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "ncRNA-tree pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams/ncRNAtrees.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "Family pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams/Families.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "Other pipelines",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams",
					do_exec = False
				)]
		), menu_conf_type.tc_menu(
			title = "Daemons",
			icon = "application-x-executable",
			items = [
				menu_conf_type.tc_item(
					name = "guiHive",
					icon = None,
					command = "/home/matthieu/src/guiHive/server/server.sh",
					do_exec = 'tickbox'
				), menu_conf_type.tc_item(
					name = "gitit",
					icon = None,
					command = "/home/matthieu/gitit/gitit.sh",
					do_exec = 'tickbox'
				)]
		)]
)

