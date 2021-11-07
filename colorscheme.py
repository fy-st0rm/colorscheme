import sys
import os


if len(sys.argv) == 1:
	print("usage: colorscheme [name of scheme]")
	exit(1)



# Scheme for i3blocks
colorschemes = {
	"gruvbox-dark": {
			"vim"			: "gruvbox8",
			"lightline"		: "gruvbox",
			"[seperator]\n"	: "#458588",
			"[ethernet]\n"	: "#fb4934",
			"[wifi]\n"		: "#b8bb26",
			"[cpu_temp]\n"	: "#83a598",
			"[cpu_usage]\n"	: "#689d6a",
			"[ram]\n"		: "#ebdbb2",
			"[volume]\n"	: "#928374",
			"[battery]\n"	: "#98971a",
			"[time]\n"		: "#d79921"
		},
	"nord":			{
			"vim"			: "nord",
			"lightline"		: "nord",
			"[seperator]\n"	: "#68809a",
			"[ethernet]\n"	: "#bf616a",
			"[wifi]\n"		: "#a3be8c",
			"[cpu_temp]\n"	: "#81a1c1",
			"[cpu_usage]\n"	: "#8fbcbb",
			"[ram]\n"		: "#D8DEE9",
			"[volume]\n"	: "#b48ead",
			"[battery]\n"	: "#a3be8c",
			"[time]\n"		: "#ebcb8b"

		},
	"dracula":		{
			"vim"			: "dracula",
			"lightline"		: "dracula",
			"[seperator]\n"	: "#6272a4",
			"[ethernet]\n"	: "#bf616a",
			"[wifi]\n"		: "#5af78e",
			"[cpu_temp]\n"	: "#8be9fd",
			"[cpu_usage]\n"	: "#9aedfe",
			"[ram]\n"		: "#ffb86c",
			"[volume]\n"	: "#bd93f9",
			"[battery]\n"	: "#ff92d0",
			"[time]\n"		: "#f1fa8c"
		},
	"doom-one":		{
			"vim"			: "onedark",
			"lightline"		: "onedark",
			"[seperator]\n"	: "#6272a4",
			"[ethernet]\n"	: "#bf616a",
			"[wifi]\n"		: "#98be65",
			"[cpu_temp]\n"	: "#51afef",
			"[cpu_usage]\n"	: "#ecbe7b",
			"[ram]\n"		: "#da8548",
			"[volume]\n"	: "#bd93f9",
			"[battery]\n"	: "#da8548",
			"[time]\n"		: "#46d9ff"
		},
	"sdark":		{	
			"vim"			: "ghdark",
			"lightline"		: "ghdark",
			"[seperator]\n"	: "#555267",
			"[ethernet]\n"	: "#bf616a",
			"[wifi]\n"		: "#7ce38b",
			"[cpu_temp]\n"	: "#a2d2fb",
			"[cpu_usage]\n"	: "#ecbe7b",
			"[ram]\n"		: "#77bdfb",
			"[volume]\n"	: "#cea5fb",
			"[battery]\n"	: "#da8548",
			"[time]\n"		: "#c8c2e1"
		}
}

colorschemes_i3 = {
	"gruvbox-dark": {
			"set $pannel_bg": "#282828",
			"set $border"	: "#689d6a",
			"set $menu_nb"	: "#282828",
			"set $menu_nf"	: "#ebdbb2",
			"set $menu_sb"	: "#98971a",
			"set $menu_sf"	: "#282828"
		},
	"nord":			{	
			"set $pannel_bg": "#2e3440",
			"set $border"	: "#81a1c1",
			"set $menu_nb"	: "#282a36",
			"set $menu_nf"	: "#ffffff",
			"set $menu_sb"	: "#89cff0",
			"set $menu_sf"	: "#282a36"
		},
	"dracula":		{
			"set $pannel_bg": "#282a36",
			"set $border"	: "#bd93f9",
			"set $menu_nb"	: "#282a36",
			"set $menu_nf"	: "#ffffff",
			"set $menu_sb"	: "#bd93f9",
			"set $menu_sf"	: "#282a36"	
		},
	"doom-one":		{
			"set $pannel_bg": "#282c34",
			"set $border"	: "#81a1c1",
			"set $menu_nb"	: "#282c34",
			"set $menu_nf"	: "#ffffff",
			"set $menu_sb"	: "#51afef",
			"set $menu_sf"	: "#282a36"	
		},
	"sdark":		{
			"set $pannel_bg": "#030209",
			"set $border"	: "#555267",
			"set $menu_nb"	: "#030209",
			"set $menu_nf"	: "#ecf2f8",
			"set $menu_sb"	: "#555267",
			"set $menu_sf"	: "#ecf2f8"	
		}
}

scheme = sys.argv[1]
if scheme not in colorschemes:
	print(scheme, "is not a valid colorscheme name.")
	exit()


home_dir = os.path.expanduser("~")
#----
# Converting i3blocks
#---- 
file_path = f"{home_dir}/.config/i3blocks/config"

with open(file_path, "r") as r:
	data = r.readlines()


tokens = ["[seperator]\n", "[ethernet]\n", "[wifi]\n", "[cpu_temp]\n", "[cpu_usage]\n", "[ram]\n", "[volume]\n", "[battery]\n", "[time]\n"]
for no, line in enumerate(data):
	if line in tokens:
		color = colorschemes[scheme][line]
	if "color" in line:
		data[no] = f"color={color}\n"


with open(file_path, "w") as w:
	w.writelines(data)

#----
# Converting alacritty
#----
file_path = f"{home_dir}/.config/alacritty/alacritty.yml"

with open(file_path, "r") as r:
	data = r.readlines()

for no, line in enumerate(data):
	if "colors: *" in line:
		data[no] = f"colors: *{scheme}\n"

with open(file_path, "w") as w:
	w.writelines(data)

#----
# Converting vim
#----
file_path = f"{home_dir}/.vimrc"

with open(file_path, "r") as r:
	data = r.readlines()

for no, line in enumerate(data):
	if "colorscheme " in line:
		vim = colorschemes[scheme]["vim"]
		data[no] = f"colorscheme {vim}\n"
	elif "\'colorscheme\'" in line:
		lightline = colorschemes[scheme]["lightline"]
		data[no] = f"	\\ \'colorscheme\': \'{lightline}\',\n"

with open(file_path, "w") as w:
	w.writelines(data)

#----
# i3
#----
file_path = f"{home_dir}/.config/i3/config"

with open(file_path, "r") as r:
	data = r.readlines()

tokens = ["set $pannel_bg", "set $border", "set $menu_nb", "set $menu_nf", "set $menu_sb", "set $menu_sf"]
for no, line in enumerate(data):
	for i in tokens:
		if i in line:
			color = colorschemes_i3[scheme][i]
			data[no] = f"{i} {color}\n"

with open(file_path, "w") as w:
	w.writelines(data)

