# -*- coding: utf-8 -*-

if __name__ == "__main__":

    import os
    import sys
    import tarfile 

    xml_path = u""

    tar_gz_name = u""

    # TODO: setup datapool
    #
    datapool = u"D:/datapool"

    # TODO: setup script dir
    #
    script_dir = "E:\01.备份\04.黄炎\3技术培训\2015影像培训班\5_示例数据\exercise 11：归档影像建库\ArchivedRasterType_gf"

    input_file = os.path.join(script_dir, "extract_hj_metadata.in");
    output_file = os.path.join(script_dir, "extract_hj_metadata.out");

    # read input file
    #
    with open(input_file,'r') as fp:
        tar_gz_name = fp.readline()
    
    # check datapool and make it available
    #
    isdir = os.path.isdir(datapool)
    isexists = os.path.exists(datapool)

    if (not isexists) or (isexists and not isdir):
        os.makedirs(datapool)

    tar = None
    
    try:
        
        # open tar.gz
        #
        tar = tarfile.TarFile.open(tar_gz_name)

        # get tar members
        #
        members = tar.getmembers()

        # get group name
        #
        group = members[0].name
        if len(group) > 6:
            raise Exception

        # get jpeg and meta member
        #
        jpeg = None
        meta = None

        for m in members:
            if m.name.upper().find(group+".JPG") >= 0:
                jpeg = m
            if m.name.upper().find(group+".XML") >= 0:
                meta = m

        if jpeg is None or meta is None:
            raise Exception

        fname = os.path.basename(tar_gz_name)
        fname = fname.upper().replace(".TAR.GZ", "")

        tar.extractall(os.path.join(datapool, fname), [meta, jpeg])

        xml_path = os.path.join(datapool, fname, meta.name)
        xml_path = os.path.normpath(xml_path)

        with open(output_file, 'w') as fp:
            fp.write(xml_path)
        
    except:
        pass

    if tar:
        tar.close()

    

