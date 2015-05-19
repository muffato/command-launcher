
import menu_conf_type

config = menu_conf_type.tc_menu(
	title = 'Useful commands',
	icon  = 'favorites',
	items = [
		menu_conf_type.tc_menu(
			title = 'Screen configuration',
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
				#), None, menu_conf_type.tc_item(
					#name = "Kill plymouth",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "plymouth", "quit"],
					#do_exec = False,
				#), menu_conf_type.tc_item(
					#name = "powersave",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "pm-powersave", "true"],
					#do_exec = False,
				#), menu_conf_type.tc_item(
					#name = "eth2 dowm",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "ifconfig", "eth2", "down"],
					#do_exec = False,
				#), menu_conf_type.tc_item(
					#name = "eth2 up",
					#icon = "network-wireless-100",
					#command = ["kdesudo", "ifconfig", "eth2", "up"],
					#do_exec = False,
				)]
		), menu_conf_type.tc_menu(
			title = "Compara documentation",
			icon = "/home/matthieu/src/local/ebang-400dpi.png",
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
				), None, menu_conf_type.tc_item(
					name = "Pairwise-aligner pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams/Pairwise.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "EPO pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams/epo_pt3.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "EPO-2X pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams/EpoLowCoverage.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "Mercator-Pecan pipeline",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams/MercatorPecan.png",
					do_exec = False
				), menu_conf_type.tc_item(
					name = "Other pipelines",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/pipelines/diagrams",
					do_exec = False
				), None, menu_conf_type.tc_item(
					name = "Species tree",
					icon = None,
					command = "/home/matthieu/workspace/src/ensembl/ensembl-compara/docs/species_tree/species_tree.pdf",
					do_exec = False
				)]
		#), menu_conf_type.tc_menu(
			#title = "Daemons",
			#icon = "application-x-executable",
			#items = [
				#menu_conf_type.tc_item(
					#name = "gitit",
					#icon = None,
					#command = "/home/matthieu/gitit/gitit.sh",
					#do_exec = 'tickbox'
				#)]
		)]
)

