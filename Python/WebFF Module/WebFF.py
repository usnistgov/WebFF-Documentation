#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: ascii -*-
# -*- coding: latin-1 -*-
'''
WebFF module: Contains functions that translate data between Excel, XML, and molecular dynamics text formats. 
'''
import xml.etree.ElementTree as ET 		  # Python standard library	
import xlrd                               # NEEDs to be installed

#
# ReadExcel Functions: Reads individual sheets from the WebFF Excel template and translate them into XML that fits the WebFF XML schema.
#

def ReadExcelMetaData_Header(sheet, sub_root): 
    ''' 
    Reads in the MetaData sheet from the WebFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    field5 = ET.SubElement(sub_root, "Force-Field-Schema-Version").text = xls_sheet.row_values(4)[1]    
    field1 = ET.SubElement(sub_root, "Force-Field-Protocol").text = xls_sheet.row_values(5)[1]
    field2 = ET.SubElement(sub_root, "Force-Field-Name").text = xls_sheet.row_values(6)[1]
    field1 = ET.SubElement(sub_root, "Description").text = xls_sheet.row_values(7)[1]
    field6 = ET.SubElement(sub_root, "Force-Field-Units").text = xls_sheet.row_values(8)[1]
    field3 = ET.SubElement(sub_root, "Data-Source")
    field4 = ET.SubElement(field3, "Compact")
    field1 = ET.SubElement(field4, "Reference").text = xls_sheet.row_values(9)[1]
    if (len(xls_sheet.row_values(9)[1]) != 0) :
        field2 = ET.SubElement(field4, "DOI").text = xls_sheet.row_values(10)[1]
    if (len(xls_sheet.row_values(9)[1]) != 0) :
        field1 = ET.SubElement(field4, "URL").text = xls_sheet.row_values(11)[1]
    if (len(xls_sheet.row_values(9)[1]) != 0) :
        field2 = ET.SubElement(field4, "Notes").text = xls_sheet.row_values(12)[1]
    field4 = ET.SubElement(sub_root, "Data-Source-Contact")
    field1 = ET.SubElement(field4, "Name").text = xls_sheet.row_values(13)[1]
    field1 = ET.SubElement(field4, "Affiliation").text = xls_sheet.row_values(14)[1]
    field2 = ET.SubElement(field4, "email").text = xls_sheet.row_values(15)[1]
    return



def ReadExcelMetaData_Keywords(sheet, root): 
    ''' 
    Reads in the Keywords sheet from the WebFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    sub_root = root.find("./Force-Field-Header")

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for col_num in xrange(0, xls_sheet.ncols):
        for row_num , cell_value in enumerate(xls_sheet.col_values(col_num)[5:]):
            if (len(str(cell_value))!=0 and str(cell_value) != "?") :
                ET.SubElement(sub_root, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelMetaData_References(sheet, root): 
    ''' 
    Reads in the Keywords sheet from the WebFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    sub_root = root.find("./Force-Field-Header")

    sheet = ET.SubElement(sub_root, "Additional-References")
	  
    # Row 2 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(2))
	
    for row_num in xrange(3, xls_sheet.nrows):
        cur_entry = ET.SubElement(sheet, "Compact")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)): 
            if (len(xls_sheet.row_values(row_num)[col_num]))!=0 :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = xls_sheet.row_values(row_num)[col_num]
    return



def ReadExcelBondPotential_Harmonic(sheet, sub_root): 
    ''' 
    Reads in the BondPotential-Harmonic sheet from the WebFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Harmonic", {'style':AA, 'formula':BB, 'K-units':CC, 'R0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelBondPotential_FENE(sheet, sub_root): 
    ''' 
    Reads in the BondPotential-FENE sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-FENE", {'style':AA, 'formula':BB, 'K-units':CC, 'R0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelBondPotential_Quartic(sheet, sub_root): 
    ''' 
    Reads in the BondPotential-Quartic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Quartic", {'style':AA, 'formula':BB, 'K-units':CC, 'R0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelBondPotential_Morse(sheet, sub_root): 
    '''
    Reads in the BondPotential-Morse sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Morse", {'style':AA, 'formula':BB, 'D-units':CC, 'A-units':DD, 'R0-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))
    for row_num in xrange(9, xls_sheet.nrows):

        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelAnglePotential_Harmonic(sheet, sub_root): 
    ''' 
    Reads in the AnglePotential-Harmonic sheet from the WebFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-Harmonic", {'style':AA, 'formula':BB, 'Ka-units':CC, 'Theta0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4: 
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return



def ReadExcelAnglePotential_COS2(sheet, sub_root): 
    ''' 
    Reads in the AnglePotential-COS2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-COS2", {'style':AA, 'formula':BB, 'Ka-units':CC, 'Theta0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4: 
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelAnglePotential_Cosine(sheet, sub_root): 
    '''
    Reads in the AnglePotential-Cosine sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-Cosine", {'style':AA, 'formula':BB, 'Ka-units':CC})

    # Row 6 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(6))

    attribute_idx1 = xls_sheet_header.index("precedence")
    attribute_idx2 = xls_sheet_header.index("comment")
    attribute_idx3 = xls_sheet_header.index("version")
    attribute_idx4 = xls_sheet_header.index("reference")

    for row_num in xrange(7, xls_sheet.nrows):
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str(int(xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4: 
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return



def ReadExcelAnglePotential_CHARMM(sheet, sub_root): 
    '''
    Reads in the AnglePotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]
    FF=xls_sheet.row_values(7)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-CHARMM", {'style':AA, 'formula':BB, 'Ka-units':CC, 'Theta0-units':DD, 'Kub-units':EE, 
                                                           'Rub-units':FF})

    # Row 9 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(9))

    for row_num in xrange(10, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4: 
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelDihedralPotential_CHARMM(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-CHARMM", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD, 'Phi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        force_integer_idx1 = xls_sheet_header.index("N")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) :
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) :
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) :
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                else:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelDihedralPotential_Harmonic(sheet,sub_root): 
    '''
    Reads in the DihedralPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Harmonic", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        force_integer_idx1 = xls_sheet_header.index("Ns")
        force_integer_idx2 = xls_sheet_header.index("N")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                elif col_num == force_integer_idx2:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                else:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelDihedralPotential_Quadratic(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-Quadratic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Quadratic", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD, 'Phi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelDihedralPotential_OPLS(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-OPLS sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-OPLS", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelDihedralPotential_FourierSimple(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-FourierSimple sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-FourierSimple", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return



def ReadExcelDihedralPotential_Fourier(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-Fourier sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Fourier", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD, 'Dn-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        force_integer_idx1 = xls_sheet_header.index("N1")
        force_integer_idx2 = xls_sheet_header.index("N2")
        force_integer_idx3 = xls_sheet_header.index("N3")
        force_integer_idx4 = xls_sheet_header.index("N4")
        force_integer_idx5 = xls_sheet_header.index("N5")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                elif col_num == force_integer_idx2:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                elif col_num == force_integer_idx3:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                elif col_num == force_integer_idx4:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                elif col_num == force_integer_idx5:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                else:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelDihedralPotential_Multiharmonic(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-Multiharmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Multiharmonic", {'style':AA, 'formula':BB, 'convention':CC, 'An-units':DD})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)            
    return



def ReadExcelImproperPotential_CVFF(sheet, sub_root): 
    '''
    Reads in the ImproperPotential-CVFF sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-CVFF", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        force_integer_idx1 = xls_sheet_header.index("Ns")
        force_integer_idx2 = xls_sheet_header.index("N")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                elif col_num == force_integer_idx2:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                else:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelImproperPotential_COS2(sheet, sub_root): 
    '''
    Reads in the ImporperPotential-COS2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-COS2", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'Chi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelImproperPotential_Harmonic(sheet, sub_root): 
    '''
    Reads in the ImporperPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Harmonic", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'Chi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelImproperPotential_Fourier(sheet, sub_root): 
    '''
    Reads in the ImporperPotential-Fourier sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Fourier", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelImproperPotential_Umbrella(sheet, sub_root): 
    '''
    Reads in the ImporperPotential-Umbrella sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Umbrella", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'w0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelImproperPotential_CHARMM(sheet, sub_root): 
    ''' 
    Reads in the ImporperPotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-CHARMM", {'style':AA, 'formula':BB, 'convention':CC, 'Kd-units':DD, 'Phi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        force_integer_idx1 = xls_sheet_header.index("N")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
                else:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_LJ(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJ sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_LJRmin(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJRmin sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ-Rmin", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'Rmin-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelNonBondPotential_LJAB(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJAB sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ-AB", {'style':AA, 'formula':BB, 'A-units':CC, 'B-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_LJ2AB(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJ2AB sheet from the WebFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ2-AB", {'style':AA, 'formula':BB, 'A-units':CC, 'B-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_LJ96 (sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJRmin sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ96", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue 
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_LJ962 (sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJ962 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ962", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue 
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_LJ2(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJ2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    ''' 
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ2", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_WCA(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-WCA sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-Weeks-Chandler-Anderson", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_Mie(sheet, sub_root):
    '''
    Reads in the NonBondPotential-Mie sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-Mie", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_EnergyRenorm (sheet, sub_root): 
    '''
    Reads in the NonBondPotential-EnergyRenorm sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-EnergyRenorm", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'T_sig-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue 
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelNonBondPotential_LJGROMACS(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJ-GROMACS sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-LJ-GROMACS", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'sigma-units':DD, 'r-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue 
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



def ReadExcelDissipativePotential_Langevin(sheet, sub_root): 
    '''
    Reads in the DissipativePotential-Langevin sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]

    sheet = ET.SubElement(sub_root, "DissipativePotential-Langevin", {'style':AA, 'formula':BB, 'gamma-units':CC})

    # Row 6 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(6))

    for row_num in xrange(7, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dissipative")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return


#
# SECTION: Soft Potentials
#

def ReadExcelSoftPotential_DPD(sheet, sub_root): 
    '''
    Reads in the SoftPotential-DPD sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "SoftPotential-DPD", {'style':AA, 'formula':BB, 'a_ij-units':CC, 'gamma-units':DD, 'r_c-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Soft")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelSoftPotential_SRP(sheet, sub_root): 
    '''
    Reads in the SoftPotential-SRP sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "SoftPotential-SRP", {'style':AA, 'formula':BB, 'c_ij-units':CC, 'r_c-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Soft")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelEquivalenceTable(sheet, sub_root): 
    '''
    Reads in the Equivalence-Table sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "Equivalence")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)   
    return




def ReadExcelAutoEquivalenceTable(sheet, sub_root): 
    '''
    Reads in the Equivalence-Table sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "AutoEquivalence")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)  
    return




def ReadExcelBondIncrements(sheet, sub_root): 
    '''
    Reads in the Bond-Increments sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "BondIncrement")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypes(sheet,root): 
    '''
    Reads in the Atom-Types sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]

    sheet = ET.SubElement(root, "AtomTypes", {'PatternNomenclatureStyle':AA, 'comment':BB}) 
    # Row 5 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(5))

    for row_num in xrange(6, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("Element")
        attribute_idx2 = xls_sheet_header.index("AtomicNumber")
        attribute_idx3 = xls_sheet_header.index("AtomicMass")
        attribute_idx4 = xls_sheet_header.index("Description")
        cur_entry = ET.SubElement(sheet, "AtomType")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'Element', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'AtomicNumber', str(int((xls_sheet.row_values(row_num)[attribute_idx2]))))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'AtomicMass', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'Description', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypes_ATDL(sheet,root): 
    '''
    Reads in the AtomTypes-ATDL sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    funko = ET.SubElement(root, "AtomTypes")

    AA=xls_sheet.row_values(2)[1]
    if (len(xls_sheet.row_values(3)[1]) != 0) :
        BB=xls_sheet.row_values(3)[1]
        sheet = ET.SubElement(funko, "AtomType-ATDL", {'Nomenclature':AA, 'comment':BB})
    else :
        sheet = ET.SubElement(funko, "AtomType-ATDL", {'Nomenclature':AA})
    
    # Row 5 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(5))

    attribute_idx1 = xls_sheet_header.index("Element")
    attribute_idx2 = xls_sheet_header.index("AtomicNumber")
    attribute_idx3 = xls_sheet_header.index("AtomicMass")
    attribute_idx4 = xls_sheet_header.index("Description")

    for row_num in xrange(6, xls_sheet.nrows):
        cur_entry = ET.SubElement(sheet, "AtomType")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'Element', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'AtomicNumber', str(int((xls_sheet.row_values(row_num)[attribute_idx2]))))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'AtomicMass', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'Description', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypes_DFF(sheet,root): 
    '''
    Reads in the AtomTypes-DFF sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    funko = ET.SubElement(root, "AtomTypes")

    AA=xls_sheet.row_values(2)[1]
    if (len(xls_sheet.row_values(3)[1]) != 0) :
        BB=xls_sheet.row_values(3)[1]
        sheet = ET.SubElement(funko, "AtomType-DFF", {'Nomenclature':AA, 'comment':BB})
    else :
        sheet = ET.SubElement(funko, "AtomType-DFF", {'Nomenclature':AA})
    
    # Row 5 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(5))

    attribute_idx1 = xls_sheet_header.index("Element")
    attribute_idx2 = xls_sheet_header.index("AtomicNumber")
    attribute_idx3 = xls_sheet_header.index("AtomicMass")
    attribute_idx4 = xls_sheet_header.index("Description")

    for row_num in xrange(6, xls_sheet.nrows):
        cur_entry = ET.SubElement(sheet, "AtomType")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'Element', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'AtomicNumber', str(int((xls_sheet.row_values(row_num)[attribute_idx2]))))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'AtomicMass', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'Description', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypes_Generic(sheet,root): 
    '''
    Reads in the AtomTypes-Generic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    funko = ET.SubElement(root, "AtomTypes")

    AA=xls_sheet.row_values(2)[1]
    if (len(xls_sheet.row_values(3)[1]) != 0) :
        BB=xls_sheet.row_values(3)[1]
        sheet = ET.SubElement(funko, "AtomType-Generic", {'Nomenclature':AA, 'comment':BB})
    else :
        sheet = ET.SubElement(funko, "AtomType-Generic", {'Nomenclature':AA})
    
    # Row 5 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(5))

    attribute_idx1 = xls_sheet_header.index("Element")
    attribute_idx2 = xls_sheet_header.index("AtomicNumber")
    attribute_idx3 = xls_sheet_header.index("AtomicMass")
    attribute_idx4 = xls_sheet_header.index("Description")

    for row_num in xrange(6, xls_sheet.nrows):
        cur_entry = ET.SubElement(sheet, "AtomType")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'Element', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'AtomicNumber', str(int((xls_sheet.row_values(row_num)[attribute_idx2]))))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'AtomicMass', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'Description', str((xls_sheet.row_values(row_num)[attribute_idx4])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                elif col_num == attribute_idx4:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypes_CoarseGrained(sheet,root): 
    '''
    Reads in the AtomTypes-ATDL sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]

    funko = ET.SubElement(root, "AtomTypes")
    sheet = ET.SubElement(funko, "AtomType-CoarseGrained", {'Nomenclature':AA, 'comment':BB}) 
    # Row 5 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(5))

    attribute_idx1 = xls_sheet_header.index("Description")
    attribute_idx2 = xls_sheet_header.index("AtomicMass-CG")
    attribute_idx3 = xls_sheet_header.index("AtomicSize-CG")

    for row_num in xrange(6, xls_sheet.nrows):
        cur_entry = ET.SubElement(sheet, "CGType")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'Description', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'AtomicMass-CG', str(int((xls_sheet.row_values(row_num)[attribute_idx2]))))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'AtomicSize-CG', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypeAttributes(sheet,root): 
    '''
    Reads in the Atom-Types-Attributes sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet1 = sheet

    # Row 4 is the header
    xls_sheet1_header = map(str, xls_sheet1.row_values(4))
    for row_num in xrange(5, xls_sheet1.nrows):
        attribute_idx1 = xls_sheet1_header.index("AtomType-Name")
        for child in root.findall("./AtomTypes/AtomType"): 
            AtomTypeName = (child.find("AtomType-Name"))
            if(AtomTypeName.text == str(xls_sheet1.cell_value(row_num, 0))): 
                # Check if there is already an attribute to avoid creating incorrect duplicate attribute elements 
                if(child.find("Atom-Attributes") == None) :
                    sheet1 = ET.SubElement(child, "Atom-Attributes")
                    sheet2 = ET.SubElement(sheet1, "Attribute")
                else :
                    sheet2 = ET.SubElement(child.find("Atom-Attributes"), "Attribute")
                    for col_num, cell_value in enumerate(xls_sheet1.row_values(row_num)):
                        if (len(str(cell_value))!=0) :
                            if col_num == attribute_idx1:
                                continue    
                            if(type(cell_value) == float): 
                                ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(int(cell_value)) 
                        else:
                            ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypeAttributes_Generic(sheet,root): 
    '''
    Reads in the Atom-Attributes-Generic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet1 = sheet

    # Row 4 is the header
    xls_sheet1_header = map(str, xls_sheet1.row_values(4))
    attribute_idx1 = xls_sheet1_header.index("AtomType-Name")
    for row_num in xrange(5, xls_sheet1.nrows):
        for child in root.findall("./AtomTypes/AtomType-Generic/AtomType"): 
            AtomTypeName = (child.find("AtomType-Name"))
            if(AtomTypeName.text == str(xls_sheet1.cell_value(row_num, 0))): 
                # Check if there is already an attribute to avoid creating incorrect duplicate attribute elements 
                if(child.find("Atom-Attributes") == None) :
                    sheet1 = ET.SubElement(child, "Atom-Attributes")
                    sheet2 = ET.SubElement(sheet1, "Attribute")
                else :
                    sheet2 = ET.SubElement(child.find("Atom-Attributes"), "Attribute")
                    for col_num, cell_value in enumerate(xls_sheet1.row_values(row_num)):
                        if (len(str(cell_value))!=0) :
                            if col_num == attribute_idx1:
                                continue
                            if col_num == 5:
                                ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(cell_value)
                            elif(type(cell_value) == float): 
                                ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(int(cell_value))
                            else:
                                ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(cell_value)
    return




def ReadExcelAtomTypeAttributes_DFF(sheet,root): 
    '''
    Reads in the Atom-Attributes-DFF sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet1 = sheet

    # Row 4 is the header
    xls_sheet1_header = map(str, xls_sheet1.row_values(4))
    attribute_idx1 = xls_sheet1_header.index("AtomType-Name")
    for row_num in xrange(5, xls_sheet1.nrows):
        for child in root.findall("./AtomTypes/AtomType-DFF/AtomType"): 
            AtomTypeName = (child.find("AtomType-Name"))
            if(AtomTypeName.text == str(xls_sheet1.cell_value(row_num, 0))):
                # Check if there is already an attribute to avoid creating incorrect duplicate attribute elements 
                if(child.find("Atom-Attributes") == None) :
                    sheet1 = ET.SubElement(child, "Atom-Attributes")
                    sheet2 = ET.SubElement(sheet1, "Attribute")
                else :
                    sheet2 = ET.SubElement(child.find("Atom-Attributes"), "Attribute")
                    for col_num, cell_value in enumerate(xls_sheet1.row_values(row_num)):
                        if (len(str(cell_value))!=0) :
                            if col_num == attribute_idx1:
                                continue    
                            if col_num == 5:
                                ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(cell_value)
                            elif(type(cell_value) == float): 
                                ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(int(cell_value))
                            else:
                                ET.SubElement(sheet2, xls_sheet1_header[col_num]).text = str(cell_value)
    return




def ReadExcelRelationTree_DFF(sheet,root): 
    '''
    Reads in the RelationTree-DFF sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet
    RT=xls_sheet.row_values(4)[1]
    if (len(str(RT))!=0) :
        temp = root.find("./AtomTypes/AtomType-DFF")
        ET.SubElement(temp, "DFFRelationTree").text = str(RT)
    return




#
# Class2 functions
#

def ReadExcelBondPotential_Class2(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Class2", {'style':AA, 'formula':BB, 'K-units':CC, 'R0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        #cur_entry = ET.SubElement(sheet, "Bond", comment=str((xls_sheet.row_values(row_num)[attribute_idx1])),
        #                          version=str(xls_sheet.row_values(row_num)[attribute_idx2]),
        #                          reference=str(xls_sheet.row_values(row_num)[attribute_idx3]))
        cur_entry = ET.SubElement(sheet, "Bond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelAnglePotential_Class2(sheet, sub_root): 
    '''
    Reads in the AnglePotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-Class2", {'style':AA, 'formula':BB, 'K-units':CC, 'Theta0-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("precedence")
        attribute_idx2 = xls_sheet_header.index("comment")
        attribute_idx3 = xls_sheet_header.index("version")
        attribute_idx4 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Angle")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'precedence', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        if (xls_sheet.cell_value(row_num, attribute_idx4)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            elif col_num == attribute_idx4: 
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelDihedralPotential_Class2(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-CHARMM sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Class2", {'style':AA, 'formula':BB, 'convention':CC, 'Kn-units':DD, 'Phin-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelImproperPotential_Class2(sheet, sub_root):
    '''
    Reads in the ImporperPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "ImproperPotential-Class2", {'style':AA, 'formula':BB, 'convention':CC, 'Ki-units':DD, 'Chi0-units':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Improper")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_BondBond(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-BondBond", {'style':AA, 'formula':BB, 'M-units':CC, 'Ri-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_BondBond13(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-BondBond13", {'style':AA, 'formula':BB, 'N-units':CC, 'Ri-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_AngleAngle(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-AngleAngle", {'style':AA, 'formula':BB, 'M-units':CC, 'Theta-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_BondAngle(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-BondAngle", {'style':AA, 'formula':BB, 'N-units':CC, 'Ri-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_MiddleBondTorsion(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-MiddleBondTorsion", {'style':AA, 'formula':BB, 'A-units':CC, 'R-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_EndBondTorsion(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-EndBondTorsion", {'style':AA, 'formula':BB, 'B-units':CC, 'C-units':DD, 'R-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_AngleTorsion(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-AngleTorsion", {'style':AA, 'formula':BB, 'D-units':CC, 'E-units':DD, 'Theta-units':EE})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_AngleAngleTorsion(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-AngleAngleTorsion", {'style':AA, 'formula':BB, 'M-units':CC, 'Theta-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelCrossPotential_AngleAngleTorsion(sheet, sub_root): 
    '''
    Reads in the BondPotential-Harmonic sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "CrossPotential-AngleAngleTorsion", {'style':AA, 'formula':BB, 'M-units':CC, 'Theta-units':DD})

    # Row 7 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(7))

    for row_num in xrange(8, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sheet, "Cross")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if col_num == attribute_idx1:
                continue 
            elif col_num == attribute_idx2:
                continue
            elif col_num == attribute_idx3:
                continue
            ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value) 
    return




def ReadExcelNonBondPotential_LJClass2(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-LJClass2 sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-Class2", {'style':AA, 'formula':BB, 'epsilon-units':CC, 'Rmin-units':DD, 'Combining-Rule':EE})

    # Row 8 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(8))

    for row_num in xrange(9, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference") 
        cur_entry = ET.SubElement(sheet, "NonBond")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return



#
# Coarse-grained potentials (Tabular form)
#

def ReadExcelBondPotential_Tabular(sheet, sub_root): 
    '''
    Reads in the BondPotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "BondPotential-Tabular", {'style':AA, 'bond-length-units':BB, 'energy-units':CC, 'force-units':DD})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(7)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(8)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    EE=xls_sheet.row_values(11)[1]
    FF=xls_sheet.row_values(12)[1]
    GG=str(xls_sheet.row_values(13)[1])
    HH=str(int(xls_sheet.row_values(14)[1]))

    ET.SubElement(sheet, "AT-1").text = EE
    ET.SubElement(sheet, "AT-2").text = FF
    ET.SubElement(sheet, "keyword").text = GG
    ET.SubElement(sheet, "N").text = HH

    # Handling optional data
    if (xls_sheet.row_values(15)[1]) :
        ET.SubElement(sheet, "fplo").text = str(xls_sheet.row_values(15)[1])
    if (xls_sheet.row_values(16)[1]) :
        ET.SubElement(sheet, "fphi").text = str(xls_sheet.row_values(16)[1])
    if (xls_sheet.row_values(17)[1]) :
        ET.SubElement(sheet, "EQ").text = str(xls_sheet.row_values(17)[1])

    # Row 19 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(19))

    for row_num in xrange(20, xls_sheet.nrows):
        force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "Bond")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
            else :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAnglePotential_Tabular(sheet, sub_root): 
    '''
    Reads in the AnglePotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "AnglePotential-Tabular", {'style':AA, 'angle-units':BB, 'energy-units':CC, 'energy-diff-units':DD})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(7)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(8)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    EE=xls_sheet.row_values(11)[1]
    FF=xls_sheet.row_values(12)[1]
    GG=xls_sheet.row_values(13)[1]
    HH=str(xls_sheet.row_values(14)[1])
    II=str(int(xls_sheet.row_values(15)[1]))

    ET.SubElement(sheet, "AT-1").text = EE
    ET.SubElement(sheet, "AT-2").text = FF
    ET.SubElement(sheet, "AT-3").text = GG
    ET.SubElement(sheet, "keyword").text = HH
    ET.SubElement(sheet, "N").text = II

    # Handling optional data
    if (xls_sheet.row_values(16)[1]) :
        ET.SubElement(sheet, "fplo").text = str(xls_sheet.row_values(16)[1])
    if (xls_sheet.row_values(17)[1]) :
        ET.SubElement(sheet, "fphi").text = str(xls_sheet.row_values(17)[1])
    if (xls_sheet.row_values(18)[1]) :
        ET.SubElement(sheet, "EQ").text = str(xls_sheet.row_values(18)[1])

    # Row 20 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(20))

    for row_num in xrange(21, xls_sheet.nrows):
        force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "Angle")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
            else :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelDihedralPotential_Tabular(sheet, sub_root): 
    '''
    Reads in the DihedralPotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]

    sheet = ET.SubElement(sub_root, "DihedralPotential-Tabular", {'style':AA, 'angle-units':BB, 'energy-units':CC, 'energy-diff-units':DD})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(7)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(8)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    EE=xls_sheet.row_values(11)[1]
    FF=xls_sheet.row_values(12)[1]
    GG=xls_sheet.row_values(13)[1]
    HH=xls_sheet.row_values(14)[1]
    II=str(xls_sheet.row_values(15)[1])
    JJ=str(int(xls_sheet.row_values(16)[1]))

    ET.SubElement(sheet, "AT-1").text = EE
    ET.SubElement(sheet, "AT-2").text = FF
    ET.SubElement(sheet, "AT-3").text = GG
    ET.SubElement(sheet, "AT-4").text = HH
    ET.SubElement(sheet, "keyword").text = II
    ET.SubElement(sheet, "N").text = JJ

    # Handling optional data
    if (xls_sheet.row_values(17)[1]) :
        ET.SubElement(sheet, "NOF").text = str(xls_sheet.row_values(17)[1])
    if (xls_sheet.row_values(18)[1]) :
        ET.SubElement(sheet, "CHECKU").text = str(xls_sheet.row_values(18)[1])
    if (xls_sheet.row_values(19)[1]) :
        ET.SubElement(sheet, "CHECKF").text = str(xls_sheet.row_values(19)[1])

    # Row 21 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(21))

    for row_num in xrange(22, xls_sheet.nrows):
        force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "Dihedral")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
            else :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelNonBondPotential_Tabular(sheet, sub_root): 
    '''
    Reads in the NonBondPotential-Tabular sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Handling attributes
    AA=xls_sheet.row_values(2)[1]
    BB=xls_sheet.row_values(3)[1]
    CC=xls_sheet.row_values(4)[1]
    DD=xls_sheet.row_values(5)[1]
    EE=xls_sheet.row_values(6)[1]

    sheet = ET.SubElement(sub_root, "NonBondPotential-Tabular", {'style':AA, 'Interpolation-style':BB, 'r-units':CC, 'energy-units':DD, 'force-units':EE})

    # Handling comments, version, and reference
    if (xls_sheet.row_values(8)[1]) :
        ET.Element.set(sheet, 'comment', str(xls_sheet.row_values(7)[1]))
    if (xls_sheet.row_values(9)[1]) : 
        ET.Element.set(sheet, 'version', str(xls_sheet.row_values(8)[1]))
    if (xls_sheet.row_values(10)[1]) : 
        ET.Element.set(sheet, 'reference', str(xls_sheet.row_values(9)[1]))

    # Handling required data
    FF=xls_sheet.row_values(12)[1]
    GG=xls_sheet.row_values(13)[1]
    HH=xls_sheet.row_values(14)[1]
    II=str(int(xls_sheet.row_values(15)[1]))

    ET.SubElement(sheet, "AT-1").text = FF
    ET.SubElement(sheet, "AT-2").text = GG
    ET.SubElement(sheet, "keyword").text = HH
    ET.SubElement(sheet, "N").text = II

    # Handling optional data
    if (xls_sheet.row_values(16)[1]) :
        ET.SubElement(sheet, "rlo").text = str(xls_sheet.row_values(16)[1])
    if (xls_sheet.row_values(17)[1]) :
        ET.SubElement(sheet, "rhi").text = str(xls_sheet.row_values(17)[1])
    if (xls_sheet.row_values(18)[1]) :
        ET.SubElement(sheet, "fplo").text = str(xls_sheet.row_values(18)[1])
    if (xls_sheet.row_values(19)[1]) :
        ET.SubElement(sheet, "fphi").text = str(xls_sheet.row_values(19)[1])

    # Row 21 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(21))

    for row_num in xrange(22, xls_sheet.nrows):
        force_integer_idx1 = xls_sheet_header.index("index")
        cur_entry = ET.SubElement(sheet, "NonBond")
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == force_integer_idx1:
                    ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(int(cell_value))
            else :
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
    return




def ReadExcelAutoEquivalenceTable(sheet, sub_root): 
    '''
    Reads in the Equivalence-Table sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''   
    xls_sheet = sheet

    # Row 4 is the header
    xls_sheet_header = map(str, xls_sheet.row_values(4))

    for row_num in xrange(5, xls_sheet.nrows):
        attribute_idx1 = xls_sheet_header.index("comment")
        attribute_idx2 = xls_sheet_header.index("version")
        attribute_idx3 = xls_sheet_header.index("reference")
        cur_entry = ET.SubElement(sub_root, "AutoEquivalence")
        if (xls_sheet.cell_value(row_num, attribute_idx1)) : 
            ET.Element.set(cur_entry, 'comment', str((xls_sheet.row_values(row_num)[attribute_idx1])))
        if (xls_sheet.cell_value(row_num, attribute_idx2)) : 
            ET.Element.set(cur_entry, 'version', str((xls_sheet.row_values(row_num)[attribute_idx2])))
        if (xls_sheet.cell_value(row_num, attribute_idx3)) : 
            ET.Element.set(cur_entry, 'reference', str((xls_sheet.row_values(row_num)[attribute_idx3])))
        for col_num, cell_value in enumerate(xls_sheet.row_values(row_num)):
            if (len(str(cell_value))!=0) :
                if col_num == attribute_idx1:
                    continue 
                elif col_num == attribute_idx2:
                    continue
                elif col_num == attribute_idx3:
                    continue
                ET.SubElement(cur_entry, xls_sheet_header[col_num]).text = str(cell_value)
   
#
# Water Model functions
#
                
def ReadExcelWaterPotential_3Site(sheet, sub_root): 
    '''
    Reads in the WaterPotential-3Site sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Description attributes:

    AA=xls_sheet.row_values(2)[1] # name
    BB=xls_sheet.row_values(3)[1] # formula
    CC=xls_sheet.row_values(4)[1] # version
    DD=xls_sheet.row_values(5)[1] # comment
    EE=xls_sheet.row_values(6)[1] # R_OH-units
    FF=xls_sheet.row_values(7)[1] # Theta_HOH-units
    GG=xls_sheet.row_values(8)[1] # A-units
    HH=xls_sheet.row_values(9)[1] # B-units
    II=xls_sheet.row_values(10)[1] # sigma-units
    JJ=xls_sheet.row_values(11)[1] # epsilon-units

    sheet = ET.SubElement(sub_root, "WaterModel-3Site-Rigid", {'name':AA, 'formula':BB, 'version':CC, 'comment':DD, 'R_OH-units':EE, 'Theta_HOH-units':FF, 'A-units':GG, 'B-units':HH, 'sigma-units':II, 'epsilon-units':JJ})

    # Data elements

    AA=str(xls_sheet.row_values(14)[0]) # R_OH
    ET.SubElement(sub_root, "R_OH").text = AA
    BB=str(xls_sheet.row_values(14)[1]) # Theta_HOH
    ET.SubElement(sub_root, "Theta_HOH").text = BB
    CC=str(xls_sheet.row_values(14)[2]) # A
    ET.SubElement(sub_root, "A").text = CC
    DD=str(xls_sheet.row_values(14)[3]) # B
    ET.SubElement(sub_root, "B").text = DD
    EE=str(xls_sheet.row_values(14)[4]) # q_O
    ET.SubElement(sub_root, "q_O").text = EE
    FF=str(xls_sheet.row_values(14)[5]) # q_H
    ET.SubElement(sub_root, "q_H").text = FF
    if len(str(xls_sheet.row_values(14)[6])) != 0: # EnergyDispersion
        GG=str(xls_sheet.row_values(14)[6])
        ET.SubElement(sub_root, "EnergyDispersion").text = GG
    if len(str(xls_sheet.row_values(14)[7])) != 0: # sigma
        HH=str(xls_sheet.row_values(14)[7])
        ET.SubElement(sub_root, "sigma").text = HH
    if len(str(xls_sheet.row_values(14)[8])) != 0: # epsilon
        II=str(xls_sheet.row_values(14)[8])
        ET.SubElement(sub_root, "epsilon").text = II
    return



def ReadExcelWaterPotential_4Site(sheet, sub_root): 
    '''
    Reads in the WaterPotential-4Site sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Description attributes:

    AA=xls_sheet.row_values(2)[1] # name
    BB=xls_sheet.row_values(3)[1] # formula
    CC=xls_sheet.row_values(4)[1] # version
    DD=xls_sheet.row_values(5)[1] # comment
    EE=xls_sheet.row_values(6)[1] # A-units
    FF=xls_sheet.row_values(7)[1] # B-units
    GG=xls_sheet.row_values(8)[1] # R-units
    HH=xls_sheet.row_values(9)[1] # Theta_HOH-units
    II=xls_sheet.row_values(10)[1] # sigma-units
    JJ=xls_sheet.row_values(11)[1] # epsilon-units

    sheet = ET.SubElement(sub_root, "WaterModel-4Site-Rigid", {'name':AA, 'formula':BB, 'version':CC, 'comment':DD, 'A-units':EE, 'B-units':FF, 'R-units':GG, 'Theta_HOH-units':HH, 'sigma-units':II, 'epsilon-units':JJ})

    # Data elements

    AA=str(xls_sheet.row_values(14)[0]) # R_OH
    ET.SubElement(sub_root, "R_OH").text = AA
    BB=str(xls_sheet.row_values(14)[1]) # R_OM
    ET.SubElement(sub_root, "R_OM").text = BB
    CC=str(xls_sheet.row_values(14)[2]) # Theta_HOH
    ET.SubElement(sub_root, "Theta_HOH").text = CC
    DD=str(xls_sheet.row_values(14)[3]) # A
    ET.SubElement(sub_root, "A").text = DD
    EE=str(xls_sheet.row_values(14)[4]) # B
    ET.SubElement(sub_root, "B").text = EE
    FF=str(xls_sheet.row_values(14)[5]) # q_M
    ET.SubElement(sub_root, "q_M").text = FF
    GG=str(xls_sheet.row_values(14)[6]) # q_H
    ET.SubElement(sub_root, "q_H").text = GG
    if len(str(xls_sheet.row_values(14)[7])) != 0: # sigma
        HH=str(xls_sheet.row_values(14)[7])
        ET.SubElement(sub_root, "sigma").text = HH
    if len(str(xls_sheet.row_values(14)[8])) != 0: # epsilon
        II=str(xls_sheet.row_values(14)[8])
        ET.SubElement(sub_root, "epsilon").text = II
    return




def ReadExcelWaterPotential_5Site(sheet, sub_root):
    '''
    Reads in the WaterPotential-5Site sheet from the webFF excel template. 
    Arguments are the sheet and the XML element that is the parent for the data.
    '''
    xls_sheet = sheet

    # Description attributes:

    AA=xls_sheet.row_values(2)[1] # name
    BB=xls_sheet.row_values(3)[1] # formula
    CC=xls_sheet.row_values(4)[1] # version
    DD=xls_sheet.row_values(5)[1] # comment
    EE=xls_sheet.row_values(6)[1] # A-units
    FF=xls_sheet.row_values(7)[1] # B-units
    GG=xls_sheet.row_values(8)[1] # R-units
    HH=xls_sheet.row_values(9)[1] # Theta-units
    II=xls_sheet.row_values(10)[1] # sigma-units
    JJ=xls_sheet.row_values(11)[1] # epsilon-units

    sheet = ET.SubElement(sub_root, "WaterModel-5Site-Rigid", {'name':AA, 'formula':BB, 'version':CC, 'comment':DD, 'A-units':EE, 'B-units':FF, 'R-units':GG, 'Theta-units':HH, 'sigma-units':II, 'epsilon-units':JJ})

    # Data elements

    AA=str(xls_sheet.row_values(14)[0]) # R_OH
    ET.SubElement(sub_root, "R_OH").text = AA
    BB=str(xls_sheet.row_values(14)[1]) # R_OL
    ET.SubElement(sub_root, "R_OL").text = BB
    CC=str(xls_sheet.row_values(14)[2]) # Theta_HOH
    ET.SubElement(sub_root, "Theta_HOH").text = CC
    DD=str(xls_sheet.row_values(14)[3]) # Theta_LOL
    ET.SubElement(sub_root, "Theta_LOL").text = DD
    EE=str(xls_sheet.row_values(14)[4]) # A
    ET.SubElement(sub_root, "A").text = EE
    FF=str(xls_sheet.row_values(14)[5]) # B
    ET.SubElement(sub_root, "B").text = FF
    GG=str(xls_sheet.row_values(14)[6]) # q_L
    ET.SubElement(sub_root, "q_L").text = GG
    HH=str(xls_sheet.row_values(14)[7]) # q_H
    ET.SubElement(sub_root, "q_L").text = HH
    II=str(xls_sheet.row_values(14)[8]) # R-L
    ET.SubElement(sub_root, "R-L").text = II
    JJ=str(xls_sheet.row_values(14)[9]) # R-ij
    ET.SubElement(sub_root, "R-ij").text = JJ
    if len(str(xls_sheet.row_values(14)[10])) != 0: # sigma
        KK=str(xls_sheet.row_values(14)[10])
        ET.SubElement(sub_root, "sigma").text = KK
    if len(str(xls_sheet.row_values(14)[11])) != 0: # epsilon
        LL=str(xls_sheet.row_values(14)[11])
        ET.SubElement(sub_root, "epsilon").text = LL
    return

#
# The set of functions below (all begin with XMLTo ) convert XML to .params format
#

#
# Non-Bonded Potentials Params
#
def XMLToParamsNonBondPotential_LJ_Rmin(root, output_file):
    '''
    Writes XML data for non-bonded LJ-Rmin potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = Eps,i,j[(Rmin,i,j/ri,j)**12 - 2(Rmin,i,j/ri,j)**6]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-Rmin')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("Eps,i,j = sqrt(eps,i * eps,j)\n")
    f.write("!Rmin/2: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ-Rmin')).attrib['Rmin-units']).encode('utf-8')+", ")
    f.write("Rmin,i,j = Rmin/2,i + Rmin/2,j\n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ-Rmin/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write( nonbond.find("AtomType").text.ljust(6))
        else:
            f.write("".ljust(6))
        #Insert a column of Zeros purely for formatting purposes
        f.write(("%.6f" %0).rjust(0))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" % float(nonbond.find("epsilon").text)).rjust(12))
        else:
            f.write("".rjust(12))
        if len(str(nonbond.find("Rmin")))!=0 and str(nonbond.find("Rmin")) != "None":
            f.write(("%.6f" % float(nonbond.find("Rmin").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n") 
    return



def XMLToParamsNonBondPotential_LJ(root, output_file):
    '''
    Writes XML data for non-bonded LJ potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = 4*epsilon*[(sigma/R)^12-(sigma/R)^6]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-LJ')).attrib['LJ-epsilon-units']).encode('utf-8')+", ")
    #f.write("Eps,i,j = sqrt(eps,i * eps,j)\n")
    f.write("!Rmin/2: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ')).attrib['LJ-sigma-units']).encode('utf-8')+", ")
    #f.write("Rmin,i,j = Rmin/2,i + Rmin/2,j\n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write( nonbond.find("AtomType").text.ljust(6))
        else:
            f.write("".ljust(6))
        #Insert a column of Zeros purely for formatting purposes
        # f.write(("%.6f" %0).rjust(0))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" % float(nonbond.find("epsilon").text)).rjust(12))
        else:
            f.write("".rjust(12))
        if len(str(nonbond.find("Rmin")))!=0 and str(nonbond.find("Rmin")) != "None":
            f.write(("%.6f" % float(nonbond.find("Rmin").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    return



def XMLToParamsNonBondPotential_LJ2(root, output_file):
    '''
    Writes XML data for non-bonded LJ2 potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = 4*epsilon*[(sigma/R)^12-(sigma/R)^6]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-LJ2')).attrib['LJ-epsilon-units']).encode('utf-8')+", ")
    #f.write("Eps,i,j = sqrt(eps,i * eps,j)\n")
    f.write("!Rmin/2: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ2')).attrib['LJ-sigma-units']).encode('utf-8')+", ")
    #f.write("Rmin,i,j = Rmin/2,i + Rmin/2,j\n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ2/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToParamsNonBondPotential_LJ96(root, output_file):
    '''
    Writes XML data for non-bonded LJ96 potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = epsilon*[2*(sigma/R)^9-3*(sigma/R)^6]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-LJ96')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("!Rmin/2: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ96')).attrib['sigma-units']).encode('utf-8')+", ")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ96/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write( nonbond.find("AtomType").text.ljust(6))
        else:
            f.write("".ljust(6))
        #Insert a column of Zeros purely for formatting purposes
        # f.write(("%.6f" %0).rjust(0))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" % float(nonbond.find("epsilon").text)).rjust(12))
        else:
            f.write("".rjust(12))
        if len(str(nonbond.find("Rmin")))!=0 and str(nonbond.find("Rmin")) != "None":
            f.write(("%.6f" % float(nonbond.find("Rmin").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    return



def XMLToParamsNonBondPotential_LJ_AB(root, output_file):
    '''
    Writes XML data for non-bonded LJ-AB potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = A/(R^12)-B/(R^6)\n!\n" )
    f.write("!A: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-AB')).attrib['A-units']).encode('utf-8')+", ")
    f.write("!B: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ-AB')).attrib['B-units']).encode('utf-8')+", ")
    f.write("!Combining Rule: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ-AB')).attrib['Combining-Rule']).encode('utf-8')+", ")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ-AB/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write(nonbond.find("AtomType").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("A")))!=0 and str(nonbond.find("A")) != "None":
            f.write(("%.6f" %float(nonbond.find("A").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("B")))!=0 and str(nonbond.find("B")) != "None": 
            f.write(("%.6f" %float(nonbond.find("B").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return




def XMLToParamsNonBondPotential_LJ2_AB(root, output_file):
    '''
    Writes XML data for non-bonded LJ2-AB potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = A/(R^12)-B/(R^6)\n!\n" )
    f.write("!A: " + ((root.find('./NonBondPotential/NonBondPotential-LJ2-AB')).attrib['A-units']).encode('utf-8')+", ")
    f.write("!B: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ2-AB')).attrib['B-units']).encode('utf-8')+", ")
    f.write("!Combining Rule: "+ ((root.find('./NonBondPotential/NonBondPotential-LJ-AB')).attrib['Combining-Rule']).encode('utf-8')+", ")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ2-AB/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("A")))!=0 and str(nonbond.find("A")) != "None":
            f.write(("%.6f" %float(nonbond.find("A").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("B")))!=0 and str(nonbond.find("B")) != "None": 
            f.write(("%.6f" %float(nonbond.find("B").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return




def XMLToParamsNonBondPotential_LJ_GROMACS(root, output_file):
    '''
    Writes XML data for non-bonded LJ-Gromacs potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Lennard-Jones) = 4*epsilon*[(sigma/R)^12-(sigma/R)^6] + S_LJ(R)\n!\n" )
    f.write("epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-GROMACS')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("sigma: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-GROMACS')).attrib['sigma-units']).encode('utf-8')+", ")
    f.write("r: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-GROMACS')).attrib['r-units']).encode('utf-8'))
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ-GROMACS/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("r_1")))!=0 and str(nonbond.find("r_1")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("r_cut")))!=0 and str(nonbond.find("r_cut")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_cut").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return




def XMLToParamsNonBondPotential_Class2(root, output_file):
    '''
    Writes XML data for non-bonded LJ Class2 potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Class 2) = Eps,i,j[(Rmin,i,j/ri,j)**12 - 2(Rmin,i,j/ri,j)**6]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-Class2')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("Eps,i,j = sqrt(eps,i * eps,j)\n")
    f.write("!Rmin/2: "+ ((root.find('./NonBondPotential/NonBondPotential-Class2')).attrib['Rmin-units']).encode('utf-8')+", ")
    f.write("Rmin,i,j = Rmin/2,i + Rmin/2,j\n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Class2/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write( nonbond.find("AtomType").text.ljust(6))
        else:
            f.write("".ljust(6))
        #Insert a column of Zeros purely for formatting purposes
        f.write(("%.6f" %0).rjust(0))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" % float(nonbond.find("epsilon").text)).rjust(12))
        else:
            f.write("".rjust(12))
        if len(str(nonbond.find("Rmin")))!=0 and str(nonbond.find("Rmin")) != "None":
            f.write(("%.6f" % float(nonbond.find("Rmin").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n") 
        return




def XMLToParamsNonBondPotential_EnergyRenorm(root, output_file):
    '''
    Writes XML data for non-bonded LJ Energy Renormalization potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Energy Renormalization) = [epsilon_g+[(epsilon_A-epsilon_g)/(1+exp(-k_sig*(T-T_sig)))]]*[((sigma*(a*T+b))/R)^12-((sigma*(a*T+b))/R)^6]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-EnergyRenorm')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("!sigma: "+ ((root.find('./NonBondPotential/NonBondPotential-EnergyRenorm')).attrib['sigma-units']).encode('utf-8')+", ")
    f.write("!T_sig: "+ ((root.find('./NonBondPotential/NonBondPotential-EnergyRenorm')).attrib['T_sig-units']).encode('utf-8')+", ")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-EnergyRenorm/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon_g")))!=0 and str(nonbond.find("epsilon_g")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon_g").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon_A")))!=0 and str(nonbond.find("epsilon_A")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon_A").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("a")))!=0 and str(nonbond.find("a")) != "None":
            f.write(("%.3f" %float(nonbond.find("a").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("b")))!=0 and str(nonbond.find("b")) != "None":
            f.write(("%.3f" %float(nonbond.find("b").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("k_sig")))!=0 and str(nonbond.find("k_sig")) != "None":
            f.write(("%.3f" %float(nonbond.find("k_sig").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("T_sig")))!=0 and str(nonbond.find("T_sig")) != "None":
            f.write(("%.3f" %float(nonbond.find("T_sig").text)).ljust(0))
        else:
            f.write("".ljust(0))			
        f.write("\n")
    f.write("\n")
    return




def XMLToParamsNonBondPotential_Mie(root, output_file):
    '''
    Writes XML data for non-bonded LJ Mie potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Mie) = C*epsilon*[(sigma/R)^m_rep-(sigma/R)^n_att]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-Mie')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("!sigma: "+ ((root.find('./NonBondPotential/NonBondPotential-Mie')).attrib['sigma-units']).encode('utf-8')+", ")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Mie/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("C")))!=0 and str(nonbond.find("C")) != "None":
            f.write(("%.6f" %float(nonbond.find("C").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("m_rep")))!=0 and str(nonbond.find("m_rep")) != "None":
            f.write(("%.3f" %float(nonbond.find("m_rep").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("n_att")))!=0 and str(nonbond.find("n_att")) != "None":
            f.write(("%.3f" %float(nonbond.find("n_att").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return




def XMLToParamsNonBondPotential_Soft(root, output_file):
    '''
    Writes XML data for non-bonded soft potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(Soft) = a_ij*[1+cos(pi*r/r_c)]\n!\n" )
    f.write("!a_ij: " + ((root.find('./NonBondPotential/NonBondPotential-Soft')).attrib['a_ij-units']).encode('utf-8')+", ")
    f.write("!r_c: "+ ((root.find('./NonBondPotential/NonBondPotential-Soft')).attrib['r_c-units']).encode('utf-8')+", ")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Soft/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("a_ij")))!=0 and str(nonbond.find("a_ij")) != "None": 
            f.write(("%.6f" %float(nonbond.find("a_ij").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("r_c")))!=0 and str(nonbond.find("r_c")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_c").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return




def XMLtoParamsNonBondPotential_Weeks_Chandler_Anderson(root, output_file):
    '''
    Writes XML data for non-bonded LJ-WCA potential in Vega format.
    '''
    f = output_file
    f.write("NONBONDED\n\n" ) 
    f.write("!\n!V(WCA) = 4*epsilon*[((sigma/R)^-12)-((sigma/R)^-6)+(1/4)]\n!\n" )
    f.write("!epsilon: " + ((root.find('./NonBondPotential/NonBondPotential-Weeks-Chandler-Anderson')).attrib['epsilon-units']).encode('utf-8')+", ")
    f.write("!sigma: "+ ((root.find('./NonBondPotential/NonBondPotential-Weeks-Chandler-Anderson')).attrib['sigma-units']).encode('utf-8')+", ")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Weeks-Chandler-Anderson/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("r_cut")))!=0 and str(nonbond.find("r_cut")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_cut").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



# Vega: Bond Potentials Forms

def XMLToParamsBondPotential_Harmonic(root, output_file):
    '''
    Writes XML data for harmonic bond potential in Vega format.
    '''
    f = output_file
    f.write("BONDS\n!\n" )
    f.write("!V(bond) = Kb(b - b0)**2\n!\n")
    f.write("!Kb: " + ((root.find('./BondPotential/BondPotential-Harmonic')).attrib['K-units']).encode('utf-8')+"\n")
    f.write("!b0: " + ((root.find('./BondPotential/BondPotential-Harmonic')).attrib['R0-units']).encode('utf-8')+"\n!\n")
    for bond in root.findall('./BondPotential/BondPotential-Harmonic/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("K")))!=0 and str(bond.find("K")) != "None": 
            f.write(("%.3f" %float(bond.find("K").text)).rjust(8))
        else:
            f.write("".rjust(8))
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.4f" %float(bond.find("R0").text)).rjust(11))
        else:
            f.write("".rjust(11))
       
        f.write("\n\n\n")
    return




def XMLToParamsBondPotential_Morse(root, output_file):
    '''
    Writes XML data for Morse bond potential in Vega format.
    '''
    f = output_file
    f.write("BONDS\n!\n" )
    f.write("!V(bond) = D*[(1-exp(-A(R-R0))]^2\n!\n")
    f.write("!D: " + ((root.find('./BondPotential/BondPotential-Morse')).attrib['D-units']).encode('utf-8')+"\n")
    f.write("!A: " + ((root.find('./BondPotential/BondPotential-Morse')).attrib['A-units']).encode('utf-8')+"\n")
    f.write("!R0: " + ((root.find('./BondPotential/BondPotential-Morse')).attrib['R0-units']).encode('utf-8')+"\n!\n")
    for bond in root.findall('./BondPotential/BondPotential-Morse/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("D")))!=0 and str(bond.find("D")) != "None": 
            f.write(("%.4f" %float(bond.find("D").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(bond.find("A")))!=0 and str(bond.find("A")) != "None": 
            f.write(("%.1f" %float(bond.find("A").text)).ljust(7))
        else:
            f.write("".ljust(7))        
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.1f" %float(bond.find("R0").text)).ljust(5))
        else:
            f.write("".ljust(5))
       
        f.write("\n")
    return




def XMLtoParamsBondPotential_Class2(root, output_file):
    '''
    Writes XML data for Class2 bond potential in Vega format.
    '''
    f = output_file
    f.write("BONDS\n!\n" )
    f.write("!V(bond) = K2*(R-R0)^2+K3*(R-R0)^3+K4*(R-R0)^4\n!\n")
    f.write("!K: " + ((root.find('./BondPotential/BondPotential-Class2')).attrib['K-units']).encode('utf-8')+"\n")
    f.write("!R0: " + ((root.find('./BondPotential/BondPotential-Class2')).attrib['R0-units']).encode('utf-8')+"\n!\n")
    for bond in root.findall('./BondPotential/BondPotential-Class2/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("K2")))!=0 and str(bond.find("K2")) != "None": 
            f.write(("%.3f" %float(bond.find("K2").text)).rjust(8))
        else:
            f.write("".rjust(8))
        if len(str(bond.find("K3")))!=0 and str(bond.find("K3")) != "None": 
            f.write(("%.3f" %float(bond.find("K3").text)).rjust(8))
        else:
            f.write("".rjust(8))
        if len(str(bond.find("K4")))!=0 and str(bond.find("K4")) != "None": 
            f.write(("%.3f" %float(bond.find("K4").text)).rjust(8))
        else:
            f.write("".rjust(8))			
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.1f" %float(bond.find("R0").text)).ljust(5))
        else:
            f.write("".ljust(5))
       
        f.write("\n")
    return




def XMLtoParamsBondPotential_FENE(root, output_file):
    '''
    Writes XML data for FENE bond potential in Vega format.
    '''
    f = output_file
    f.write("BONDS\n!\n" )
    f.write("!V(bond) = Kb(b - b0)**2\n!\n")
    f.write("!Kb: " + ((root.find('./BondPotential/BondPotential-FENE')).attrib['K-units']).encode('utf-8')+"\n")
    f.write("!b0: " + ((root.find('./BondPotential/BondPotential-FENE')).attrib['R0-units']).encode('utf-8')+"\n!\n")
    for bond in root.findall('./BondPotential/BondPotential-FENE/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("K")))!=0 and str(bond.find("K")) != "None": 
            f.write(("%.3f" %float(bond.find("K").text)).rjust(8))
        else:
            f.write("".rjust(8))
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.4f" %float(bond.find("R0").text)).rjust(11))
        else:
            f.write("".rjust(11))
       
        f.write("\n")
    return



		
# Vega: Angle Potentials Params	

def XMLToParamsAnglePotential_Harmonic(root, output_file):
    '''
    Writes XML data for harmonic angle potential in Vega format.
    '''
    f = output_file
    f.write("ANGLES\n!\n" )
    f.write("!V(angle) = Ktheta(Theta - Theta0)**2\n!\n")
    f.write("!Ktheta: " + ((root.find('./AnglePotential/AnglePotential-Harmonic')).attrib['Ka-units']).encode('utf-8')+"\n")
    f.write("!Theta0: " + ((root.find('./AnglePotential/AnglePotential-Harmonic')).attrib['Theta0-units']).encode('utf-8')+"\n!\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Harmonic/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
         f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.3f" %float(angle.find("Ka").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).rjust(11))
        else: 
            f.write("".rjust(11))
        
        f.write("\n")
    return



def XMLToParamsAnglePotential_Cosine(root, output_file):
    '''
    Writes XML data for cosine angle potential in Vega format.
    '''
    f = output_file
    f.write("ANGLES\n!\n" )
    f.write("!V(angle) = Ka*[1+cos(theta)]\n!\n")
    f.write("!Ktheta: " + ((root.find('./AnglePotential/AnglePotential-Cosine')).attrib['Ka-units']).encode('utf-8')+"\n!\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Cosine/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
         f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.3f" %float(angle.find("Ka").text)).rjust(7))
        else:
            f.write("".rjust(7))
        
        f.write("\n")
    return



def XMLToParamsAnglePotential_COS2(root, output_file):
    '''
    Writes XML data for cosine-squared angle potential in Vega format.
    '''
    f = output_file
    f.write("ANGLES\n!\n" )
    f.write("!V(angle) = Ka*[cos(Theta)-cos(Theta0)]^2\n!\n")
    f.write("!Ktheta: " + ((root.find('./AnglePotential/AnglePotential-COS2')).attrib['Ka-units']).encode('utf-8')+"\n")
    f.write("!Theta0: " + ((root.find('./AnglePotential/AnglePotential-COS2')).attrib['Theta0-units']).encode('utf-8')+"\n!\n")
    for angle in root.findall('./AnglePotential/AnglePotential-COS2/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
         f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.3f" %float(angle.find("Ka").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).rjust(11))
        else: 
            f.write("".rjust(11))
        
        f.write("\n")
    return



def XMLToParamsAnglePotential_CHARMM(root, output_file):
    '''
    Writes XML data for CHARMM angle potential in Vega format.
    '''
    f = output_file
    f.write("ANGLES\n!\n" )
    f.write("!V(angle) = Ka*(Theta-Theta0)^2+Kub*(R-Rub)^2\n!\n")
    f.write("!Ktheta: " + ((root.find('./AnglePotential/AnglePotential-CHARMM')).attrib['Ka-units']).encode('utf-8')+"\n")
    f.write("!Theta0: " + ((root.find('./AnglePotential/AnglePotential-CHARMM')).attrib['Theta0-units']).encode('utf-8')+"\n")
    f.write("!Kub: " + ((root.find('./AnglePotential/AnglePotential-CHARMM')).attrib['Kub-units']).encode('utf-8')+"\n")
    f.write("!Rub: " + ((root.find('./AnglePotential/AnglePotential-CHARMM')).attrib['Rub-units']).encode('utf-8')+"\n!\n")
    for angle in root.findall('./AnglePotential/AnglePotential-CHARMM/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
         f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.3f" %float(angle.find("Ka").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).rjust(11))
        else: 
            f.write("".rjust(11))
        if len(str(angle.find("Kub")))!=0 and str(angle.find("Kub")) != "None": 
            f.write(("%.3f" %float(angle.find("Kub").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("Rub")))!=0 and str(angle.find("Rub")) != "None": 
            f.write(("%.3f" %float(angle.find("Rub").text)).rjust(7))
        else:
            f.write("".rjust(7))
        
        f.write("\n")
    return



def XMLToParamsAnglePotential_Class2(root, output_file):
    '''
    Writes XML data for Class2 angle potential in Vega format.
    '''
    f = output_file
    f.write("ANGLES\n!\n" )
    f.write("!V(angle) = K2*(Theta-Theta0)^2+K3*(Theta-Theta0)^3+K4*(Theta-Theta0)^4\n!\n")
    f.write("!K: " + ((root.find('./AnglePotential/AnglePotential-Class2')).attrib['K-units']).encode('utf-8')+"\n")
    f.write("!Theta0: " + ((root.find('./AnglePotential/AnglePotential-Class2')).attrib['Theta0-units']).encode('utf-8')+"\n!\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Class2/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
         f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("K2")))!=0 and str(angle.find("K2")) != "None": 
            f.write(("%.3f" %float(angle.find("K2").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("K3")))!=0 and str(angle.find("K3")) != "None": 
            f.write(("%.3f" %float(angle.find("K3").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("K4")))!=0 and str(angle.find("K4")) != "None": 
            f.write(("%.3f" %float(angle.find("K4").text)).rjust(7))
        else:
            f.write("".rjust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).rjust(11))
        else: 
            f.write("".rjust(11))
        
        f.write("\n")
    return


		
# Vega: Dihedral Potentials Forms

def XMLToParamsDihedralPotential_CHARMM(root, output_file):
    '''
    Writes XML data for CHARMM dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = Kchi(1 + cos(n(chi) + delta))\n!\n")
    f.write("!Kchi: " + ((root.find('./DihedralPotential/DihedralPotential-CHARMM')).attrib['Kd-units']).encode('utf-8')+"\n")
    f.write("!n: multiplicity\n")
    f.write("!delta: " + ((root.find('./DihedralPotential/DihedralPotential-CHARMM')).attrib['Phi0-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-CHARMM/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("Kd")))!=0 and str(dihedral.find("Kd")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("Kd").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("N")))!=0 and str(dihedral.find("N")) != "None": 
            f.write(("%.0f"%float((dihedral.find("N").text))).ljust(4))
        else:
            f.write("".ljust(4))
        if len(str(dihedral.find("Phi0")))!=0 and str(dihedral.find("Phi0")) != "None": 
            f.write(("%.3f" %float(dihedral.find("Phi0").text)).rjust(7))
        else:
            f.write("".rjust(7))
        f.write("\n")
    return



def XMLToParamsDihedralPotential_Harmonic(root, output_file):
    '''
    Writes XML data for harmonic dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = Kd*[1+Ns*cos(N*Phi)]\n!\n")
    f.write("!Kd: " + ((root.find('./DihedralPotential/DihedralPotential-Harmonic')).attrib['Kd-units']).encode('utf-8')+"\n")
    f.write("!n: multiplicity\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Harmonic/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("Kd")))!=0 and str(dihedral.find("Kd")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("Kd").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("Ns")))!=0 and str(dihedral.find("Ns")) != "None": 
            f.write(("%.0f"%float((dihedral.find("Ns").text))).ljust(4))
        else:
            f.write("".ljust(4))
        if len(str(dihedral.find("N")))!=0 and str(dihedral.find("N")) != "None": 
            f.write(("%.0f"%float((dihedral.find("N").text))).ljust(4))
        else:
            f.write("".ljust(4))
        f.write("\n")
    return



def XMLToParamsDihedralPotential_FourierSimple(root, output_file):
    '''
    Writes XML data for Fourier-simple dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = K1*[1+cos(Phi)]+K2*[1+cos(2*Phi)]+K3*[1+cos(3*Phi)]+K4*[1+cos(4*Phi)]+K5*[1+cos(5*Phi)]\n!\n")
    f.write("!Kn: " + ((root.find('./DihedralPotential/DihedralPotential-FourierSimple')).attrib['Kn-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-FourierSimple/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K1").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K2").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K3").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K4")))!=0 and str(dihedral.find("K4")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K4").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K5")))!=0 and str(dihedral.find("K5")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K5").text)).ljust(8))
        else:
            f.write("".ljust(8))
        f.write("\n")
    return



def XMLToParamsDihedralPotential_Fourier(root, output_file):
    '''
    Writes XML data for Fourier dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = K1*[1+cos(N1*Phi-D1)]+K2*[1+cos(N2*Phi-D2)]+K3*[1+cos(N3*Phi-D3)]+K4*[1+cos(N4*Phi-D4)]+K5*[1+cos(N5*Phi-D5)]\n!\n")
    f.write("!Kn: " + ((root.find('./DihedralPotential/DihedralPotential-Fourier')).attrib['Kn-units']).encode('utf-8')+"\n")
    f.write("!Dn: " + ((root.find('./DihedralPotential/DihedralPotential-Fourier')).attrib['Dn-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Fourier/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K1").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N1")))!=0 and str(dihedral.find("N1")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N1").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D1")))!=0 and str(dihedral.find("D1")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D1").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K2").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N2")))!=0 and str(dihedral.find("N2")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N2").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D2")))!=0 and str(dihedral.find("D2")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D2").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K3").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N3")))!=0 and str(dihedral.find("N3")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N3").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D3")))!=0 and str(dihedral.find("D3")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D3").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K4")))!=0 and str(dihedral.find("K4")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K4").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N4")))!=0 and str(dihedral.find("N4")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N4").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D4")))!=0 and str(dihedral.find("D4")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D4").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K5")))!=0 and str(dihedral.find("K5")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K5").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N5")))!=0 and str(dihedral.find("N5")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N5").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D5")))!=0 and str(dihedral.find("D5")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D5").text)).rjust(10))
        else:
            f.write("".rjust(10))
        f.write("\n")
    return



def XMLToParamsDihedralPotential_Class2(root, output_file):
    '''
    Writes XML data for Class2 dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = K1*[1-cos(Phi-Phi1)]+K2*[1-cos(2*Phi-Phi2)]+K3*[1-cos(3*Phi-Phi3)]\n!\n")
    f.write("!Kn: " + ((root.find('./DihedralPotential/DihedralPotential-Class2')).attrib['Kn-units']).encode('utf-8')+"\n")
    f.write("!Phin: " + ((root.find('./DihedralPotential/DihedralPotential-Class2')).attrib['Phin-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Class2/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K1").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K2").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K3").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("Phi1")))!=0 and str(dihedral.find("Phi1")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("Phi1").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("Phi2")))!=0 and str(dihedral.find("Phi2")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("Phi2").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("Phi3")))!=0 and str(dihedral.find("Phi3")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("Phi3").text)).ljust(8))
        else:
            f.write("".ljust(8))
        f.write("\n")
    return



def XMLToParamsDihedralPotential_OPLS(root, output_file):
    '''
    Writes XML data for OPLS dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = 0.5*{K1*[1+cos(Phi)]+K2*[1-cos(2*Phi)]+K3*[1+cos(3*Phi)]+K4*[1-cos(4*Phi)]}\n!\n")
    f.write("!Kn: " + ((root.find('./DihedralPotential/DihedralPotential-OPLS')).attrib['Kn-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-OPLS/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K1").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K2").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K3").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("K4")))!=0 and str(dihedral.find("K4")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K4").text)).ljust(8))
        else:
            f.write("".ljust(8))
        f.write("\n")
    return



def XMLToParamsDihedralPotential_Quadratic(root, output_file):
    '''
    Writes XML data for Quadratic dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = Kchi*(Phi-Phi0)^2\n!\n")
    f.write("!Kchi: " + ((root.find('./DihedralPotential/DihedralPotential-Quadratic')).attrib['Kd-units']).encode('utf-8')+"\n")
    f.write("!delta: " + ((root.find('./DihedralPotential/DihedralPotential-Quadratic')).attrib['Phi0-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Quadratic/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("Kd")))!=0 and str(dihedral.find("Kd")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("Kd").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("Phi0")))!=0 and str(dihedral.find("Phi0")) != "None": 
            f.write(("%.3f" %float(dihedral.find("Phi0").text)).rjust(7))
        else:
            f.write("".rjust(7))
        f.write("\n")
    return



def XMLToParamsDihedralPotential_Multiharmonic(root, output_file):
    '''
    Writes XML data for Multiharmonic dihedral potential in Vega format.
    '''
    f = output_file
    f.write("DIHEDRALS\n!\n" )
    f.write("!V(dihedral) = A1+A2*cos(Phi)+A3*cos^2(Phi)+A4*cos^3(Phi)+A5*cos^4(Phi)\n!\n")
    f.write("!An: " + ((root.find('./DihedralPotential/DihedralPotential-Multiharmonic')).attrib['An-units']).encode('utf-8')+"\n!\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Multiharmonic/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(dihedral.find("A1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K1").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("A2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K2").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("A3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K3").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("A4")))!=0 and str(dihedral.find("K4")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K4").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(dihedral.find("A5")))!=0 and str(dihedral.find("K5")) != "None": 
            f.write(( "%.4f"%float(dihedral.find("K5").text)).ljust(8))
        else:
            f.write("".ljust(8))
        f.write("\n")
    return



# Vega: Improper Potentials Forms

def XMLToParamsImproperPotential_Harmonic(root, output_file):
    '''
    Writes XML data for harmonic improper potential in Vega format.
    '''
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = Kpsi(psi - psi0)**2\n!\n" )
    f.write("!Kpsi: " + ((root.find('./ImproperPotential/ImproperPotential-Harmonic')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!psi0: "+ ((root.find('./ImproperPotential/ImproperPotential-Harmonic')).attrib['Chi0-units']).encode('utf-8')+"\n")
    f.write("!note that the second column of numbers (0) is ignored\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-Harmonic/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
            f.write(improper.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.5f" %float(improper.find("Ki").text)).rjust(8))
        else:
            f.write("".rjust(8))
        f.write((str(0)).rjust(4))
        if len(str(improper.find("Chi0")))!=0 and str(improper.find("Chi0")) != "None": 
            f.write(("%.4f" %float(improper.find("Chi0").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    return



def XMLToParamsImproperPotential_CHARMM(root, output_file):
    '''
    Writes XML data for CHARMM improper potential in Vega format.
    '''
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = Kd*[1+cos(N*Phi+Phi0)]\n!\n" )
    f.write("!Kpsi: " + ((root.find('./ImproperPotential/ImproperPotential-CHARMM')).attrib['Kd-units']).encode('utf-8')+"\n")
    f.write("!n: multiplicity\n")
    f.write("!delta: " + ((root.find('./ImproperPotential/ImproperPotential-CHARMM')).attrib['Phi0-units']).encode('utf-8')+"\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-CHARMM/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
            f.write(improper.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("Kd")))!=0 and str(improper.find("Kd")) != "None": 
            f.write(("%.5f" %float(improper.find("Kd").text)).rjust(8))
        else:
            f.write("".rjust(8))
        if len(str(improper.find("N")))!=0 and str(improper.find("N")) != "None": 
            f.write(("%.0f"%float((improper.find("N").text))).ljust(4))
        else:
            f.write("".ljust(4))
        if len(str(improper.find("Phi0")))!=0 and str(improper.find("Phi0")) != "None": 
            f.write(("%.3f" %float(improper.find("Phi0").text)).rjust(7))
        else:
            f.write("".rjust(7))
        f.write("\n")
    return



def XMLToParamsImproperPotential_Class2(root, output_file):
    '''
    Writes XML data for Class2 improper potential in Vega format.
    '''
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = Ki*(Chi-Chi0)^2\n!\n" )
    f.write("!Ki: " + ((root.find('./ImproperPotential/ImproperPotential-Class2')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!Chi0: " + ((root.find('./ImproperPotential/ImproperPotential-Class2')).attrib['Chi0-units']).encode('utf-8')+"\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-Class2/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("Chi0")))!=0 and str(improper.find("Chi0")) != "None": 
            f.write(("%.1f" %float(improper.find("Chi0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToParamsImproperPotential_COS2(root, output_file):
    '''
    Writes XML data for cosine-squared improper potential in Vega format.
    '''
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = Ki*cos(Chi-Chi0)**2\n!\n" )
    f.write("!Ki: " + ((root.find('./ImproperPotential/ImproperPotential-COS2')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!Chi0: " + ((root.find('./ImproperPotential/ImproperPotential-COS2')).attrib['Chi0-units']).encode('utf-8')+"\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-COS2/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("Chi0")))!=0 and str(improper.find("Chi0")) != "None": 
            f.write(("%.1f" %float(improper.find("Chi0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToParamsImproperPotential_CVFF(root, output_file):
    '''
    Writes XML data for CVFF improper potential in Vega format.
    '''
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = Ki*[1+Ns*cos(N*Phi)]\n!\n" )
    f.write("!Ki: " + ((root.find('./ImproperPotential/ImproperPotential-CVFF')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!n: multiplicity\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-CVFF/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("Ns")))!=0 and str(improper.find("Ns")) != "None": 
            f.write(("%.1f" %float(improper.find("Ns").text)).ljust(2))
        else:
            f.write("".ljust(2))
        if len(str(improper.find("N")))!=0 and str(improper.find("N")) != "None": 
            f.write(("%.1f" %float(improper.find("N").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToParamsImproperPotential_Fourier(root, output_file):
    '''
    Writes XML data for Fourier improper potential in Vega format.
    '''
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = Ki*[C0+C1*cos(w)+C2*cos(2*w)]\n!\n" )
    f.write("!Ki: " + ((root.find('./ImproperPotential/ImproperPotential-Fourier')).attrib['Ki-units']).encode('utf-8')+"\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-Fourier/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("C0")))!=0 and str(improper.find("C0")) != "None": 
            f.write(("%.4f" %float(improper.find("C0").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("C1")))!=0 and str(improper.find("C1")) != "None": 
            f.write(("%.4f" %float(improper.find("C1").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("C2")))!=0 and str(improper.find("C2")) != "None": 
            f.write(("%.4f" %float(improper.find("C2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToParamsImproperPotential_Umbrella(root, output_file):
    '''
    Writes XML data for Umbrella improper potential in Vega format.
    '''
    f = output_file
    f.write("IMPROPER\n!\n")
    f.write("!V(improper) = 0.5*K*[{1+cos(w0)}/sin(w0)]^2*[cos(w)-cos(w0)] ~ w0 ≠ 0° <> K*[1-cos(w)] ~ w0 = 0°\n!\n" )
    f.write("!Kpsi: " + ((root.find('./ImproperPotential/ImproperPotential-Umbrella')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!psi0: "+ ((root.find('./ImproperPotential/ImproperPotential-Umbrella')).attrib['Chi0-units']).encode('utf-8')+"\n")
    f.write("!note that the second column of numbers (0) is ignored\n!\n")
        
    for improper in root.findall('./ImproperPotential/ImproperPotential-Umbrella/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
            f.write(improper.find("AT-3").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.5f" %float(improper.find("Ki").text)).rjust(8))
        else:
            f.write("".rjust(8))
        f.write((str(0)).rjust(4))
        if len(str(improper.find("w0")))!=0 and str(improper.find("w0")) != "None": 
            f.write(("%.4f" %float(improper.find("w0").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    return



# Vega: Cross Potentials Forms

def XMLtoParamsCrossPotential_BondBond(root, output_file):
    '''
    Writes XML data for Bond-Bond Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = M*(R-R1)*(R-R2)\n!\n" )
    f.write("!M: " + ((root.find('./CrossPotential/CrossPotential-BondBond')).attrib['M-units']).encode('utf-8')+"\n")
    f.write("!Ri: " + ((root.find('./CrossPotential/CrossPotential-BondBond')).attrib['Ri-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-BondBond/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("M")))!=0 and str(cross.find("M")) != "None": 
            f.write(("%.6f" %float(cross.find("M").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R2")))!=0 and str(cross.find("R2")) != "None": 
            f.write(("%.3f" %float(cross.find("R2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoParamsCrossPotential_BondBond13(root, output_file):
    '''
    Writes XML data for Bond-Bond13 Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = N*(Rij-R1)*(Rkl-R3)\n!\n" )
    f.write("!N: " + ((root.find('./CrossPotential/CrossPotential-BondBond13')).attrib['N-units']).encode('utf-8')+"\n")
    f.write("!Ri: " + ((root.find('./CrossPotential/CrossPotential-BondBond13')).attrib['Ri-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-BondBond13/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("M")))!=0 and str(cross.find("M")) != "None": 
            f.write(("%.6f" %float(cross.find("M").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R3")))!=0 and str(cross.find("R3")) != "None": 
            f.write(("%.3f" %float(cross.find("R3").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoParamsCrossPotential_AngleAngle(root, output_file):
    '''
    Writes XML data for Angle-Angle Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = M1*(Theta-Theta1)(Theta-Theta3)+M2*(Theta-Theta1)(Theta-Theta2)+M3*(Theta-Theta2)(Theta-Theta3)\n!\n" )
    f.write("!M: " + ((root.find('./CrossPotential/CrossPotential-AngleAngle')).attrib['M-units']).encode('utf-8')+"\n")
    f.write("!Theta: " + ((root.find('./CrossPotential/CrossPotential-AngleAngle')).attrib['Theta-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-AngleAngle/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("M1")))!=0 and str(cross.find("M1")) != "None": 
            f.write(("%.6f" %float(cross.find("M1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("M2")))!=0 and str(cross.find("M2")) != "None": 
            f.write(("%.6f" %float(cross.find("M2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("M3")))!=0 and str(cross.find("M3")) != "None": 
            f.write(("%.6f" %float(cross.find("M3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta1")))!=0 and str(cross.find("Theta1")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta2")))!=0 and str(cross.find("Theta2")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta3")))!=0 and str(cross.find("Theta3")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta3").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoParamsCrossPotential_BondAngle(root, output_file):
    '''
    Writes XML data for Bond-Angle Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = N1*(R-R1)*(Theta-Theta0)+N2*(R-R2)*(Theta-Theta0)\n!\n" )
    f.write("!N: " + ((root.find('./CrossPotential/CrossPotential-BondAngle')).attrib['N-units']).encode('utf-8')+"\n")
    f.write("!Ri: " + ((root.find('./CrossPotential/CrossPotential-BondAngle')).attrib['Ri-units']).encode('utf-8')+"\n")
    f.write("!Theta0: " + ((root.find('./CrossPotential/CrossPotential-BondAngle')).attrib['Theta0-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-BondAngle/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("Theta0")))!=0 and str(cross.find("Theta0")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta0").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("N1")))!=0 and str(cross.find("N1")) != "None": 
            f.write(("%.6f" %float(cross.find("N1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("N2")))!=0 and str(cross.find("N2")) != "None": 
            f.write(("%.6f" %float(cross.find("N2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R2")))!=0 and str(cross.find("R2")) != "None": 
            f.write(("%.3f" %float(cross.find("R2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoParamsCrossPotential_MiddleBondTorsion(root, output_file):
    '''
    Writes XML data for Middle-Bond Torsion Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = (R-R2)*[A1*cos(Phi)+A2*cos(2*Phi)+A3*cos(3*Phi)]\n!\n" )
    f.write("!A: " + ((root.find('./CrossPotential/CrossPotential-MiddleBondTorsion')).attrib['A-units']).encode('utf-8')+"\n")
    f.write("!R: " + ((root.find('./CrossPotential/CrossPotential-MiddleBondTorsion')).attrib['R-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-MiddleBondTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("A1")))!=0 and str(cross.find("A1")) != "None": 
            f.write(("%.6f" %float(cross.find("A1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("A2")))!=0 and str(cross.find("A2")) != "None": 
            f.write(("%.6f" %float(cross.find("A2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("A3")))!=0 and str(cross.find("A3")) != "None": 
            f.write(("%.6f" %float(cross.find("A3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R2")))!=0 and str(cross.find("R2")) != "None": 
            f.write(("%.3f" %float(cross.find("R2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoParamsCrossPotential_EndBondTorsion(root, output_file):
    '''
    Writes XML data for End-Bond Torsion Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = (R-R1)*[B1*cos(Phi)+B2*cos(2*Phi)+B3*cos(3*Phi)]+(R-R3)*[C1*cos(Phi)+C2*cos(2*Phi)+C3*cos(3*Phi)]\n!\n" )	
    f.write("!B: " + ((root.find('./CrossPotential/CrossPotential-EndBondTorsion')).attrib['B-units']).encode('utf-8')+"\n")
    f.write("!C: " + ((root.find('./CrossPotential/CrossPotential-EndBondTorsion')).attrib['C-units']).encode('utf-8')+"\n")
    f.write("!R: " + ((root.find('./CrossPotential/CrossPotential-EndBondTorsion')).attrib['R-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-EndBondTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("B1")))!=0 and str(cross.find("B1")) != "None": 
            f.write(("%.6f" %float(cross.find("B1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("B2")))!=0 and str(cross.find("B2")) != "None": 
            f.write(("%.6f" %float(cross.find("B2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("B3")))!=0 and str(cross.find("B3")) != "None": 
            f.write(("%.6f" %float(cross.find("B3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("C1")))!=0 and str(cross.find("C1")) != "None": 
            f.write(("%.6f" %float(cross.find("C1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("C2")))!=0 and str(cross.find("C2")) != "None": 
            f.write(("%.6f" %float(cross.find("C2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("C3")))!=0 and str(cross.find("C3")) != "None": 
            f.write(("%.6f" %float(cross.find("C3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("R3")))!=0 and str(cross.find("R3")) != "None": 
            f.write(("%.3f" %float(cross.find("R3").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoParamsCrossPotential_AngleTorsion(root, output_file):
    '''
    Writes XML data for Angle Torsion Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = (Theta-Theta1)*[D1*cos(Phi)+D2*cos(2*Phi)+D3*cos(3*Phi)]+(Theta-Theta2)*[E1*cos(Phi)+E2*cos(2*Phi)+E3*cos(3*Phi)]\n!\n")
    f.write("!D: " + ((root.find('./CrossPotential/CrossPotential-AngleTorsion')).attrib['D-units']).encode('utf-8')+"\n")
    f.write("!E: " + ((root.find('./CrossPotential/CrossPotential-AngleTorsion')).attrib['E-units']).encode('utf-8')+"\n")
    f.write("!Theta: " + ((root.find('./CrossPotential/CrossPotential-AngleTorsion')).attrib['Theta-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-AngleTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("D1")))!=0 and str(cross.find("D1")) != "None": 
            f.write(("%.6f" %float(cross.find("D1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("D2")))!=0 and str(cross.find("D2")) != "None": 
            f.write(("%.6f" %float(cross.find("D2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("D3")))!=0 and str(cross.find("D3")) != "None": 
            f.write(("%.6f" %float(cross.find("D3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("E1")))!=0 and str(cross.find("E1")) != "None": 
            f.write(("%.6f" %float(cross.find("E1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("E2")))!=0 and str(cross.find("E2")) != "None": 
            f.write(("%.6f" %float(cross.find("E2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("E3")))!=0 and str(cross.find("E3")) != "None": 
            f.write(("%.6f" %float(cross.find("E3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta1")))!=0 and str(cross.find("Theta1")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("Theta2")))!=0 and str(cross.find("Theta2")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoParamsCrossPotential_AngleAngleTorsion(root, output_file):
    '''
    Writes XML data for Angle-Angle Torsion Cross potential in Vega format.
    '''
    f = output_file
    f.write("CROSS\n!\n")
    f.write("!V(cross) = M(Theta-Theta1)*(Theta-Theta2)*cos(Phi)\n!\n")
    f.write("!M: " + ((root.find('./CrossPotential/CrossPotential-AngleAngleTorsion')).attrib['M-units']).encode('utf-8')+"\n")
    f.write("!Theta: " + ((root.find('./CrossPotential/CrossPotential-AngleAngleTorsion')).attrib['Theta-units']).encode('utf-8')+"\n!\n")
    for cross in root.findall('./CrossPotential/CrossPotential-AngleAngleTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("M")))!=0 and str(cross.find("M")) != "None": 
            f.write(("%.6f" %float(cross.find("M").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta1")))!=0 and str(cross.find("Theta1")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("Theta2")))!=0 and str(cross.find("Theta2")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



# Vega: Atom Types Forms

def XMLToParamsAtomTypes(root, output_file):
    '''
    Writes XML data for Atom Types in Vega format.
    '''
    f = output_file
    f.write("MASSES\n")
    masses = []
    for atomType in root.findall('./AtomTypes/AtomType'):
        if "AtomicMass" in atomType.attrib.keys() and atomType.find("AtomType-Name").text not in masses: 
            f.write((atomType.find("AtomType-Name").text) + " " + "%.5f" %float(atomType.attrib["AtomicMass"]))
            masses.append(atomType.find("AtomType-Name").text)
            f.write("\n") 
    return


#
# XML -to- FRC output functions (.frc output format)
#

# FRC: Atom Types
def XMLtoFrcAtomTypes(root, output_file): 
    '''
    Writes XML data for Atom Types in FRC format.
    '''
    f = output_file
    f.write("#atom_types \n\n" )
    f.write("> Atom type definitions (set the mass of atom types)\n\n")
    f.write("!Type    Mass      Element  Connection   Comment\n")
    f.write("!----  ----------  -------  -----------  ----------------------------\n")
    for atomtype in root.findall('./AtomTypes/AtomType'):
        if len(str(atomtype.find("AtomType-Name")))!=0 and str(atomtype.find("AtomType-Name")) != "None":
            f.write(atomtype.find("AtomType-Name").text.ljust(7))
        else:
            f.write("".ljust(7))
        if "AtomicMass"in atomtype.attrib.keys():
            f.write(("%.3f" %float(atomtype.attrib["AtomicMass"])).rjust(6))
        else:
            f.write("".rjust(6))
        if "Element" in atomtype.attrib.keys(): 
            f.write(atomtype.attrib["Element"].rjust(8))
        else:
            f.write("".rjust(8))
        if "Connection" in atomtype.attrib.keys(): 
            f.write(atomtype.attrib["Connection"].rjust(10))
        else:
            f.write("".rjust(10))
        f.write("".rjust(10))
        if "Description" in atomtype.attrib.keys(): 
            f.write(atomtype.attrib["Description"].ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcAtomTypesCG(root, output_file):
    '''
    Writes XML data for coarse-grained Atom Types in FRC format.
    '''
    f = output_file
    f.write("#atom_types \n\n" )
    f.write("> Atom type definitions (set the mass of atom types)\n\n")
    f.write("!Name    Mass      Description \n")
    f.write("!----  ----------  ----------- \n")
    for atomtype in root.findall('./AtomTypes/AtomType-CoarseGrained/CGType'):
        if len(str(atomtype.find("CG-Name")))!=0 and str(atomtype.find("CG-Name")) != "None":
            f.write(atomtype.find("CG-Name").text.ljust(7))
        else:
            f.write("".atomtype.find("CG-Name").text.ljust(7))
        if "AtomicMass-CG"in atomtype.attrib.keys():
            f.write(("%.3f" %float(atomtype.attrib["AtomicMass-CG"])).ljust(10))
        else:
            f.write("".ljust(10))
        if "Description" in atomtype.attrib.keys(): 
            f.write(atomtype.attrib["Description"].ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



# FRC: Equivalence Table	
def XMLtoFrcEquivalenceTable(root, output_file): 
    '''
    Writes XML data for Equivalence Table in FRC format.
    '''
    f = output_file
    f.write("#\n#equivalence\n\n" )
    f.write("> Equivalence table\n\n")
    f.write("!                                 Equivalences\n")
    f.write("!                 -----------------------------------------\n")
    f.write("!Type  NonB     Bond    Angle    Torsion    OOP\n")
    f.write("!----  ----     ----    -----    -------    ----\n")
    for equivalence in root.findall('./EquivalenceTable/Equivalence-Table'):
        if len(str(equivalence.find("AtomType")))!=0 and str(equivalence.find("AtomType")) != "None":
            f.write(equivalence.find("AtomType").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(equivalence.find("NonBond")))!=0 and str(equivalence.find("NonBond")) != "None":
            f.write(equivalence.find("NonBond").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(equivalence.find("Bond")))!=0 and str(equivalence.find("Bond")) != "None": 
            f.write(equivalence.find("Bond").text.ljust(9))
        else:
            f.write("".ljust(8))
        if len(str(equivalence.find("Angle")))!=0 and str(equivalence.find("Angle")) != "None": 
            f.write(equivalence.find("Angle").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(equivalence.find("Dihedral")))!=0 and str(equivalence.find("Dihedral")) != "None": 
            f.write(equivalence.find("Dihedral").text.ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(equivalence.find("Improper")))!=0 and str(equivalence.find("Improper")) != "None": 
            f.write(equivalence.find("Improper").text.ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



# FRC: Bond Potentials Forms

def XMLtoFrcBondPotential_Harmonic(root, output_file): 
    '''
    Writes XML data for harmonic bond potential in FRC format.
    '''
    f = output_file
    f.write("#quadratic_bond\n\n" )
    f.write("> E = K*(R-R0)^2\n\n")
    f.write("!I     J      R0      K\n")
    f.write("!----  ----  -----   -------\n")
    for bond in root.findall('./BondPotential/BondPotential-Harmonic/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.4f" %float(bond.find("R0").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(bond.find("K")))!=0 and str(bond.find("K")) != "None": 
            f.write(("%.1f" %float(bond.find("K").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n") 
    return



def XMLtoFrcBondPotential_Morse(root, output_file):
    '''
    Writes XML data for Morse bond potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXXX\n\n" )
    f.write("> E = D*[(1-exp(-A(R-R0))]^2\n\n")
    f.write("!I      J    D    A    R0  \n")
    f.write("!----  ----   ----  ---  ----\n")
    for bond in root.findall('./BondPotential/BondPotential-Morse/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(bond.find("D")))!=0 and str(bond.find("D")) != "None": 
            f.write(("%.4f" %float(bond.find("D").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(bond.find("A")))!=0 and str(bond.find("A")) != "None": 
            f.write(("%.1f" %float(bond.find("A").text)).ljust(7))
        else:
            f.write("".ljust(7))        
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.1f" %float(bond.find("R0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n") 
    return



def XMLtoFrcBondPotential_Class2(root, output_file): 
    '''
    Writes XML data for Class2 bond potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = K2*(R-R0)^2+K3*(R-R0)^3+K4*(R-R0)^4\n\n")
    f.write("!I     J      K2    K3      K4    R0  \n")
    f.write("!----  ----  -----  -----  -----  -----\n")
    for bond in root.findall('./BondPotential/BondPotential-Class2/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(bond.find("K2")))!=0 and str(bond.find("K2")) != "None": 
            f.write(("%.1f" %float(bond.find("K2").text)).ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("K3")))!=0 and str(bond.find("K3")) != "None": 
            f.write(("%.1f" %float(bond.find("K3").text)).ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("K4")))!=0 and str(bond.find("K4")) != "None": 
            f.write(("%.1f" %float(bond.find("K4").text)).ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.4f" %float(bond.find("R0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcBondPotential_FENE(root, output_file): 
    '''
    Writes XML data for FENE bond potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = (-[(K*R0^2)/2]*ln[1-(R/R0)^2])\n\n")
    f.write("!I     J      R0      K\n")
    f.write("!----  ----  -----   -------\n")
    for bond in root.findall('./BondPotential/BondPotential-FENE/Bond'):
        if len(str(bond.find("AT-1")))!=0 and str(bond.find("AT-1")) != "None":
            f.write(bond.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(bond.find("AT-2")))!=0 and str(bond.find("AT-2")) != "None":
            f.write(bond.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(bond.find("R0")))!=0 and str(bond.find("R0")) != "None": 
            f.write(("%.4f" %float(bond.find("R0").text)).ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(bond.find("K")))!=0 and str(bond.find("K")) != "None": 
            f.write(("%.1f" %float(bond.find("K").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



# FRC: Angle Potentials Forms

def XMLtoFrcAnglePotential_Harmonic(root, output_file): 
    '''
    Writes XML data for harmonic angle potential in FRC format.
    '''
    f = output_file
    f.write("#quadratic_angle\n\n" )
    f.write("> E = K2 * (th - th0)^2\n\n")
    f.write("!I     J    K      th0        K2\n")
    f.write("!----  ---- ----   ------    ---------\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Harmonic/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
            f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).ljust(10))
        else: 
            f.write("".ljust(10))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.2f" %float(angle.find("Ka").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n") 
    return



def XMLtoFrcAnglePotential_COS2(root, output_file):
    '''
    Writes XML data for cosine-squared angle potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = (1/2)*Ka*[cos(Theta)-cos(Theta0)]^2\n\n")
    f.write("!I     J    K      Theta0    Ka         Comment\n")
    f.write("!----  ---- ----    ------   -----       -------\n")
    for angle in root.findall('./AnglePotential/AnglePotential-COS2/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
            f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).ljust(10))
        else: 
            f.write("".ljust(10))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.2f" %float(angle.find("Ka").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if "comment" in angle.attrib.keys():
            f.write(" " +angle.attrib["comment"].ljust(10))
        else:
            f.write("".ljust(10))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcAnglePotential_Cosine(root, output_file):
    '''
    Writes XML data for cosine angle potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = Ka*[1+cos(theta)]\n\n")
    f.write("! I     J    K     Ka    Comment\n")
    f.write("!---- ---- ----   -----  -------\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Cosine/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
            f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.2f" %float(angle.find("Ka").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if "comment" in angle.attrib.keys():
            f.write(" " +angle.attrib["comment"].ljust(10))
        else:
            f.write("".ljust(10))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcAnglePotential_CHARMM(root, output_file):
    '''
    Writes XML data for CHARMM angle potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = Ka*(Theta-Theta0)^2+Kub*(R-Rub)^2\n\n")
    f.write("!I     J    K      Theta0    Ka     Kub    Rub    Comment\n")
    f.write("!----  ---- ----    ------  -----  -----  -----   -------\n")
    for angle in root.findall('./AnglePotential/AnglePotential-CHARMM/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
            f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).ljust(10))
        else: 
            f.write("".ljust(10))
        if len(str(angle.find("Ka")))!=0 and str(angle.find("Ka")) != "None": 
            f.write(("%.2f" %float(angle.find("Ka").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(angle.find("Kub")))!=0 and str(angle.find("Kub")) != "None":
            f.write(angle.find("Kub").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(angle.find("Rub")))!=0 and str(angle.find("Rub")) != "None":
            f.write(angle.find("Rub").text.ljust(7))
        else:
            f.write("".ljust(7))
        if "comment" in angle.attrib.keys():
            f.write(" " +angle.attrib["comment"].ljust(10))
        else:
            f.write("".ljust(10))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcAnglePotential_Class2(root, output_file):
    '''
    Writes XML data for Class2 angle potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = K2*(Theta-Theta0)^2+K3*(Theta-Theta0)^3+K4*(Theta-Theta0)^4\n\n")
    f.write("!I     J    K    K2   K3   K4   Theta0 \n")
    f.write("!---- ---- ----  ---  --- ---   -------\n")
    for angle in root.findall('./AnglePotential/AnglePotential-Class2/Angle'):
        if len(str(angle.find("AT-1")))!=0 and str(angle.find("AT-1")) != "None":
            f.write(angle.find("AT-1").text.ljust(6))
        else:
            f.write("".ljust(6))
        if len(str(angle.find("AT-2")))!=0 and str(angle.find("AT-2")) != "None":
            f.write(angle.find("AT-2").text.ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("AT-3")))!=0 and str(angle.find("AT-3")) != "None":
            f.write(angle.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(angle.find("K2")))!=0 and str(angle.find("K2")) != "None": 
            f.write(("%.1f" %float(angle.find("K2").text)).ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("K3")))!=0 and str(angle.find("K3")) != "None": 
            f.write(("%.1f" %float(angle.find("K3").text)).ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("K4")))!=0 and str(angle.find("K4")) != "None": 
            f.write(("%.1f" %float(angle.find("K4").text)).ljust(5))
        else:
            f.write("".ljust(5))
        if len(str(angle.find("Theta0")))!=0 and str(angle.find("Theta0")) != "None": 
            f.write(("%.2f" %float(angle.find("Theta0").text)).ljust(10))
        else: 
            f.write("".ljust(10))
        f.write("\n")
    f.write("\n")
    return
	


# FRC: Improper Potentials Forms

def XMLtoFrcImproperPotential_CHARMM(root, output_file): 
    '''
    Writes XML data for CHARMM improper potential in FRC format.
    '''
    f = output_file
    f.write("#out_of_plane\n\n" )
    f.write("> E = Kd*[1+cos(n*Phi+Phi0)]\n\n")
    f.write("!I      J      K      L        Kd        N       Phi0\n")
    f.write("!-----  -----  -----  -----   -------   --------- -------\n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-CHARMM/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Kd")))!=0 and str(improper.find("Kd")) != "None": 
            f.write(("%.6f" %float(improper.find("Kd").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("N")))!=0 and str(improper.find("N")) != "None": 
            f.write(("%.1f" %float(improper.find("N").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("Phi0")))!=0 and str(improper.find("Phi0")) != "None": 
            f.write(("%.1f" %float(improper.find("Phi0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcImproperPotential_FourierSimple(root, output_file):
    '''
    Writes XML data for Fourier simple improper potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXXX\n\n" )
    f.write("> E = Ki*[C0+C1*cos(w)+C2*cos(2*w)]\n\n")
    f.write("!I      J      K      L      Ki      C0    C1    C2     \n")
    f.write("!-----  -----  -----  -----   -----   ----  ----   ----    \n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-FourierSimple/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("C0")))!=0 and str(improper.find("C0")) != "None": 
            f.write(("%.4f" %float(improper.find("C0").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("C1")))!=0 and str(improper.find("C1")) != "None": 
            f.write(("%.4f" %float(improper.find("C1").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("C2")))!=0 and str(improper.find("C2")) != "None": 
            f.write(("%.4f" %float(improper.find("C2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcImproperPotential_Class2(root, output_file): 
    '''
    Writes XML data for Class2 improper potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXX\n\n" )
    f.write("> E = Ki*(Chi-Chi0)^2\n\n")
    f.write("!Ki units: " + ((root.find('./ImproperPotential/ImproperPotential-Class2')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!Chi0 units: " + ((root.find('./ImproperPotential/ImproperPotential-Class2')).attrib['Chi0-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        Ki       Chi0\n")
    f.write("!-----  -----  -----  -----   -------   -------\n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-Class2/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("Chi0")))!=0 and str(improper.find("Chi0")) != "None": 
            f.write(("%.1f" %float(improper.find("Chi0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcImproperPotential_COS2(root, output_file): 
    '''
    Writes XML data for cosine-squared improper potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXX\n\n" )
    f.write("> E = Ki*cos(Chi-Chi0)^2\n\n")
    f.write("!Ki units: " + ((root.find('./ImproperPotential/ImproperPotential-COS2')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!Chi0 units: " + ((root.find('./ImproperPotential/ImproperPotential-COS2')).attrib['Chi0-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        Ki       Chi0\n")
    f.write("!-----  -----  -----  -----   -------   -------\n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-COS2/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("Chi0")))!=0 and str(improper.find("Chi0")) != "None": 
            f.write(("%.1f" %float(improper.find("Chi0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcImproperPotential_CVFF(root, output_file): 
    '''
    Writes XML data for CVFF improper potential in FRC format.
    '''
    f = output_file
    f.write("#out_of_plane\n\n" )
    f.write("> E = Ki*[1+Ns*cos(N*Phi)]\n\n")
    f.write("!Ki units: " + ((root.find('./ImproperPotential/ImproperPotential-CVFF')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        Ki        Ns     N \n")
    f.write("!-----  -----  -----  -----   -------   ---    ---\n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-CVFF/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("Ns")))!=0 and str(improper.find("Ns")) != "None": 
            f.write(("%.1f" %float(improper.find("Ns").text)).ljust(2))
        else:
            f.write("".ljust(2))
        if len(str(improper.find("N")))!=0 and str(improper.find("N")) != "None": 
            f.write(("%.1f" %float(improper.find("N").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcImproperPotential_Fourier(root, output_file):
    '''
    Writes XML data for Fourier improper potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXXX\n\n" )
    f.write("> E = Ki*[C0+C1*cos(w)+C2*cos(2*w)]\n\n")
    f.write("!I      J      K      L      Ki      C0    C1    C2     \n")
    f.write("!-----  -----  -----  -----   -----   ----  ----   ----    \n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-Fourier/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("C0")))!=0 and str(improper.find("C0")) != "None": 
            f.write(("%.4f" %float(improper.find("C0").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("C1")))!=0 and str(improper.find("C1")) != "None": 
            f.write(("%.4f" %float(improper.find("C1").text)).ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(improper.find("C2")))!=0 and str(improper.find("C2")) != "None": 
            f.write(("%.4f" %float(improper.find("C2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcImproperPotential_Harmonic(root, output_file): 
    '''
    Writes XML data for harmonic improper potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXX\n\n" )
    f.write("> E = Ki*(Chi-Chi0)^2\n\n")
    f.write("!Ki units: " + ((root.find('./ImproperPotential/ImproperPotential-Harmonic')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!Chi0 units: " + ((root.find('./ImproperPotential/ImproperPotential-Harmonic')).attrib['Chi0-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        Ki       Chi0\n")
    f.write("!-----  -----  -----  -----   -------   -------\n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-Harmonic/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("Chi0")))!=0 and str(improper.find("Chi0")) != "None": 
            f.write(("%.1f" %float(improper.find("Chi0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcImproperPotential_Umbrella(root, output_file): 
    '''
    Writes XML data for Umbrella improper potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXX\n\n" )
    f.write("> E = 0.5*K*[{1+cos(w0)}/sin(w0)]^2*[cos(w)-cos(w0)] ~ w0 ≠ 0° <> K*[1-cos(w)] ~ w0 = 0°\n\n")
    f.write("!Ki units: " + ((root.find('./ImproperPotential/ImproperPotential-Umbrella')).attrib['Ki-units']).encode('utf-8')+"\n")
    f.write("!w0 units: " + ((root.find('./ImproperPotential/ImproperPotential-Umbrella')).attrib['w0-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        Ki       w0\n")
    f.write("!-----  -----  -----  -----   -------   -------\n")
    for improper in root.findall('./ImproperPotential/ImproperPotential-Umbrella/Improper'):
        if len(str(improper.find("AT-1")))!=0 and str(improper.find("AT-1")) != "None":
            f.write(improper.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-2")))!=0 and str(improper.find("AT-2")) != "None":
            f.write(improper.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-3")))!=0 and str(improper.find("AT-3")) != "None":
                f.write(improper.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(improper.find("AT-4")))!=0 and str(improper.find("AT-4")) != "None":
            f.write(improper.find("AT-4").text.ljust(8))
        else:
            f.write("".ljust(8))
        if len(str(improper.find("Ki")))!=0 and str(improper.find("Ki")) != "None": 
            f.write(("%.6f" %float(improper.find("Ki").text)).ljust(13))
        else:
            f.write("".ljust(13))
        if len(str(improper.find("w0")))!=0 and str(improper.find("w0")) != "None": 
            f.write(("%.1f" %float(improper.find("w0").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



# FRC: Dihedral Potentials Forms

def XMLtoFrcDihedralPotential_FourierSimple(root, output_file):
    '''
    Writes XML data for Fourier simple dihedral potential in FRC format.
    '''
    f = output_file
    f.write("##torsion_4\n\n" )
    f.write("> E = K1*[1+cos(Phi)] + K2*[1+cos(2*Phi)] + K3*[1+cos(3*Phi)] + K4*[1+cos(4*Phi)]\n\n")
    f.write("!I      J      K      L        K1         K2         K3         K4        K5\n")
    f.write("!-----  -----  -----  -----   --------   --------   --------   --------   --------\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-FourierSimple/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K1").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K2").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K3").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("K4")))!=0 and str(dihedral.find("K4")) != "None" : 
            f.write(("%.6f" %float(dihedral.find("K4").text)).rjust(11))
        else:
            f.write("".rjust(11)) 
        if len(str(dihedral.find("K5")))!=0 and str(dihedral.find("K5")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K5").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcDihedralPotential_Fourier(root, output_file):
    '''
    Writes XML data for Fourier dihedral potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = K1*[1+cos(N1*Phi-D1)]+K2*[1+cos(N2*Phi-D2)]+K3*[1+cos(N3*Phi-D3)]+K4*[1+cos(N4*Phi-D4)]+K5*[1+cos(N5*Phi-D5)]\n\n")
    f.write("!Kn units: " + ((root.find('./DihedralPotential/DihedralPotential-Fourier')).attrib['Kn-units']).encode('utf-8')+"\n!\n")
    f.write("!Dn units: " + ((root.find('./DihedralPotential/DihedralPotential-Fourier')).attrib['Dn-units']).encode('utf-8')+"\n!\n")
    f.write("!I      J      K      L        K1         N1         D1         K2        N2       D2         K3         N3         D3        K4       N4       D4        K5       N5       D5   \n")
    f.write("!-----  -----  -----  -----   --------   --------   --------   --------  ------   ------    --------   --------   --------  -------  -------  -------  --------  -------  -------\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Fourier/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K1").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N1")))!=0 and str(dihedral.find("N1")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N1").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D1")))!=0 and str(dihedral.find("D1")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D1").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K2").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N2")))!=0 and str(dihedral.find("N2")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N2").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D2")))!=0 and str(dihedral.find("D2")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D2").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K3").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N3")))!=0 and str(dihedral.find("N3")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N3").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D3")))!=0 and str(dihedral.find("D3")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D3").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K4")))!=0 and str(dihedral.find("K4")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K4").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N4")))!=0 and str(dihedral.find("N4")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N4").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D4")))!=0 and str(dihedral.find("D4")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D4").text)).rjust(10))
        else:
            f.write("".rjust(10))
        if len(str(dihedral.find("K5")))!=0 and str(dihedral.find("K5")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K5").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("N5")))!=0 and str(dihedral.find("N5")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N5").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("D5")))!=0 and str(dihedral.find("D5")) != "None": 
            f.write(("%.2f" %float(dihedral.find("D5").text)).rjust(10))
        else:
            f.write("".rjust(10))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcDihedralPotential_CHARMM(root, output_file):
    '''
    Writes XML data for CHARMM dihedral potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = Kd*[1+cos(N*Phi-Phi0)]\n\n")
    f.write("!I      J      K      L        Kd         N         Phi0  \n")
    f.write("!-----  -----  -----  -----   --------   --------   ------  \n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-CHARMM/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("Kd")))!=0 and str(dihedral.find("Kd")) != "None": 
            f.write(("%.6f" %float(dihedral.find("Kd").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K2").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("N")))!=0 and str(dihedral.find("N")) != "None": 
            f.write(("%.1f" %float(dihedral.find("N").text)).rjust(5))
        else:
            f.write("".rjust(5))
        if len(str(dihedral.find("Phi0")))!=0 and str(dihedral.find("Phi0")) != "None" : 
            f.write(("%.6f" %float(dihedral.find("Phi0").text)).rjust(0))
        else:
            f.write("".rjust(0)) 
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcDihedralPotential_Harmonic(root, output_file):
    '''
    Writes XML data for harmonic dihedral potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = Kd*[1+Ns*cos(N*Phi)]\n\n")
    f.write("!Kd units: " + ((root.find('./DihedralPotential/DihedralPotential-Harmonic')).attrib['Kd-units']).encode('utf-8')+"\n")
    f.write("!N: multiplicity\n")
    f.write("!I      J      K      L        Kd         Ns         N  \n")
    f.write("!-----  -----  -----  -----   --------   --------   -----\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Harmonic/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("Kd")))!=0 and str(dihedral.find("Kd")) != "None": 
            f.write(("%.6f" %float(dihedral.find("Kd").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("Ns")))!=0 and str(dihedral.find("Ns")) != "None": 
            f.write(("%.6f" %float(dihedral.find("Ns").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("N")))!=0 and str(dihedral.find("N")) != "None": 
            f.write(("%.6f" %float(dihedral.find("N").text)).rjust(5))
        else:
            f.write("".rjust(5)) 
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcDihedralPotential_Class2(root, output_file):
    '''
    Writes XML data for Class2 dihedral potential in FRC format.
    '''
    f = output_file
    f.write("##XXXXXX\n\n" )
    f.write("> E = K1*[1-cos(Phi-Phi1)]+K2*[1-cos(2*Phi-Phi2)]+K3*[1-cos(3*Phi-Phi3)]\n\n")
    f.write("!Kn units: " + ((root.find('./DihedralPotential/DihedralPotential-Class2')).attrib['Kn-units']).encode('utf-8')+"\n")
    f.write("!Phin units: " + ((root.find('./DihedralPotential/DihedralPotential-Class2')).attrib['Phin-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        K1         K2         K3         Phi1        Phi2      Phi3  \n")
    f.write("!-----  -----  -----  -----   --------   --------   --------   --------   --------   -------\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Class2/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K1").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K2").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K3").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("Phi1")))!=0 and str(dihedral.find("Phi1")) != "None" : 
            f.write(("%.6f" %float(dihedral.find("Phi1").text)).rjust(11))
        else:
            f.write("".rjust(11)) 
        if len(str(dihedral.find("Phi2")))!=0 and str(dihedral.find("Phi2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("Phi2").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("Phi3")))!=0 and str(dihedral.find("Phi3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("Phi3").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcDihedralPotential_OPLS(root, output_file):
    '''
    Writes XML data for OPLS dihedral potential in FRC format.
    '''
    f = output_file
    f.write("##XXXXXX\n\n" )
    f.write("> E = 0.5*{K1*[1+cos(Phi)]+K2*[1-cos(2*Phi)]+K3*[1+cos(3*Phi)]+K4*[1-cos(4*Phi)]}\n\n")
    f.write("!Kn: " + ((root.find('./DihedralPotential/DihedralPotential-OPLS')).attrib['Kn-units']).encode('utf-8')+"\n!\n")
    f.write("!I      J      K      L        K1         K2         K3         K4        \n")
    f.write("!-----  -----  -----  -----   --------   --------   --------   --------   \n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-OPLS/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("K1")))!=0 and str(dihedral.find("K1")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K1").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("K2")))!=0 and str(dihedral.find("K2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K2").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("K3")))!=0 and str(dihedral.find("K3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("K3").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("K4")))!=0 and str(dihedral.find("K4")) != "None" : 
            f.write(("%.6f" %float(dihedral.find("K4").text)).rjust(11))
        else:
            f.write("".rjust(11)) 
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcDihedralPotential_Quadratic(root, output_file):
    '''
    Writes XML data for quadratic dihedral potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("> E = Kd*(Phi-Phi0)^2\n\n")
    f.write("!Kd units: " + ((root.find('./DihedralPotential/DihedralPotential-Quadratic')).attrib['Kd-units']).encode('utf-8')+"\n")
    f.write("!Phi0 units: " + ((root.find('./DihedralPotential/DihedralPotential-Quadratic')).attrib['Phi0-units']).encode('utf-8')+"\n!\n")
    f.write("!I      J      K      L        Kd          Phi0  \n")
    f.write("!-----  -----  -----  -----   --------    ------  \n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Quadratic/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("Kd")))!=0 and str(dihedral.find("Kd")) != "None": 
            f.write(("%.6f" %float(dihedral.find("Kd").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("Phi0")))!=0 and str(dihedral.find("Phi0")) != "None" : 
            f.write(("%.6f" %float(dihedral.find("Phi0").text)).rjust(0))
        else:
            f.write("".rjust(0)) 
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcDihedralPotential_Multiharmonic(root, output_file):
    '''
    Writes XML data for Multiharmonic dihedral potential in FRC format.
    '''
    f = output_file
    f.write("##XXXXXXX\n\n" )
    f.write("> E = A1+A2*cos(Phi)+A3*cos^2(Phi)+A4*cos^3(Phi)+A5*cos^4(Phi)\n\n")
    f.write("!I      J      K      L        A1         A2         A3         A4        A5\n")
    f.write("!-----  -----  -----  -----   --------   --------   --------    -------   --------\n")
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Multiharmonic/Dihedral'):
        if len(str(dihedral.find("AT-1")))!=0 and str(dihedral.find("AT-1")) != "None":
            f.write(dihedral.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-2")))!=0 and str(dihedral.find("AT-2")) != "None":
            f.write(dihedral.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-3")))!=0 and str(dihedral.find("AT-3")) != "None":
            f.write(dihedral.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("AT-4")))!=0 and str(dihedral.find("AT-4")) != "None":
            f.write(dihedral.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(dihedral.find("A1")))!=0 and str(dihedral.find("A1")) != "None": 
            f.write(("%.6f" %float(dihedral.find("A1").text)).rjust(9))
        else:
            f.write("".rjust(9))
        if len(str(dihedral.find("A2")))!=0 and str(dihedral.find("A2")) != "None": 
            f.write(("%.6f" %float(dihedral.find("A2").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("A3")))!=0 and str(dihedral.find("A3")) != "None": 
            f.write(("%.6f" %float(dihedral.find("A3").text)).rjust(11))
        else:
            f.write("".rjust(11))
        if len(str(dihedral.find("A4")))!=0 and str(dihedral.find("A4")) != "None" : 
            f.write(("%.6f" %float(dihedral.find("A4").text)).rjust(11))
        else:
            f.write("".rjust(11)) 
        if len(str(dihedral.find("A5")))!=0 and str(dihedral.find("A5")) != "None": 
            f.write(("%.6f" %float(dihedral.find("A5").text)).rjust(11))
        else:
            f.write("".rjust(11))
        f.write("\n")
    f.write("\n")
    return



# FRC: Non-Bonded Potentials Forms

def XMLtoFrcNonBondPotential_LJ(root, output_file):
    '''
    Writes XML data for LJ non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#nonbond(12-6)\n\n" )
    f.write("@type r-eps\n@combination geometric\n\n" )
    f.write("> E = 4*eps((sigma/r)^12 - (sigma/r)^6)\n\n")
    f.write("epsilon units: " + ((root.find('./NonBondPotential/NonBondPotential-LJ')).attrib['epsilon-units']).encode('utf-8')+"\n")
    f.write("sigma units: " + ((root.find('./NonBondPotential/NonBondPotential-LJ')).attrib['sigma-units']).encode('utf-8')+"\n")
    f.write("!I        sigma       eps       \n")
    f.write("!----    ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBond-LJ/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write(nonbond.find("AtomType").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcNonBondPotential_LJ96(root, output_file):
    '''
    Writes XML data for LJ96 non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type XXXXX\n\n" )
    f.write("> E = epsilon*[2*(sigma/R)^9-3*(sigma/R)^6]\n\n")
    f.write("!I        sigma       eps       \n")
    f.write("!----    ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ96/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write(nonbond.find("AtomType").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcNonBondPotential_LJ2(root, output_file):
    '''
    Writes XML data for LJ2 non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type XXXXXXX\n\n" )
    f.write("> E = 4*epsilon*[(sigma/R)^12-(sigma/R)^6]\n\n")
    f.write("!I    J       epsilon       sigma       \n")
    f.write("!---- ----   ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ2/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToFrcNonBondPotential_LJ_Rmin(root, output_file):
    '''
    Writes XML data for LJ-Rmin non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type ??\n\n" )
    f.write("> E = epsilon*[(Rmin/R)^12-2*(Rmin/R)^6]\n\n")
    f.write("!I        sigma       eps       \n")
    f.write("!----    ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ-Rmin/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write(nonbond.find("AtomType").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToFrcNonBondPotential_LJ_AB(root, output_file):
    '''
    Writes XML data for LJ-AB non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type ??\n\n" )
    f.write("> E = A/(R^12)-B/(R^6)\n\n")
    f.write("!I           A          B       \n")
    f.write("!----    ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ-AB/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write(nonbond.find("AtomType").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("A")))!=0 and str(nonbond.find("A")) != "None":
            f.write(("%.6f" %float(nonbond.find("A").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("B")))!=0 and str(nonbond.find("B")) != "None": 
            f.write(("%.6f" %float(nonbond.find("B").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToFrcNonBondPotential_LJ2_AB(root, output_file):
    '''
    Writes XML data for LJ2-AB non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type ??\n\n" )
    f.write("> E = A/(R^12)-B/(R^6)\n\n")
    f.write("!I     J         A          B       \n")
    f.write("!----  ----  ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ2-AB/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("A")))!=0 and str(nonbond.find("A")) != "None":
            f.write(("%.6f" %float(nonbond.find("A").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("B")))!=0 and str(nonbond.find("B")) != "None": 
            f.write(("%.6f" %float(nonbond.find("B").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToFrcNonBondPotential_Class2(root, output_file):
    '''
    Writes XML data for Class2 non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type ??\n\n" )
    f.write("> E = epsilon*[(Rmin/R)^12-2*(Rmin/R)^6]\n\n")
    f.write("!I        sigma       eps       \n")
    f.write("!----    ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Class2/NonBond'):
        if len(str(nonbond.find("AtomType")))!=0 and str(nonbond.find("AtomType")) != "None":
            f.write(nonbond.find("AtomType").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcNonBondPotential_EnergyRenorm(root, output_file):
    '''
    Writes XML data for Energy-Renormalization non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type XXXXXXX\n\n" )
    f.write("> E = [epsilon_g+[(epsilon_A-epsilon_g)/(1+exp(-k_sig*(T-T_sig)))]]*[((sigma*(a*T+b))/R)^12-((sigma*(a*T+b))/R)^6]\n\n")
    f.write("!I    J      epsilon_g  epsilon_A     sigma      a       b       k_sig        T-sig       \n")
    f.write("!---- ----   ---------  ---------    -------   ------  ------   -------      --------     \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-EnergyRenorm/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon_g")))!=0 and str(nonbond.find("epsilon_g")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon_g").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon_A")))!=0 and str(nonbond.find("epsilon_A")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon_A").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("a")))!=0 and str(nonbond.find("a")) != "None":
            f.write(("%.3f" %float(nonbond.find("a").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("b")))!=0 and str(nonbond.find("b")) != "None":
            f.write(("%.3f" %float(nonbond.find("b").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("k_sig")))!=0 and str(nonbond.find("k_sig")) != "None":
            f.write(("%.3f" %float(nonbond.find("k_sig").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("T_sig")))!=0 and str(nonbond.find("T_sig")) != "None":
            f.write(("%.3f" %float(nonbond.find("T_sig").text)).ljust(0))
        else:
            f.write("".ljust(0))			
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcNonBondPotential_Mie(root, output_file):
    '''
    Writes XML data for LJ-Mie non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type XXXXXXX\n\n" )
    f.write("> E = C*epsilon*[(sigma/R)^m_rep-(sigma/R)^n_att]\n\n")
    f.write("epsilon units: " + ((root.find('./NonBondPotential/NonBondPotential-Mie')).attrib['epsilon-units']).encode('utf-8')+"\n")
    f.write("sigma units: " + ((root.find('./NonBondPotential/NonBondPotential-Mie')).attrib['sigma-units']).encode('utf-8')+"\n")
    f.write("!I      J      C       epsilon     sigma      m_rep     n_att   \n")
    f.write("!---- ----  -------   ---------   -------     ------    ------  \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Mie/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("C")))!=0 and str(nonbond.find("C")) != "None":
            f.write(("%.6f" %float(nonbond.find("C").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("m_rep")))!=0 and str(nonbond.find("m_rep")) != "None":
            f.write(("%.3f" %float(nonbond.find("m_rep").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("n_att")))!=0 and str(nonbond.find("n_att")) != "None":
            f.write(("%.3f" %float(nonbond.find("n_att").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcNonBondPotential_Soft(root, output_file):
    '''
    Writes XML data for Soft non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type XXXXXXX\n\n" )
    f.write("> E = a_ij*[1+cos(pi*r/r_c)]\n\n")
    f.write("a_ij units: " + ((root.find('./NonBondPotential/NonBondPotential-Soft')).attrib['a_ij-units']).encode('utf-8')+"\n")
    f.write("r_c units: " + ((root.find('./NonBondPotential/NonBondPotential-Soft')).attrib['r_c-units']).encode('utf-8')+"\n")
    f.write("!I    J         a_ij       r_c       \n")
    f.write("!---- ----   ---------  ---------   \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Soft/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("a_ij")))!=0 and str(nonbond.find("a_ij")) != "None": 
            f.write(("%.6f" %float(nonbond.find("a_ij").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("r_c")))!=0 and str(nonbond.find("r_c")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_c").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToFrcNonBondPotential_Weeks_Chandler_Anderson(root, output_file):
    '''
    Writes XML data for LJ-WCA non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type ??\n\n" )
    f.write("> E = 4*epsilon*[((sigma/R)^-12)-((sigma/R)^-6)+(1/4)]\n\n")
    f.write("epsilon units: " + ((root.find('./NonBondPotential/NonBondPotential-Weeks-Chandler-Anderson')).attrib['epsilon-units']).encode('utf-8')+"\n")
    f.write("sigma units: " + ((root.find('./NonBondPotential/NonBondPotential-Weeks-Chandler-Anderson')).attrib['sigma-units']).encode('utf-8')+"\n")
    f.write("!I     J      epsilon    sigma     r_cut  \n")
    f.write("!----  ----  ---------  ---------  ------- \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-Weeks-Chandler-Anderson/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("r_cut")))!=0 and str(nonbond.find("r_cut")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_cut").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLToFrcNonBondPotential_LJ_GROMACS(root, output_file):
    '''
    Writes XML data for LJ-Gromacs non-bonded potential in FRC format.
    '''
    f = output_file
    f.write("#XXXXXX\n\n" )
    f.write("@type ??\n\n" )
    f.write("> E = 4*epsilon*[(sigma/R)^12-(sigma/R)^6] + S_LJ(R)\n\n")
    f.write("epsilon units: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-GROMACS')).attrib['epsilon-units']).encode('utf-8')+"\n")
    f.write("sigma units: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-GROMACS')).attrib['sigma-units']).encode('utf-8')+"\n")
    f.write("r units: " + ((root.find('./NonBondPotential/NonBondPotential-LJ-GROMACS')).attrib['r-units']).encode('utf-8')+"\n")
    f.write("!I     J      epsilon    sigma     r_1     r_cut  \n")
    f.write("!----  ----  ---------  ---------  ------  ------ \n")
    for nonbond in root.findall('./NonBondPotential/NonBondPotential-LJ-GROMACS/NonBond'):
        if len(str(nonbond.find("AT-1")))!=0 and str(nonbond.find("AT-1")) != "None":
            f.write(nonbond.find("AT-1").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("AT-2")))!=0 and str(nonbond.find("AT-2")) != "None":
            f.write(nonbond.find("AT-2").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(nonbond.find("epsilon")))!=0 and str(nonbond.find("epsilon")) != "None": 
            f.write(("%.6f" %float(nonbond.find("epsilon").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(nonbond.find("sigma")))!=0 and str(nonbond.find("sigma")) != "None":
            f.write(("%.3f" %float(nonbond.find("sigma").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("r_1")))!=0 and str(nonbond.find("r_1")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(nonbond.find("r_cut")))!=0 and str(nonbond.find("r_cut")) != "None":
            f.write(("%.3f" %float(nonbond.find("r_cut").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return


	
# FRC: Cross Potentials Forms

def XMLtoFrcCrossPotential_BondBond(root, output_file):
    '''
    Writes XML data for Bond-Bond cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = M*(R-R1)*(R-R2)\n\n")
    f.write("M units: " + ((root.find('./CrossPotential/CrossPotential-BondBond')).attrib['M-units']).encode('utf-8')+"\n")
    f.write("Ri units: " + ((root.find('./CrossPotential/CrossPotential-BondBond')).attrib['Ri-units']).encode('utf-8')+"\n")
    f.write("!I      J      K        M      R1     R2  \n")
    f.write("!----  ----   ----  --------  -----  -----\n")
    for cross in root.findall('./CrossPotential/CrossPotential-BondBond/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("M")))!=0 and str(cross.find("M")) != "None": 
            f.write(("%.6f" %float(cross.find("M").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R2")))!=0 and str(cross.find("R2")) != "None": 
            f.write(("%.3f" %float(cross.find("R2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return 



def XMLtoFrcCrossPotential_BondBond13(root, output_file):
    '''
    Writes XML data for Bond-Bond13 cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = N*(Rij-R1)*(Rkl-R3)\n\n")
    f.write("N units: " + ((root.find('./CrossPotential/CrossPotential-BondBond13')).attrib['N-units']).encode('utf-8')+"\n")
    f.write("Ri units: " + ((root.find('./CrossPotential/CrossPotential-BondBond13')).attrib['Ri-units']).encode('utf-8')+"\n")
    f.write("!I      J      K        N      R1     R3  \n")
    f.write("!----  ----   ----  --------  -----  -----\n")
    for cross in root.findall('./CrossPotential/CrossPotential-BondBond13/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("N")))!=0 and str(cross.find("N")) != "None": 
            f.write(("%.6f" %float(cross.find("N").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R3")))!=0 and str(cross.find("R3")) != "None": 
            f.write(("%.3f" %float(cross.find("R3").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcCrossPotential_AngleAngle(root, output_file):
    '''
    Writes XML data for Angle-Angle cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = M1*(Theta-Theta1)(Theta-Theta3)+M2*(Theta-Theta1)(Theta-Theta2)+M3*(Theta-Theta2)(Theta-Theta3)\n\n")
    f.write("M units: " + ((root.find('./CrossPotential/CrossPotential-AngleAngle')).attrib['M-units']).encode('utf-8')+"\n")
    f.write("Theta units: " + ((root.find('./CrossPotential/CrossPotential-AngleAngle')).attrib['Theta-units']).encode('utf-8')+"\n")
    f.write("!I      J      K     L     M1       M2      M3      Theta1       Theta2       Theta3   \n")
    f.write("!---- ----   ----  ----  ------  -------  -------  ---------   ---------     --------- \n")
    for cross in root.findall('./CrossPotential/CrossPotential-AngleAngle/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("M1")))!=0 and str(cross.find("M1")) != "None": 
            f.write(("%.6f" %float(cross.find("M1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("M2")))!=0 and str(cross.find("M2")) != "None": 
            f.write(("%.6f" %float(cross.find("M2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("M3")))!=0 and str(cross.find("M3")) != "None": 
            f.write(("%.6f" %float(cross.find("M3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta1")))!=0 and str(cross.find("Theta1")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta2")))!=0 and str(cross.find("Theta2")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta3")))!=0 and str(cross.find("Theta3")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta3").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcCrossPotential_BondAngle(root, output_file):
    '''
    Writes XML data for Bond-Angle cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = N1*(R-R1)*(Theta-Theta0)+N2*(R-R2)*(Theta-Theta0)\n\n")
    f.write("N units: " + ((root.find('./CrossPotential/CrossPotential-BondAngle')).attrib['N-units']).encode('utf-8')+"\n")
    f.write("Ri units: " + ((root.find('./CrossPotential/CrossPotential-BondAngle')).attrib['Ri-units']).encode('utf-8')+"\n")
    f.write("Theta0 units: " + ((root.find('./CrossPotential/CrossPotential-BondAngle')).attrib['Theta0-units']).encode('utf-8')+"\n")
    f.write("!I      J      K        Theta0      N1       N2       R1     R2   \n")
    f.write("!----  ----   ----     --------  -------   -------   ----   ----   \n")
    for cross in root.findall('./CrossPotential/CrossPotential-BondAngle/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("Theta0")))!=0 and str(cross.find("Theta0")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta0").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("N1")))!=0 and str(cross.find("N1")) != "None": 
            f.write(("%.6f" %float(cross.find("N1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("N2")))!=0 and str(cross.find("N2")) != "None": 
            f.write(("%.6f" %float(cross.find("N2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R2")))!=0 and str(cross.find("R2")) != "None": 
            f.write(("%.3f" %float(cross.find("R2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcCrossPotential_MiddleBondTorsion(root, output_file):
    '''
    Writes XML data for Middle-Bond Torsion cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = (R-R2)*[A1*cos(Phi)+A2*cos(2*Phi)+A3*cos(3*Phi)]\n\n")
    f.write("A units: " + ((root.find('./CrossPotential/CrossPotential-MiddleBondTorsion')).attrib['A-units']).encode('utf-8')+"\n")
    f.write("R units: " + ((root.find('./CrossPotential/CrossPotential-MiddleBondTorsion')).attrib['R-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        A1       A2        A3      R2   \n")
    f.write("!----  ----   ----   ----    ------   -------  -------   ----   \n")
    for cross in root.findall('./CrossPotential/CrossPotential-MiddleBondTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("A1")))!=0 and str(cross.find("A1")) != "None": 
            f.write(("%.6f" %float(cross.find("A1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("A2")))!=0 and str(cross.find("A2")) != "None": 
            f.write(("%.6f" %float(cross.find("A2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("A3")))!=0 and str(cross.find("A3")) != "None": 
            f.write(("%.6f" %float(cross.find("A3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R2")))!=0 and str(cross.find("R2")) != "None": 
            f.write(("%.3f" %float(cross.find("R2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcCrossPotential_EndBondTorsion(root, output_file):
    '''
    Writes XML data for End-Bond Torsion cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = (R-R1)*[B1*cos(Phi)+B2*cos(2*Phi)+B3*cos(3*Phi)]+(R-R3)*[C1*cos(Phi)+C2*cos(2*Phi)+C3*cos(3*Phi)]\n\n")
    f.write("B units: " + ((root.find('./CrossPotential/CrossPotential-EndBondTorsion')).attrib['B-units']).encode('utf-8')+"\n")
    f.write("C units: " + ((root.find('./CrossPotential/CrossPotential-EndBondTorsion')).attrib['C-units']).encode('utf-8')+"\n")
    f.write("R units: " + ((root.find('./CrossPotential/CrossPotential-EndBondTorsion')).attrib['R-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        B1       B2        B3        C1        C2        C3         R1      R3   \n")
    f.write("!----  ----   ----   ----   --------   -------  -------   --------   --------  --------  ------   ------ \n")
    for cross in root.findall('./CrossPotential/CrossPotential-EndBondTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("B1")))!=0 and str(cross.find("B1")) != "None": 
            f.write(("%.6f" %float(cross.find("B1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("B2")))!=0 and str(cross.find("B2")) != "None": 
            f.write(("%.6f" %float(cross.find("B2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("B3")))!=0 and str(cross.find("B3")) != "None": 
            f.write(("%.6f" %float(cross.find("B3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("C1")))!=0 and str(cross.find("C1")) != "None": 
            f.write(("%.6f" %float(cross.find("C1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("C2")))!=0 and str(cross.find("C2")) != "None": 
            f.write(("%.6f" %float(cross.find("C2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("C3")))!=0 and str(cross.find("C3")) != "None": 
            f.write(("%.6f" %float(cross.find("C3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("R1")))!=0 and str(cross.find("R1")) != "None": 
            f.write(("%.3f" %float(cross.find("R1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("R3")))!=0 and str(cross.find("R3")) != "None": 
            f.write(("%.3f" %float(cross.find("R3").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcCrossPotential_AngleTorsion(root, output_file):
    '''
    Writes XML data for Bond-Bond cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = (Theta-Theta1)*[D1*cos(Phi)+D2*cos(2*Phi)+D3*cos(3*Phi)]+(Theta-Theta2)*[E1*cos(Phi)+E2*cos(2*Phi)+E3*cos(3*Phi)]\n\n")
    f.write("D units: " + ((root.find('./CrossPotential/CrossPotential-AngleTorsion')).attrib['D-units']).encode('utf-8')+"\n")
    f.write("E units: " + ((root.find('./CrossPotential/CrossPotential-AngleTorsion')).attrib['E-units']).encode('utf-8')+"\n")
    f.write("Theta units: " + ((root.find('./CrossPotential/CrossPotential-AngleTorsion')).attrib['Theta-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        D1       D2        D3        E1         E2        E3       Theta1   Theta2  \n")
    f.write("!----  ----   ----   ----   --------   -------  -------   --------   --------  --------   ------   ------ \n")
    for cross in root.findall('./CrossPotential/CrossPotential-AngleTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("D1")))!=0 and str(cross.find("D1")) != "None": 
            f.write(("%.6f" %float(cross.find("D1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("D2")))!=0 and str(cross.find("D2")) != "None": 
            f.write(("%.6f" %float(cross.find("D2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("D3")))!=0 and str(cross.find("D3")) != "None": 
            f.write(("%.6f" %float(cross.find("D3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("E1")))!=0 and str(cross.find("E1")) != "None": 
            f.write(("%.6f" %float(cross.find("E1").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("E2")))!=0 and str(cross.find("E2")) != "None": 
            f.write(("%.6f" %float(cross.find("E2").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("E3")))!=0 and str(cross.find("E3")) != "None": 
            f.write(("%.6f" %float(cross.find("E3").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta1")))!=0 and str(cross.find("Theta1")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("Theta2")))!=0 and str(cross.find("Theta2")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return



def XMLtoFrcCrossPotential_AngleAngleTorsion(root, output_file):
    '''
    Writes XML data for Angle-Angle Torsion cross potential in FRC format.
    '''
    f = output_file
    f.write("XXXXXX\n\n")
    f.write("> E = M(Theta-Theta1)*(Theta-Theta2)*cos(Phi)\n\n")
    f.write("M units: " + ((root.find('./CrossPotential/CrossPotential-AngleAngleTorsion')).attrib['M-units']).encode('utf-8')+"\n")
    f.write("Theta units: " + ((root.find('./CrossPotential/CrossPotential-AngleAngleTorsion')).attrib['Theta-units']).encode('utf-8')+"\n")
    f.write("!I      J      K      L        M       Theta1   Theta2  \n")
    f.write("!----  ----   ----   ----   --------   ------   ------ \n")
    for cross in root.findall('./CrossPotential/CrossPotential-AngleAngleTorsion/Cross'):
        if len(str(cross.find("AT-1")))!=0 and str(cross.find("AT-1")) != "None":
            f.write(cross.find("AT-1").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-2")))!=0 and str(cross.find("AT-2")) != "None":
            f.write(cross.find("AT-2").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-3")))!=0 and str(cross.find("AT-3")) != "None":
            f.write(cross.find("AT-3").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("AT-4")))!=0 and str(cross.find("AT-4")) != "None":
            f.write(cross.find("AT-4").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("M")))!=0 and str(cross.find("M")) != "None": 
            f.write(("%.6f" %float(cross.find("M").text)).ljust(10))
        else:
            f.write("".ljust(10))
        if len(str(cross.find("Theta1")))!=0 and str(cross.find("Theta1")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta1").text)).ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(cross.find("Theta2")))!=0 and str(cross.find("Theta2")) != "None": 
            f.write(("%.3f" %float(cross.find("Theta2").text)).ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return


# FRC: Bond Increments Form	

def XMLtoFrcBondIncrements(root, output_file):
    f = output_file
    f.write("##bond_increments\n\n" )
    f.write("!I     J       DeltaIJ     DeltaJI\n")
    f.write("!----  ----     -------     -------\n")
    for increment in root.findall('./BondIncrements/Bond-Increments'):
        if len(str(increment.find("AT-I")))!=0 and str(increment.find("AT-I")) != "None":
            f.write(increment.find("AT-I").text.ljust(7))
        else:
            f.write("".ljust(7))
        if len(str(increment.find("AT-J")))!=0 and str(increment.find("AT-J")) != "None":
            f.write(increment.find("AT-J").text.ljust(9))
        else:
            f.write("".ljust(9))
        if len(str(increment.find("Delta-IJ")))!=0 and str(increment.find("Delta-IJ")) != "None":
            f.write(increment.find("Delta-IJ").text.ljust(12))
        else:
            f.write("".ljust(12))
        if len(str(increment.find("Delta-JI")))!=0 and str(increment.find("Delta-JI")) != "None": 
            f.write(increment.find("Delta-JI").text.ljust(0))
        else:
            f.write("".ljust(0))
        f.write("\n")
    f.write("\n")
    return


#
# FRC: Converting between tabular XMLs and LAMMPS' .table format
#

def XMLToTableBondPotential_Tabular(root, output_file):
    '''
    Writes XML data for tabular bond potential in FRC format.
    '''
    f = open(output_file, 'w+')
    root = ET.parse(root).getroot()

	# Line 1
	# Write keyword
    f.write((root.findtext('./BondPotential/BondPotential-Tabular/keyword')).encode('utf-8') + '\n')
	
	# Line 2
	# Write N, the number of table entries per column
    f.write("N " + (root.findtext('./BondPotential/BondPotential-Tabular/N')).encode('utf-8'))
	# Checking if fplo and fphi both exist before writing them to file
    if (root.find('./BondPotential/BondPotential-Tabular/fplo') is not None) and (root.find('./BondPotential/BondPotential-Tabular/fphi') is not None):
        f.write(" FP " + (root.findtext('./BondPotential/BondPotential-Tabular/fplo')).encode('utf-8'))
        f.write(" " + (root.findtext('./BondPotential/BondPotential-Tabular/fphi')).encode('utf-8'))
	# Checking if EQ exists before writing
    if (root.find('./BondPotential/BondPotential-Tabular/EQ') is not None):
        f.write(" EQ " + (root.findtext('./BondPotential/BondPotential-Tabular/EQ')).encode('utf-8'))

	# Skip line 3
    f.write('\n')

	# Table data, lines 4 and beyond
    for bond in root.findall('./BondPotential/BondPotential-Tabular/Bond'):
        f.write('\n' + bond.findtext('index').encode('utf-8'))
        f.write(" " + bond.findtext('bond-length').encode('utf-8'))
        f.write(" " + bond.findtext('energy').encode('utf-8'))
        f.write(" " + bond.findtext('force').encode('utf-8'))

	# Close the file
    f.close()
    return



def XMLToTableAnglePotential_Tabular(root, output_file):
    '''
    Writes XML data for tabular angle potential in FRC format.
    '''
    f = open(output_file, 'w+')
    root = ET.parse(root).getroot()

	# Line 1
	# Write keyword
    f.write((root.findtext('./AnglePotential/AnglePotential-Tabular/keyword')).encode('utf-8') + '\n')
	
	# Line 2
	# Write N, the number of table entries per column
    f.write("N " + (root.findtext('./AnglePotential/AnglePotential-Tabular/N')).encode('utf-8'))
	# Checking if fplo and fphi both exist before writing them to file
    if (root.find('./AnglePotential/AnglePotential-Tabular/fplo') is not None) and (root.find('./AnglePotential/AnglePotential-Tabular/fphi') is not None):
        f.write(" FP " + (root.findtext('./AnglePotential/AnglePotential-Tabular/fplo')).encode('utf-8'))
        f.write(" " + (root.findtext('./AnglePotential/AnglePotential-Tabular/fphi')).encode('utf-8'))
	# Checking if EQ exists before writing
    if (root.find('./AnglePotential/AnglePotential-Tabular/EQ') is not None):
        f.write(" EQ " + (root.findtext('./AnglePotential/AnglePotential-Tabular/EQ')).encode('utf-8'))

	# Skip line 3
    f.write('\n')
    f.write('\n')

	# Line 4
	# Write N, the number of table entries per column
    f.write("N " + (root.findtext('./AnglePotential/AnglePotential-Tabular/N')).encode('utf-8'))
	# Checking if fplo and fphi both exist before writing them to file
    if (root.find('./AnglePotential/AnglePotential-Tabular/fplo') is not None) and (root.find('./AnglePotential/AnglePotential-Tabular/fphi') is not None):
        f.write(" FP " + (root.findtext('./AnglePotential/AnglePotential-Tabular/fplo')).encode('utf-8'))
        f.write(" " + (root.findtext('./AnglePotential/AnglePotential-Tabular/fphi')).encode('utf-8'))

	# Table data, lines 5 and beyond
    for angle in root.findall('./AnglePotential/AnglePotential-Tabular/Angle'):
        f.write('\n' + angle.findtext('index').encode('utf-8'))
        f.write(" " + angle.findtext('angle').encode('utf-8'))
        f.write(" " + angle.findtext('energy').encode('utf-8'))
        f.write(" " + angle.findtext('energy-diff').encode('utf-8'))

	# Close the file
    f.close()
    return



def XMLToTableDihedralPotential_Tabular(root, output_file):
    '''
    Writes XML data for tabular dihedral potential in FRC format.
    '''
    f = open(output_file, 'w+')
    root = ET.parse(root).getroot()

	# Line 1
	# Write keyword
    f.write((root.findtext('./DihedralPotential/DihedralPotential-Tabular/keyword')).encode('utf-8') + '\n')
	
	# Line 2
	# Write N, the number of table entries per column
    f.write("N " + (root.findtext('./DihedralPotential/DihedralPotential-Tabular/N')).encode('utf-8'))
	# Checking if angle-units has been specified
    if (root.find('./DihedralPotential/DihedralPotential-Tabular')).attrib['angle-units'] is not None:
        f.write(' ' + ((root.find('./DihedralPotential/DihedralPotential-Tabular')).attrib['angle-units']).upper().encode('utf-8'))
	# Checking if NOF exists before writing to file
    if (root.find('./DihedralPotential/DihedralPotential-Tabular/NOF') is not None):
        if (root.findtext('./DihedralPotential/DihedralPotential-Tabular/NOF')).encode('utf-8') == 'true':
            f.write(" NOF")
	# Checking if CHECKU exists before writing
    if (root.find('./DihedralPotential/DihedralPotential-Tabular/CHECKU') is not None):
        f.write(" CHECKU " + (root.findtext('./DihedralPotential/DihedralPotential-Tabular/CHECKU')).encode('utf-8'))
	# Checking if CHECKF exists before writing
    if (root.find('./DihedralPotential/DihedralPotential-Tabular/CHECKF') is not None):
        f.write(" CHECKF " + (root.findtext('./DihedralPotential/DihedralPotential-Tabular/CHECKF')).encode('utf-8'))

	# Skip line 3
    f.write('\n')

	# Table data, lines 4 and beyond
    for dihedral in root.findall('./DihedralPotential/DihedralPotential-Tabular/Dihedral'):
        f.write('\n' + dihedral.findtext('index').encode('utf-8'))
        f.write(" " + dihedral.findtext('angle').encode('utf-8'))
        f.write(" " + dihedral.findtext('energy').encode('utf-8'))
        f.write(" " + dihedral.findtext('energy-diff').encode('utf-8'))

	# Close the file
    f.close()
    return



def XMLToTableNonBondPotential_Tabular(root, output_file):
    '''
    Writes XML data for tabular non-bond potential in FRC format.
    '''
    f = open(output_file, 'w+')
    root = ET.parse(root).getroot()

	# Line 1
	# Write keyword
    f.write((root.findtext('./NonBondPotential/NonBondPotential-Tabular/keyword')).encode('utf-8') + '\n')
	
	# Line 2
	# Write N, the number of table entries per column
    f.write("N " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/N')).encode('utf-8'))
	# Checking if interpolation style has been specified
    if (root.find('./NonBondPotential/NonBondPotential-Tabular')).attrib['Interpolation-style'] is not None:
        if (root.find('./NonBondPotential/NonBondPotential-Tabular')).attrib['Interpolation-style'] == 'R':
            f.write(" R " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/rlo')).encode('utf-8'))
            f.write(" " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/rhi')).encode('utf-8'))
        elif (root.find('./NonBondPotential/NonBondPotential-Tabular')).attrib['Interpolation-style'] == 'RSQ':
            f.write(" RSQ " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/rlo')).encode('utf-8'))
            f.write(" " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/rhi')).encode('utf-8'))
        elif (root.find('./NonBondPotential/NonBondPotential-Tabular')).attrib['Interpolation-style'] == 'BITMAP':
            f.write(" BITMAP " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/rlo')).encode('utf-8'))
            f.write(" " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/rhi')).encode('utf-8'))
	# Checking if fplo and fphi both exist before writing them to file
    if (root.find('./NonBondPotential/NonBondPotential-Tabular/fplo') is not None) and (root.find('./NonBondPotential/NonBondPotential-Tabular/fphi') is not None):
        f.write(" FPRIME " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/fplo')).encode('utf-8'))
        f.write(" " + (root.findtext('./NonBondPotential/NonBondPotential-Tabular/fphi')).encode('utf-8'))

	# Skip line 3
    f.write('\n')

	# Table data, lines 4 and beyond
    for non_bond in root.findall('./NonBondPotential/NonBondPotential-Tabular/NonBond'):
        f.write('\n' + non_bond.findtext('index').encode('utf-8'))
        f.write(" " + non_bond.findtext('r').encode('utf-8'))
        f.write(" " + non_bond.findtext('energy').encode('utf-8'))
        f.write(" " + non_bond.findtext('force').encode('utf-8'))

	# Close the file
    f.close()
    return



# The functions below create a file with citation information taken from an XML file and outputed as a text file 
def XMLtoCitBib(root, output_file):
    '''
    Writes XML data for citation data in FRC format.
    '''
    f = output_file
    if(root.find("./Force-Field-Header/Data-Source/Compact/Reference") != None):
        citation = (root.find("./Force-Field-Header/Data-Source/Compact/Reference").text)
    if(root.find("./Force-Field-Header/Data-Source/Compact/DOI") != None):
        DOI = (root.find("./Force-Field-Header/Data-Source/Compact/DOI").text)
    f.write("You have downloaded data from webff.nist.gov, if you use this data in any publication please cite the following sources: \n")
    f.write("Data source citation: webff.nist.gov\n")
    f.write("Data source publication: TBA\n")
    f.write("Force-field data citation: "+ citation +", "+ DOI+ "\n" )
    return


