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
            part_result.append([prefix + "/", "README"])
        else:
            part_result.append([prefix + "/" + file, file])

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
        if type(it) == type([]):
            continue
        elif type(it) == type({}):
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

    result = [ i.encode('utf-8').decode('unicode_escape') for i in result]

    return result


def main():
    owner_repository = sys.argv[1]
    base = "/" + owner_repository.split("/")[-1] + "/"
    plugins = [
        "vuepress-plugin-helper-live2d",
        "vuepress-plugin-reading-progress",
        "vuepress-plugin-code-copy",
    ]
    themeConfig = {
        # if your docs are in a different repo from your main project:
        "docsRepo": owner_repository,
        # if your docs are in a specific branch (defaults to 'master'):
        "docsBranch": "main",
        # if your docs are not at the root of the repo:
        "docsDir": "docs",
        # defaults to false, set to true to enable
        "editLinks": True,
        # custom text for edit link. Defaults to "Edit this page"
        "editLinkText": "Help us improve this page!",
        "sidebar": {"/": get_array()},
    }

    map_result = {
        "title": 'Hello' + owner_repository,
        "base": base,
        "plugins": plugins,
        "themeConfig": themeConfig,
    }
    with open("./docs/.vuepress/config.ts", "w", encoding="utf-8") as f:
        lines = [
            'import { defineConfig } from "vuepress/config";',
            "export default defineConfig(",
            json.dumps(map_result),
            ");",
        ]
        print(lines)
        f.writelines(lines)

main()
