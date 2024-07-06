def sort_file(input_file, output_file):
    with open(input_file) as i:
        with open(output_file, "w") as o:
            o.write("\n".join(sorted(i.read().splitlines())))

sort_file("input.txt", "output.txt")
print("Done")
# I know this file is a little useless but I wanted the file to be in alphabetical order and thought why not do it with a python script.