import sys
import os


if len(sys.argv) == 1:
	print("usage: colorscheme [name of scheme]")
	exit(1)



# Scheme for i3blocks
colorschemes = {
	"gruvbox-dark": {
			"[seperator]\n"	: "#458588",
			"[ethernet]\n"	: "#fb4934",
			"[wifi]\n"		: "#b8bb26",
			"[cpu_temp]\n"	: "#83a598",
			"[cpu_usage]\n"	: "#689d6a",
			"[ram]\n"		: "#ebdbb2",
			"[volume]\n"	: "#928374",
			"[battery]\n"	: "#98971a",
			"[time]\n"		: "#d79921"
		}
}

scheme = sys.argv[1]
if scheme not in colorschemes:
	print(scheme, "is not a valid colorscheme name.")
	exit(1)


#----
# Converting i3blocks
#---- 
home_dir = os.path.expanduser("~")
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
