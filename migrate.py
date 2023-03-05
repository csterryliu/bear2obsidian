import re, os, argparse, shutil

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
    stack = []

    for currentFolder, subfolders, filenames in os.walk(args.rootDir):
        print('Current folder: ' + currentFolder)
        print('Subfolders: ' + str(subfolders))
        # print('files: ' + str(filenames))

        stack.append(len(subfolders))

        depth = len(stack)
        print("depth: " + str(depth))
        print(stack)

        mdList = [name.removesuffix('.md')
                  for name in filenames if name.endswith('.md')]
        pngList = [name
                  for name in filenames if name.endswith('.png')]

        if len(mdList) > 0:
            # create the target folder
            target_folder = '/'.join(currentFolder.rsplit('/', depth)[-depth:])
            print(currentFolder.rsplit('/', depth))
            os.mkdir(target_folder)
            # copy md files to the target folder
            for f in filenames:
                print('copy ' + currentFolder + \
                      '/' + f + ' to ' + target_folder + '/' + f)

        while len(stack) > 1 and stack[-1] == 0:
            stack.pop()
            stack[-1] = stack[-1] - 1

        print('--------------------------------')

    # print(TEST)
    # match = re.search(RE_BEAR_IMAGE_UUID, TEST)
    # print(f'![[{match.group()}]]')



if __name__ == '__main__':
    main()