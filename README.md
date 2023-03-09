# bear2obsidian

## Motivation
When migrating from a Markdown note-taking app to another one, the most frustrating thing is the broken links to the attached images.

I was a fanboy of Bear app. But this year I'd like to move my notes to Obsidian. Therefore, I faced the trouble mentioned above.

I don't want to see broken images inside my notes so I started this tiny and maybe a little boring even useless project.

---
## Folder Structure
### Bear
- folder1
    - file1.md
    - file2.md
    - file2
        - image.png
        - image2.png
    - subfolder1
        - file3.md
        - file3
            - image3.png
        - file4.md
        - file4
            - image4.png

### Obsidian
- folder1
    - file1.md
    - file2.md
    - attachments
        - image.png
        - image2.png
    - subfolder1
        - file3.md
        - file4.md
        - attachments
            - image3.png
            - image4.png

#### Rule To Link A Image
### Bear
- Images referred by a Markdown file is put into the folder with an identical name in the same path.
- Syntax
`![](path_to_the_file/filename.extension)`

#### Obsidian
- Images reffered by Markdown files are put into the "attachments" folder in the same path.
- Syntax
`![[filename.extension]]`

### Objective
- Change the folder structure.
- Move images into "attachments" folder.
- Change the syntax to link to a image.

---
## License
MIT