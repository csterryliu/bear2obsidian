import re, os, argparse

RE_BEAR_IMAGE_UUID = "[0-9A-Z]{8}\-[0-9A-Z]{4}\-[0-9A-Z]{4}\-[0-9A-Z]{4}\-[0-9A-Z]{12}\.[a-z]+"
TEST = 'Abstract%20Factory/90489A74-398D-411C-A281-52D6B16F6009.png'

def process_args():
    arg_parser = argparse.ArgumentParser(
                    description='bear2obsidian',
                    add_help=False)

    arg_parser.add_argument('rootDir', action='store')
    return arg_parser.parse_args()

def main():
    args = process_args()
    prefix = args.rootDir.rsplit('/', 1)[0]
    print(prefix)
    depth = 1
    depth_map = {}
    for currentFolder, subfolders, filenames in os.walk(args.rootDir):
        print('depth:', depth)
        print('Current folder: ' + currentFolder)
        print('Subfolders: ' + str(subfolders))
        # print('files: ' + str(filenames))
        mdList = [name.removesuffix('.md')
                  for name in filenames if name.endswith('.md')]
        pngList = [name
                  for name in filenames if name.endswith('.png')]

        if len(mdList) > 0:
            # create the target folder
            target_folder = currentFolder.rsplit('/', depth)[-1]
            print(currentFolder.rsplit('/', depth))
            # copy md files to the target folder
            for f in filenames:
                print('copy ' + '/'.join([target_folder, f]))

        if len(subfolders) > 0:
            depth = depth + 1
            depth_map[depth] = len(subfolders)
        else:
            depth_map[depth] = depth_map[depth] - 1
        print('left folders: ', depth_map[depth])
        if depth_map[depth] == 0:
            depth = depth - 1

        print('--------------------------------')

    
    
    # for folderPath, subfolders, filenames in os.walk(args.rootDir):
    #     print('Current folder: ' + folderPath)
    #     print('Subfolders: ' + str(subfolders))
    #     print('files: ' + str(filenames))
        # mdList = [name.removesuffix('.md')
        #           for name in filenames if name.endswith('.md')]
        # pngList = [name
        #           for name in filenames if name.endswith('.png')]
        # print(str(mdList))
        # print(str(pngList))
        # if len(mdList) > 0:
        #     # create folder for this one
        #     print(folderPath.rsplit('/')[-1])

        # print('--------------------------------')


        # for fullName in filenames:
        #     if fullName.endswith('.md'):
        #         name = fullName.rstrip('.md')
        #         print(name)
    
    # print(TEST)
    # match = re.search(RE_BEAR_IMAGE_UUID, TEST)
    # print(f'![[{match.group()}]]')



if __name__ == '__main__':
    main()