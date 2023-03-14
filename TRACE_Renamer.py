import os
from PyPDF2 import PdfMerger

pdfs = ['Title Page.pdf',
        'Room Information.pdf',
        'System Information.pdf',
        'Project Information.pdf',
        'System Checksums.pdf',
        'Room Checksums.pdf',
        'Zone Checksums.pdf',
        'Load Airflow Summary.pdf',
        'Peak Cooling Load (Main System).pdf',
        'Peak Heating Load (Main System).pdf',
        'Bldg Env Clg Ld (Space Peak).pdf',
        'Bldg Env Htg Ld (Space Pk).pdf']

# test
# Initialize empty string
new_pdfs = []

# Rename files and add leading integers
count = 0
n = 1
for x in pdfs:
    num_str = str(n)
    fill_num = num_str.zfill(2)
    new_name = fill_num + ". " + pdfs[count]
    new_pdfs.append(new_name)
    # print(pdfs[count])
    try:
        my_file = open(pdfs[count])
        my_file.close()
        os.rename(pdfs[count], new_name)
    except IOError:
        # file didn't exist (or other issues)
        print(pdfs[count], "doesn't exist")
        pass

    count += 1
    n += 1

print("")
# Remove extenstions for bookmark names
marks = [os.path.splitext(x)[0] for x in new_pdfs]

file = PdfMerger(strict=False)
count = 0
for y in new_pdfs:
    file.merge(
        position=count,
        fileobj=new_pdfs[count],
        outline_item=marks[count]
    )
    print(marks[count])
    count += 1

print("")
print("Do not close window. Processing COMBINED PDF...")
file.write('COMBINED.pdf')
print("Complete!")
input("Press enter to exit;")
