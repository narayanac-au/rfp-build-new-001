import docx2python

# Load the source file
source_doc = docx2python.docx2python(
    'C:/Users/shubhamjain35/Downloads/aspose_merge.docx')

# Create a new Word document
dest_doc = docx2python.create_new_docx()

# Copy all paragraphs and images from the source file to the destination file
for element in source_doc.body:
    if element['type'] == 'text':
        dest_doc.append(element['value'], style=element.get('style', ''))
    elif element['type'] == 'image':
        dest_doc.append(element['value'], element['width'], element['height'])

# Save the destination file
docx2python.python2docx(
    dest_doc.docx, 'C:/Users/shubhamjain35/Downloads/DFGH.docx')
