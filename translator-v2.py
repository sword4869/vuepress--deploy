import os
import sys
import json

def tree_dir(dir, part_result, prefix=""):
    files = sorted(os.listdir(dir))
    file_lst = []
    dir_lst = []
    for file in files:
        file_path = os.path.join(dir, file)
        if os.path.isfile(file_path):
            # Only display md
            if file.endswith(".md") == False:
                continue
            file_lst.append(file)
        else: 
            # We don't show folders docs/.vuepress
            if file == ".vuepress":
                continue
            dir_lst.append(file)

    for file in file_lst:
        # README.md need special dealing
        if file.lower() == "readme.md":
            part_result.append({"text": "README", "link": prefix + "/"})

        else:
            part_result.append({"text": file, "link": prefix + "/" + file})

    for subdir in dir_lst:
        subdir_path = os.path.join(dir, subdir)
        part_result.append({"title": subdir, "children": []})
        tree_dir(subdir_path, part_result[-1]["children"], prefix + "/" + subdir)


def tree_empty(part_result):
    # Remove empty chidren
    i = -1
    while i + 1 < len(part_result):
        i += 1
        it = part_result[i]
        if 'children' in it.keys():
            if len(it["children"]) == 0:
                part_result.pop(i)
                continue
            else:
                tree_empty(it["children"])


def get_array():
    path_dest = "docs"
    result = []

    tree_dir(path_dest, result)
    tree_empty(result)

    return result


def main():
    print('translator.py path:', os.getcwd())
    owner_repository = sys.argv[1]
    base = "/" + owner_repository.split("/")[-1] + "/"
    
    theme = {
        'repo': owner_repository,
        "docsDir": "docs",
        "sidebar": {"/": get_array()},
    }

    lines = [
        'import { defineUserConfig } from "vuepress";',
        'import { hopeTheme } from "vuepress-theme-hope";',
        'export default defineUserConfig({',
        f'title: "Hello {owner_repository}",',
        f'base: "{base}",',
        'theme: hopeTheme(',
        json.dumps(theme).encode('utf-8').decode('unicode_escape'),
        ')',
        '});'
    ]
    try:
        with open("./docs/.vuepress/config.ts", "w", encoding="utf-8") as f:
            print(lines)
            f.writelines(lines)
    except FileNotFoundError:
        print(lines)

main()
