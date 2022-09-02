import docx

doc = docx.Document("Platoon_SOP.docx")

all_paras = doc.paragrapgs

for para in all_paras:
    print(para.text)
    print('-----------')

print('test')