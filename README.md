The action will auto deploy the vuepress project when you push your code. 

My contribution is `translator-v?.py` which is used to extract the sidebar of config.ts.

## Usage
```yml
name: Build and Deploy
on: 
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: vuepress-deploy
        uses: sword4869/vuepress-deploy@main
        env:
          ACCESS_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          TARGET_BRANCH: gh-pages
          BUILD_SCRIPT: python3 translotor-v1.py ${{ github.repository }} && yarn install && yarn vuepress:build
          BUILD_DIR: docs/.vuepress/dist/
```

vuepress-version:
          
- vuepress1: `BUILD_SCRIPT: python3 translotor-v1.py ${{ github.repository }} && yarn install && yarn vuepress:build`

- vuepress2: `BUILD_SCRIPT: python3 translotor-v2.py ${{ github.repository }} && yarn install && yarn vuepress:build`

## Parameters

|  Parameter |  Description | Type | Required
| :------------ | :------------ |:------------ |:------------ |
| `ACCESS_TOKEN` | Personal access token or directly GITHUB_TOKEN of repository| `secrets`  |  **Yes** |
| `TARGET_BRANCH` | The branch you want to deploy. e.g.`gh-pages`.Default: **gh-pages** | `env` | **No** |
| `BUILD_SCRIPT` | The script to build the vuepress project. e.g. `yarn install && yarn vuepress:build` | `env` | **Yes** |
| `BUILD_DIR` | The output of the build-script above. e.g. `docs/.vuepress/dist/` | `env` | **Yes** |

## the sidebar style

> v1: 

```ts
sidebar: {
  "/": [
    ["/", "README"],
    ["/theme.md", "theme.md"],
    {
      title: "create",
      children: [
        ["/create/deploy\u811a\u672c.md", "deploy\u811a\u672c.md"],
        ["/create/github action.md", "github action.md"],
        [
          "/create/\u56fe\u7247\u683c\u5f0f.md",
          "\u56fe\u7247\u683c\u5f0f.md",
        ],
        ["/create/\u7a7a\u9879\u76ee.md", "\u7a7a\u9879\u76ee.md"],
        { title: "fake", children: [["/create/fake/test.md", "test.md"]] },
      ],
    },
  ],
},
```
for article: `["LINK", "NAME"]`

for diretory: `{ title: "NAME", children: [ articles.. ] }`

> v2:

```ts

```

for article: `{ text: "NAME", link: "LINK"}`

for directory: as same as v1