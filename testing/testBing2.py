try:
    import os
    from bing_image_downloader import downloader
except Exception as e:
    print(f'error while loading packages ...\n{e}')

#declaring query_string which includes all the buzzwords we need!
query_string = ['ميمز','ميمز بالعربي','ميمز مضحكة','ميمز نكت','نكت بايخه',
                'نكت تحشيش','نكت سخيفه','نكت فيس','نكت واتس',
                'نكت','نكت عربيه','نكت نسوان','نكت اطفال']
#here insert the names of object/person whose data is to be collected(query_string)
for content in query_string:
    #make sure folder is created, if not create one!
    save_loc = "../testing/img/testingImg/"
    if not os.path.exists(save_loc):
        os.mkdir(save_loc)
    #now we download all images we need as declared,
    #and set the limit for every object/image in list.
    downloader.download(content, limit=10, output_dir=save_loc, timeout=120);