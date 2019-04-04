import os

def filter_genes_from_raw():
    currentDirectory = os.curdir
    try:
        os.makedirs('./filtered-files')
        print("Successfully created directory 'filtered-files'")
    except FileExistsError:
        print("Directory 'filtered-files/' already exists. Proceeding.")
        pass
    count = 0
    for filename in os.listdir(os.curdir):
        if (filename.endswith(".maf.txt")):
            count+=1
            filter_relevant_genes(filename)
    print(f'{count} files  filtered.')

def filter_relevant_genes(maf_file):
    gene_list = []
    with open(maf_file) as file:
       content = file.readlines()
    total_count = len(content)
    for line in content:
       wordarray = line.split()
       if (wordarray[8] == "Missense_Mutation"):
           gene_list.append(wordarray[0])


    l1 = len(gene_list)
    print(f'now filtering {maf_file}. Total gene count: {total_count}. Filtered Gene count: {l1}')

    split_file_name_array = maf_file.split(".")
    new_file_name =  split_file_name_array[0] + ".non.txt"
    new_path = f'./filtered-files/{new_file_name}'
    with open(new_path, 'w') as file:
        for gene in gene_list:
            file.write(f'{gene}\n')


filter_genes_from_raw()