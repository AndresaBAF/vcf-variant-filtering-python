input_file = "data/example.vcf"
output_file = "data/filtered_variants.vcf"

min_qual = 30

with open(input_file, "r") as infile, open(output_file, "w") as outfile:

    for line in infile:

        if line.startswith("#"):
            outfile.write(line)
            continue

        fields = line.strip().split("\t")

        chrom = fields[0]
        position = fields[1]
        ref = fields[3]
        alt = fields[4]
        qual = fields[5]

        if qual != "." and float(qual) >= min_qual:
            outfile.write(line)

print("Filtering completed.")
