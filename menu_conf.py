
import menu_conf_type

config = menu_conf_type.tc_menu(
	title = 'Useful commands',
	icon  = 'view-list-details',
	items = [
		menu_conf_type.tc_menu(
			title = 'Screen configuration',
			icon = 'video-display',
			items = [
				menu_conf_type.tc_item(
					name = "Dual screen configuration (copy)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--same-as", "eDP1"],
					background = False,
					run_at_startup = False,
				), menu_conf_type.tc_item(
					name = "Dual screen configuration (VGA on the right)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--right-of", "eDP1"],
					background = False,
					run_at_startup = True,
				), menu_conf_type.tc_item(
					name = "Dual screen configuration (VGA on top)",
					icon = "video-television",
					command = ["xrandr", "--output", "eDP1", "--primary", "--auto", "--output", "VGA1", "--auto", "--above", "eDP1"],
					background = False,
					run_at_startup = False,
				), menu_conf_type.tc_item(
					name = "Single screen configuration",
					icon = "computer-laptop",
					command = ["xrandr", "--output", "eDP1", "--auto", "--output", "VGA1", "--off"],
					background = False,
					run_at_startup = False,
				), menu_conf_type.tc_item(
					name = "Single screen configuration",
					icon = "video-display",
					command = ["xrandr", "--output", "eDP1", "--off", "--output", "VGA1", "--auto"],
					background = False,
					run_at_startup = False,
				#), None, menu_conf_type.tc_item(
					#name = "Kill plymouth",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "plymouth", "quit"],
					#background = False,
					#run_at_startup = False,
				#), menu_conf_type.tc_item(
					#name = "powersave",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "pm-powersave", "true"],
					#background = False,
					#run_at_startup = False,
				#), menu_conf_type.tc_item(
					#name = "eth2 dowm",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "ifconfig", "eth2", "down"],
					#background = False,
					#run_at_startup = False,
				#), menu_conf_type.tc_item(
					#name = "eth2 up",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "ifconfig", "eth2", "up"],
					#background = False,
					#run_at_startup = False,
				)]
		), menu_conf_type.tc_menu(
			title = "Compara documentation",
			icon = "/home/matthieu/src/local/ebang-400dpi.png",
			items = [
				menu_conf_type.tc_item(
					name = "Protein-side schema",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/schema/diagrams/protein_schema.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "Genomic-side schema",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/schema/diagrams/genomic_schema.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "eHive schema",
					icon = None,
					command = "/home/matthieu/workspace/src/hive/master/docs/hive_schema.png",
					background = False,
					run_at_startup = False
				), None, menu_conf_type.tc_item(
					name = "Protein-tree pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/ProteinTrees.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "ncRNA-tree pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/ncRNAtrees.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "Family pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/Families.png",
					background = False,
					run_at_startup = False
				), None, menu_conf_type.tc_item(
					name = "Pairwise-aligner pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/Pairwise.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "EPO pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/epo_pt3.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "EPO-2X pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/EpoLowCoverage.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "Mercator-Pecan pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams/MercatorPecan.png",
					background = False,
					run_at_startup = False
				), menu_conf_type.tc_item(
					name = "Other pipelines",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/production/diagrams",
					background = False,
					run_at_startup = False
				), None, menu_conf_type.tc_item(
					name = "ensembl-compara checkout",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/",
					background = False,
					run_at_startup = False
				)]
		#), menu_conf_type.tc_menu(
			#title = "Daemons",
			#icon = "application-x-executable",
			#items = [
				#menu_conf_type.tc_item(
					#name = "gitit",
					#icon = None,
					#command = "/home/matthieu/gitit/gitit.sh",
					#background = True,
					#run_at_startup = False,
				#)]
		)]
)

