import sys
import os


if len(sys.argv) == 1:
	print("usage: colorscheme [name of scheme]")
	exit(1)



# Scheme for i3blocks
colorschemes = {
	"gruvbox-dark": {
			"vim"			: "gruvbox8",
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
			"[seperator]\n"	: "#6272a4",
			"[ethernet]\n"	: "#bf616a",
			"[wifi]\n"		: "#50fa7b",
			"[cpu_temp]\n"	: "#8be9fd",
			"[cpu_usage]\n"	: "#9aedfe",
			"[ram]\n"		: "#ffb86c",
			"[volume]\n"	: "#bd93f9",
			"[battery]\n"	: "#ff79c6",
			"[time]\n"		: "#f1fa8c"

		}
}

scheme = sys.argv[1]
if scheme not in colorschemes:
	print(scheme, "is not a valid colorscheme name.")
	exit(1)


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
		print(line)
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

with open(file_path, "w") as w:
	w.writelines(data)

