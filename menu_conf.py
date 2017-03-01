
import menu_conf_type

config = menu_conf_type.tc_menu(
	title = 'Useful commands',
	icon  = 'view-list-details',
	items = [
		menu_conf_type.tc_menu(
			title = 'Screen configuration',
			icon = 'video-display',
			items = [
				menu_conf_type.new_menu_item(
					name = "Dual screen configuration (copy)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--same-as", "eDP1"],
				), menu_conf_type.new_menu_item(
					name = "Dual screen configuration (VGA on the right)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--right-of", "eDP1"],
					run_at_startup = True,
				), menu_conf_type.new_menu_item(
					name = "Dual screen configuration (VGA on top)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--above", "eDP1"],
				), menu_conf_type.new_menu_item(
					name = "Only the laptop screen",
					icon = "computer-laptop",
					command = ["xrandr", "--output", "eDP1", "--auto", "--output", "VGA1", "--off"],
				), menu_conf_type.new_menu_item(
					name = "Only the external monitor",
					icon = "video-display",
					command = ["xrandr", "--output", "eDP1", "--off", "--output", "VGA1", "--auto"],
				#), None, menu_conf_type.new_menu_item(
					#name = "Kill plymouth",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "plymouth", "quit"],
				#), menu_conf_type.new_menu_item(
					#name = "powersave",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "pm-powersave", "true"],
				#), menu_conf_type.new_menu_item(
					#name = "eth2 dowm",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "ifconfig", "eth2", "down"],
				#), menu_conf_type.new_menu_item(
					#name = "eth2 up",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "ifconfig", "eth2", "up"],
				)]
		), menu_conf_type.tc_menu(
			title = "Compara documentation",
			icon = "/home/matthieu/src/local/ebang-400dpi.png",
			items = [
				menu_conf_type.new_menu_item(
					name = "Protein-side schema",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/schema/diagrams/protein_schema.png",
				), menu_conf_type.new_menu_item(
					name = "Genomic-side schema",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/schema/diagrams/genomic_schema.png",
				), menu_conf_type.new_menu_item(
					name = "eHive schema",
					command = "/home/matthieu/workspace/src/hive/master/docs/hive_schema.png",
				), None, menu_conf_type.new_menu_item(
					name = "Protein-tree pipeline",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/ProteinTrees.png",
				), menu_conf_type.new_menu_item(
					name = "ncRNA-tree pipeline",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/ncRNAtrees.png",
				), menu_conf_type.new_menu_item(
					name = "Family pipeline",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/Families.png",
				), None, menu_conf_type.new_menu_item(
					name = "Pairwise-aligner pipeline",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/Pairwise.png",
				), menu_conf_type.new_menu_item(
					name = "EPO pipeline",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/epo_pt3.png",
				), menu_conf_type.new_menu_item(
					name = "EPO-2X pipeline",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/EpoLowCoverage.png",
				), menu_conf_type.new_menu_item(
					name = "Mercator-Pecan pipeline",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/MercatorPecan.png",
				), menu_conf_type.new_menu_item(
					name = "Other pipelines",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams",
				), None, menu_conf_type.new_menu_item(
					name = "ensembl-compara checkout",
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/",
				)]
		#), menu_conf_type.tc_menu(
			#title = "Daemons",
			#icon = "application-x-executable",
			#items = [
				#menu_conf_type.new_menu_item(
					#name = "gitit",
					#command = "/home/matthieu/gitit/gitit.sh",
					#background = True,
				#)]
		)]
)

