import re, argparse

RE_BEAR_IMAGE_UUID = "[0-9A-Z]{8}\-[0-9A-Z]{4}\-[0-9A-Z]{4}\-[0-9A-Z]{4}\-[0-9A-Z]{12}\.[a-z]+"
TEST = 'Abstract%20Factory/90489A74-398D-411C-A281-52D6B16F6009.png'

arg_parser = argparse.ArgumentParser(
                    description='parse_image_link',
                    add_help=False)

arg_parser.add_argument('file', action='store')
args = arg_parser.parse_args()
print("input: " + args.file)

with open('test.txt', 'w', encoding='utf8') as dest:
    with open(args.file, 'r', encoding='utf8') as src:
        for line in src:
            match = re.search(RE_BEAR_IMAGE_UUID, line.strip())
            if match:
                # print(f'![[{match.group()}]]')
                dest.write(f'![[{match.group()}]]\n')
            else:
                # print(line.strip())
                dest.write(line.strip() + '\n')

# print(TEST)
# match = re.search(RE_BEAR_IMAGE_UUID, TEST)
# print(f'![[{match.group()}]]')
