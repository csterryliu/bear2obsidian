import re, os, argparse, shutil

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

        mdList = [name
                  for name in filenames if name.endswith('.md')]
        pngList = [name
                   for name in filenames if name.endswith('.png')]

        target_folder = '/'.join(currentFolder.rsplit('/', depth)[-depth:])
        print(currentFolder.rsplit('/', depth))
        if len(mdList) > 0:
            # create the target folder
            # os.mkdir(target_folder)
            # copy md files to the target folder
            for f in mdList:
                src = currentFolder + '/' + f
                dest = target_folder + '/' + f
                if f.removesuffix('.md') in subfolders:
                    print(src + ' has to be parsed!!')
                else:
                    print('copy ' + src + ' to ' + dest)

        if len(pngList) > 0:
            attachments = (target_folder.rsplit('/', 1)[0] + '/attachments')
            if not os.path.exists(attachments):
                print('create attachments: ' + attachments)
                # os.mkdir(target_folder)
            # copy png files to attachments folder
            for f in pngList:
                src = currentFolder + '/' + f
                dest = attachments + '/' + f
                print('copy ' + src + ' to ' + dest)

        while len(stack) > 1 and stack[-1] == 0:
            stack.pop()
            stack[-1] = stack[-1] - 1

        print('--------------------------------')



if __name__ == '__main__':
    main()