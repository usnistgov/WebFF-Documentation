import pandas as pd
import numpy as np
try:
    from lxml import etree as ET
except:
    import xml.etree.ElementTree as ET
import re

def is_not_element(elm):
    # if the tag is not element return true
    return False if "element" in elm.tag else True

def has_element_child(elm):
    # if one of children is element return true
    return True if elm.find('./xs:element',nsmap) is not None else False

def get_element_children_name(elm):
    # return list of element children if there's any, None if there's none
    if has_element_child(elm):
        return [i.attrib['name'] for i in elm.findall('./xs:element',nsmap)]
    else:
        return None
    
def get_multiple_occuring_children(elm):
    # return children whose relation to parent is many to 1, None if such child doesn't exist
    if has_element_child(elm):
        lst = elm.findall('./xs:element[@maxOccurs="unbounded"]',nsmap) 
        if len(lst) == 0:
            return None
        else:
            return lst
    else:
        return None

def ignored_type(elm, whole_schema):
    # if the type should be ignored return true
    return True if whole_schema.find("./*[@name='{}']".format(elm.attrib['type'])) is None else False

def has_enum(elm, whole_schema):
    return True if whole_schema.find("./*[@name='{}']".format(elm.attrib['type'])).find(".//xs:enumeration",nsmap) is not None else False

def get_num_child(root):
    c = 0
    for i in root:
        c += 1
    return c

def is_leaf(root):
    return True if len(root) == 0 else False

def contain_complex(sub_root):
    return True if sub_root.find(".//xs:complexType",nsmap) is not None else False

def resolve_road_map(roadmap, root):
    return resolve_road_map(roadmap[1:],ET.SubElement(root,roadmap[0])) if len(roadmap) > 1 else ET.SubElement(root,roadmap[0])

def group_tabular(d):
    d["AnglePotential-Tabular"] = [d[i] for i in d if re.match("^AnglePotential-Tabular.*\d+",i) is not None]
    d["BondPotential-Tabular"] = [d[i] for i in d if re.match("^BondPotential-Tabular.*\d+",i) is not None]
    d["NonBondPotential-Tabular"] = [d[i] for i in d if re.match("NonBondPotential-Tabular.*\d+",i) is not None]
    d["DihedralPotential-Tabular"] = [d[i] for i in d if re.match("DihedralPotential-Tabular.*\d+",i) is not None]
    
    if d["AnglePotential-Tabular"] == []:
        d.pop("AnglePotential-Tabular")
    if d["BondPotential-Tabular"] == []:
        d.pop("BondPotential-Tabular")
    if d["NonBondPotential-Tabular"] == []:
        d.pop("NonBondPotential-Tabular")
    if d["DihedralPotential-Tabular"] == []:
        d.pop("DihedralPotential-Tabular")
        
    delete = []
    for i in d:
        if re.match("^.*Tabular.*\d+$",i) is not None:
            delete.append(i)
    for dl in delete:
        d.pop(dl)
    
    return d

def rename_dict_key(d,old,new):
    d[new] = d.pop(old)
    return d

def rename_WCA(d):
    return rename_dict_key(d,"NonBondPotential-WCA","NonBondPotential-Weeks-Chandler-Anderson")

def rename_bondincrement(d):
    d["BondIncrement"] = d.pop("BondIncrements")
    return d

def atomistic_rename(d):
    if "BondIncrements" in d:
        d["BondIncrement"] = d.pop("BondIncrements")
    if "AutoEquivalenceTable" in d:
        d["AutoEquivalence"] = d.pop("AutoEquivalenceTable")
    if "EquivalenceTable" in d:
        d["Equivalence"] = d.pop("EquivalenceTable")
        
    return d

def make_xml_element_tabular(sheet, elm_schema, sub_root, roadmap, attr_lst):
    # used when data in excel is arranged in a tabular fashion
    # all data in sheet will be used to create the xml element specified in elm_schema
    # roadmap specified what xml tags will surround the created xml elements
    # attr_lst specified what attributes will go with each element
    
    # first we need to know which road has the data we want 
    xml_names = [i.attrib['name'] for i in elm_schema]
    row = -1
    for i in range(sheet.shape[0]):
        if len(xml_names) <= sheet.shape[1] and (xml_names == sheet.loc[i,:len(xml_names) - 1]).all():
            row = i + 1
            break
    assert(row != -1)
    
    # if attr_lst is present, we need to know which col should be used for attributes
    if attr_lst is not None:
        col = sheet.loc[row-1].loc[sheet.loc[row-1] == attr_lst[0]].index
        assert(len(col) > 0)
        col = col[0]
    # it's assumed that col is greater than 0
    
    for i in range(row, sheet.shape[0]):
        field = resolve_road_map(roadmap,sub_root)
        if attr_lst is not None:
            c = col
            for attr in attr_lst:
                if sheet.loc[i,c] != '':
                    field.set(attr,str(sheet.loc[i,c]))
                c += 1
        c = 0
        for elm in elm_schema:
            if sheet.loc[i,c] != '':
                tmp_field = ET.SubElement(field,elm.attrib['name'])
                tmp_field.text = str(sheet.loc[i,c])
            c += 1
            
def make_xml_element_2tabular(sheet1, sheet2, elm_schema1, elm_schema2, sub_root, roadmap1, roadmap2, name, attr_lst):
    # used when data in excel is arranged in a tabular fashion and locates in two spread sheet
    # all data in sheet will be used to create the xml element specified in elm_schema
    # roadmap specified what xml tags will surround the created xml elements
    # attr_lst specified what attributes will go with each element
    # name indicate which element will use sheet2
    
    # first we need to know which row has the data we want 
    xml_names = [i.attrib['name'] for i in elm_schema1[:-1]]
    row1 = -1   # for sheet1
    for i in range(sheet1.shape[0]):
        if len(xml_names) <= sheet1.shape[1] and (xml_names == sheet1.loc[i,:len(xml_names) - 1]).sum() >= len(xml_names) - 1:
            row1 = i + 1
            break
            
    xml_names = [i.attrib['name'] for i in elm_schema2]
    row2 = -1   # for sheet2
    for i in range(sheet2.shape[0]):
        if len(xml_names) <= sheet2.shape[1] and (xml_names == sheet2.loc[i,1:len(xml_names)]).sum() >= len(xml_names) - 1:
            row2 = i + 1
            break
    assert(row1 != -1 and row2 != -1)
    
    # if attr_lst is present, we need to know which col should be used for attributes
    # it's assumed that only sheet1 is used to create attributes
    if attr_lst is not None:
        col = sheet1.loc[row1-1].loc[sheet1.loc[row1-1] == attr_lst[0]].index
        assert(len(col) > 0)
        col = col[0]
    # it's assumed that col is greater than 0
    
    for i in range(row1, sheet1.shape[0]):
        field = resolve_road_map(roadmap1,sub_root)
        if attr_lst is not None:
            c = col
            for attr in attr_lst:
                if sheet1.loc[i,c] != '':
                    field.set(attr,str(sheet1.loc[i,c]))
                c += 1
        c = 0
        for elm in elm_schema1:
            if elm.attrib['name'] == name:  # if we need to use second sheet
                # select only rows with matching type name
                tmp_sheet = sheet2.loc[row2:,:]
                tmp_sheet = tmp_sheet.loc[tmp_sheet.loc[:,0] == sheet1.loc[i,0]].reset_index(drop=True).loc[:,1:]
                if tmp_sheet.shape[0] != 0:
                    tmp_field = ET.SubElement(field,elm.attrib['name'])
                    for j in range(tmp_sheet.shape[0]):
                        attribute_field = resolve_road_map(roadmap2,tmp_field)
                        cc = 1
                        for elm2 in elm_schema2:
                            if tmp_sheet.loc[j,cc] != '':
                                tmp_attribute_field = ET.SubElement(attribute_field,elm2.attrib['name'])
                                tmp_attribute_field.text = str(tmp_sheet.loc[j,cc])
                            cc += 1
                
            elif sheet1.loc[i,c] != '':
                tmp_field = ET.SubElement(field,elm.attrib['name'])
                tmp_field.text = str(sheet1.loc[i,c])
            c += 1

def make_xml_element_linear_continuous(sheet,elm_schema,sub_root):
    # used when all data in one column will be used to create the SAME xml element
    # Assumes data starts at row 1 of sheet
    xml_name = elm_schema.attrib['name']
    start_row = sheet[1:].loc[sheet.apply(lambda x : xml_name == x and "Instruction" not in x)].index[0] + 1
    for i in range(start_row, sheet.shape[0]):
        if sheet[i] != "":
            field = ET.SubElement(sub_root,elm_schema.attrib['name'])
            field.text = sheet[i]

def make_xml_element_linear(sheet, elm_schema, whole_schema, sub_root, flag):
    # used when data in excel sheet spread out vertically 
    count = 0   # count how many elements are created
    start_row = sheet.loc[:,0].loc[sheet.loc[:,0].map(lambda x : elm_schema[0].attrib['name'] in str(x) and 'instruction' not in x)].index[0]
    for elm in elm_schema:
        if start_row >= sheet.shape[0]: # sheet runs out of data 
            return count
        elif 'type' in elm.attrib and not ignored_type(elm, whole_schema) and not has_enum(elm, whole_schema):
            schema_ptr = whole_schema.find("./*[@name='{}']".format(elm.attrib['type']))[0]
            tmp_root = ET.SubElement(sub_root,elm.attrib['name'])
            start_row += make_xml_element_linear(sheet.loc[start_row:].reset_index(drop=True),schema_ptr,whole_schema,
                                                tmp_root,flag)
            count += 1
        elif flag or sheet.loc[start_row,1] != '':
            field = ET.SubElement(sub_root,elm.attrib['name'])
            field.text = str(sheet.loc[start_row,1])
            count += 1
        start_row += 1
    
    return start_row

def get_attr(sub_root):
    return [i.attrib['name'] for i in sub_root.findall("./xs:attribute",nsmap)]

def make_attr_dict(sheet, elm_schema):
    attr_lst = get_attr(elm_schema[0])
    if len(attr_lst) == 0:
        return {}
    start_row = sheet.loc[:,0].loc[sheet.loc[:,0].map(lambda x : attr_lst[0] in str(x))].index[0]
    attr_dict = {}
    
    c = 0
    for i in range(start_row,sheet.shape[0]):
        if c == len(attr_lst):
            break
        if sheet.loc[i,0] != '' and sheet.loc[i,1] != '':
            attr_dict[attr_lst[c]] = sheet.loc[i,1]
            c += 1
        elif sheet.loc[i,0] != '' and sheet.loc[i,1] == '':
            c += 1
        
    return attr_dict

def excel_transform(xls_file, schema_root, xml_path): 
    schema = schema_root.find('.//xs:element',nsmap)
    
    # create root for xml file
    xml_root = ET.Element(schema.attrib['name']) 
    # move schema to the right place
    schema = schema[0][0]
    
    # metadatas
    sub_root = ET.SubElement(xml_root,schema[0].attrib['name'], {"Version":xls_file["Schema"].loc[5,1]})
    tmp_elm = ET.SubElement(sub_root,"Force-Field-Protocol")
    tmp_elm.text = xls_file["Schema"].loc[4,1]
    
    sub_root = ET.SubElement(xml_root,schema[1].attrib['name'])
    tmp = schema_root.find("./*[@name='{}']".format(schema[1].attrib['type']))[0]
    c = make_xml_element_linear(xls_file['Metadata'],tmp,schema_root,sub_root,True)
    make_xml_element_linear_continuous(xls_file['Keywords'].loc[:,0].reset_index(drop=True), 
                            tmp[c],sub_root) # for keywords
    make_xml_element_linear_continuous(xls_file['Keywords'].loc[:,1].reset_index(drop=True), 
                            tmp[c + 1],sub_root) # for chemistry keywords
    make_xml_element_linear_continuous(xls_file['Keywords'].loc[:,2].reset_index(drop=True), 
                            tmp[c + 2],sub_root) # for material keywords
    make_xml_element_linear_continuous(xls_file['Keywords'].loc[:,3].reset_index(drop=True), 
                            tmp[c + 3],sub_root) # for specialty keywords
    make_xml_element_linear_continuous(xls_file['Keywords'].loc[:,4].reset_index(drop=True), 
                            tmp[c + 4],sub_root) # for additional keywords
    
    sub_root = ET.SubElement(xml_root,schema[2].attrib['name'])
    tmp = schema_root.find(".//*[@name='{}']".format("SimpleReference-Type"))[0]
    make_xml_element_tabular(xls_file['References'], tmp, sub_root, ["Sources","Reference"], None)
    
    sub_root = ET.SubElement(xml_root,schema[3].attrib['name'])
    tmp = schema_root.find(".//*[@name='{}']".format("Contact"))[0]
    make_xml_element_tabular(xls_file['Contacts'], tmp, sub_root, ["Investigator"], None)
    
    sub_root = ET.SubElement(xml_root,schema[4].attrib['name'])
    tmp = schema_root.find(".//*[@name='{}']".format('Notes'))[0]
    if "Scholium" in xls_file:
        make_xml_element_tabular(xls_file['Scholium'], tmp, sub_root, ["Scholium"], None)
    tmp = schema_root.find(".//*[@name='{}']".format('Contact'))[0]
    make_xml_element_tabular(xls_file['Curators'], tmp, sub_root, ["Curator"], None)
    
    for c in schema[5:]:
        # first we need to figure out which sheet we should use 
        # multiple sub element of c could be present, need to account for it
        elements_need_to_create = []
        sheets_for_element = []
        sheet_name = ''
        elm_schema = c
        while(is_not_element(elm_schema[0])): 
            elm_schema = elm_schema[0]
        # sheet finding rule: match sheet name with root's grandchild element name
        # use excel_process_func to rename keys if need to
        for n in xls_file.keys():
            for e in elm_schema:
                if e.attrib['name'] == n: 
                    sheets_for_element.append(n)
                    elements_need_to_create.append(e)
        if(len(elements_need_to_create) == 0): # there is no sheet for this elm
            continue
            
        for i in range(len(elements_need_to_create)):
            elm_schema = elements_need_to_create[i]
            sheet_name = sheets_for_element[i]
            
            if elm_schema.find(".//xs:element",nsmap) is not None:
                schema_ptr = elm_schema
                while(not has_element_child(schema_ptr)):
                    schema_ptr = schema_ptr[0]
            else:
                schema_ptr = None

            # c is the parent xml element, e is the child element 
            # relation between c & e can be 1 to many or 1 to 1
            if 'maxOccurs' in elm_schema.attrib and elm_schema.attrib['maxOccurs'] == "unbounded" and schema_ptr is None: # 1 to many, non tabular type
                # make node for parent xml element
                sub_root = ET.SubElement(xml_root,c.attrib['name'],make_attr_dict(xls_file[sheet_name],c))

                # build roadmap, e is the many side, so use e
                roadmap = [elm_schema.attrib['name']]

                # get list of attributes
                e = elm_schema
                while(len(get_attr(e)) == 0):
                    e = e[0]
                attr_lst = get_attr(e)

                # get schema for the complex type within the element
                e = schema_root.find("./*[@name=\"{}\"]".format(e.attrib['base']))

                make_xml_element_tabular(xls_file[sheet_name],e[0], sub_root,roadmap,attr_lst)
            
            elif 'maxOccurs' in elm_schema.attrib and elm_schema.attrib['maxOccurs'] == "unbounded" and len(get_element_children_name(schema_ptr)) > 1: # 1 to many, tabular type
                # make node for parent xml element
                sub_root = ET.SubElement(xml_root,c.attrib['name'],make_attr_dict(xls_file[sheet_name],c))
                
                # expect sheets with same tabulat type wll be grouped into one list
                for sheet in xls_file[sheet_name]:
                    # root for each sheet
                    tmp_root = ET.SubElement(sub_root,elm_schema.attrib['name'],make_attr_dict(sheet,elm_schema))
                    
                    # get name of child whose relation to tmp_root is many to 1
                    mul = get_multiple_occuring_children(schema_ptr)
                    # only support one 1 to many child
                    assert(len(mul) == 1)
                    mul = mul[0]
                    
                    # create xml child elements
                    tmp_schema_ptr = [i for i in schema_ptr if i.attrib['name'] != mul.attrib['name']]
                    make_xml_element_linear(sheet, tmp_schema_ptr, schema_root, tmp_root, False)
                    
                    # find the schema for the complex type of the 1 to many child
                    tmp_schema_ptr = schema_root.find("./*[@name=\"{}\"]".format(mul.attrib['type']))[0]
                    
                    make_xml_element_tabular(sheet,tmp_schema_ptr, tmp_root,[mul.attrib['name']],None)
                
            else:
                # make node for parent xml element
                sub_root = ET.SubElement(xml_root,c.attrib['name'])
                # since 1 to 1, can just make node for child here
                tmp_root = ET.SubElement(sub_root,elm_schema.attrib['name'],make_attr_dict(xls_file[sheet_name],elm_schema))
                
                # build roadmap
                e = elm_schema.find(".//xs:element",nsmap)
                roadmap = [e.attrib['name']]

                # get list of attributes
                while(len(get_attr(e)) == 0):
                    e = e[0]
                attr_lst = get_attr(e)

                # get schema for the complex type within the element
                e = schema_root.find("./*[@name=\"{}\"]".format(e.attrib['base']))

                # there could be complex type within the schema, 
                # need to differentiate the case
#                 print(e.tag," ",e.attrib)
                if e.find(".//xs:complexType/..",schema_root.nsmap) is None: # without complexType
                    make_xml_element_tabular(xls_file[sheet_name],e[0], tmp_root,roadmap,attr_lst)
                else:
                    e1 = e                                         # over arching complex type
                    e2 = e1.find(".//xs:complexType/..",schema_root.nsmap) # complex type within
                    e3 = e2.find(".//xs:element",schema_root.nsmap)        # reach the inner most node
                    assert('maxOccurs' in e3.attrib)                       # just in case
                    roadmap2 = [e3.attrib['name'] ]                          # since 1 to many
                    e3 = schema_root.find("./*[@name=\"{}\"]".format(e3.attrib['type']))[0] # resolve definition
                    roadmap1 = roadmap
                    e1 = e1[0]
                    sheet_name2 = [i for i in xls_file.keys() if "Attributes" in i][0]
                    make_xml_element_2tabular(xls_file[sheet_name], xls_file[sheet_name2], e1, e3, 
                                              tmp_root, roadmap1, roadmap2, e2.attrib['name'], attr_lst)

                # AtomType-DFF has additional xml element unique to it
                # treat it as an exceptional case rather than try to generalize 
                if elm_schema.attrib['name'] == 'AtomType-DFF' and 'RelationTree-DFF' in xls_file:
                    field = ET.SubElement(tmp_root,"DFFRelationTree")
                    field.text = xls_file['RelationTree-DFF'].loc[4,1]
    
    
    xml_str = ET.tostring(xml_root, pretty_print=True)
    
    with open(xml_path, "wb") as text_file:
        text_file.write(xml_str)
        text_file.close()
        
def excel_xml(excel_path, schema_path, xml_path, excel_process_func, *args, **kwargs):
    # read in excel using pandas
    xls_file = pd.read_excel(excel_path,sheet_name=None,header=None,keep_default_na=False)
    for k in xls_file:
        xls_file[k] = xls_file[k].fillna("")
        xls_file[k].replace([True],1,inplace=True)
        xls_file[k].replace([False],0,inplace=True)
        xls_file[k].replace(["Choose one","Choose value"],"",inplace=True)
    
    # read in xsd schema file
    schema_root = ET.parse(schema_path).getroot()
    global nsmap
    nsmap = schema_root.nsmap
    
    # do the actual conversion
    if excel_process_func is not None:
        excel_transform(excel_process_func(xls_file, *args, **kwargs), schema_root, xml_path)
    else:
        excel_transform(xls_file, schema_root, xml_path)
        
