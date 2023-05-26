import csv

def compare_user_ids(mrn_file, tli_file):
    mrn_user_ids = set()
    tli_user_ids = set()

    # Read MRN file and collect user IDs
    with open(mrn_file, 'r') as file1:
        reader1 = csv.DictReader(file1)
        for row in reader1:
            mrn_user_ids.add(row['User ID'])

    # Read TLI file user IDs
    with open(tli_file, 'r') as file2:
        reader2 = csv.DictReader(file2)
        for row in reader2:
            tli_user_ids.add(row['User ID'])

    # Check if all TLI user IDs are present in MRN file
    all_present = tli_user_ids.issubset(mrn_user_ids)

    # Check if any extra user IDs exist in TLI file
    extra_user_ids = tli_user_ids.difference(mrn_user_ids)

    return all_present, extra_user_ids

# Usage example
mrn_file_path = '/Users/betterhalf/Desktop/Niro automation/1Sample.csv'
tli_file_path = '/Users/betterhalf/Desktop/Niro automation/2Sample.csv'
all_present, extra_user_ids = compare_user_ids(mrn_file_path, tli_file_path)

if all_present:
    print("All user IDs in TLI file are present in MRN file.")
else:
    print("Some user IDs in TLI file are missing from MRN file.")

if extra_user_ids:
    print("Extra user IDs found in TLI file:")
    print(extra_user_ids)
else:
    print("No extra user IDs found in TLI file.")
