import re
import os
import argparse
import shutil

RE_IMAGE_FILENAME = "\!\[\]\([\w\W]+\/([\w\W]+)\)"
SPACE = "%20"
IMAGE_TUPLE = ("png", "jpg", "HEIC")
VERBOSE = False


def process_args():
    arg_parser = argparse.ArgumentParser(
                    description='bear2obsidian',
                    add_help=False)

    arg_parser.add_argument('rootDir', action='store')
    return arg_parser.parse_args()


def parse_links_to_images(source_file, target_file):
    with open(target_file, 'w', encoding='utf8') as dest:
        with open(source_file, 'r', encoding='utf8') as src:
            for line in src:
                match = re.search(RE_IMAGE_FILENAME, line.strip())
                if match:
                    matched_str = (match.group(1)).removeprefix('/')\
                        .replace(SPACE, " ")
                    dest.write(f'![[{matched_str}]]\n')
                else:
                    dest.write(line.strip() + '\n')


def log_verbose(log, is_verbose_on=VERBOSE):
    if is_verbose_on:
        print(log)


def main():
    args = process_args()
    prefix = args.rootDir.rsplit('/', 1)[0]
    log_verbose(prefix)
    stack = []

    for currentFolder, subfolders, filenames in os.walk(args.rootDir):
        print('Current folder: ' + currentFolder)
        log_verbose('Subfolders: ' + str(subfolders))

        stack.append(len(subfolders))

        depth = len(stack)
        log_verbose("depth: " + str(depth))
        log_verbose(stack)

        mdList = [name
                  for name in filenames if name.endswith('.md')]
        imgList = [name
                   for name in filenames if name.endswith(IMAGE_TUPLE)]

        target_folder = '/'.join(currentFolder.rsplit('/', depth)[-depth:])
        log_verbose(currentFolder.rsplit('/', depth))

        # create the target folder
        if len(imgList) == 0 and not os.path.exists(target_folder):
            log_verbose("create folder: " + target_folder)
            os.mkdir(target_folder)
        # copy md files to the target folder
        for f in mdList:
            src = currentFolder + '/' + f
            dest = target_folder + '/' + f
            print("src: ", src)
            print("dest: ", dest)
            if f.removesuffix('.md') in subfolders:
                log_verbose(src + ' has to be parsed!!')
                parse_links_to_images(src, dest)
            else:
                log_verbose('copy ' + src + ' to ' + dest)
                shutil.copyfile(src, dest)

        if len(imgList) > 0:
            attachments = target_folder.rsplit('/', 1)[0] + '/attachments'
            if not os.path.exists(attachments):
                log_verbose('create attachments: ' + attachments)
                os.mkdir(attachments)
            # copy png files to attachments folder
            for f in imgList:
                src = currentFolder + '/' + f
                dest = attachments + '/' + f
                log_verbose('copy ' + src + ' to ' + dest)
                shutil.copyfile(src, dest)

        while len(stack) > 1 and stack[-1] == 0:
            stack.pop()
            stack[-1] = stack[-1] - 1

        print('--------------------------------')


if __name__ == '__main__':
    main()
