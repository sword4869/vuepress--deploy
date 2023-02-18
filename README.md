The action will auto deploy the vuepress project when you push your code. 

My contribution is `translator-v?.py` which is used to extract the sidebar of config.ts.

## Offline-Usage

```python
python ../vuepress-deploy/translator-v2.py "sword/learn_python"
yarn install
yarn vuepress:build
yarn vuepress:dev
```
## Online-Usage
```bash
python ../vuepress-deploy/translator-v2.py "sword/learn_python"
```
### 自定生成配置的编译
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
          BUILD_SCRIPT: python3 translator-v1.py ${{ github.repository }} && yarn install && yarn vuepress:build
          BUILD_DIR: docs/.vuepress/dist/
```

vuepress-version:
          
- vuepress1: `BUILD_SCRIPT: python3 translator-v1.py ${{ github.repository }} && yarn install && yarn vuepress:build`

- vuepress2: `BUILD_SCRIPT: python3 translator-v2.py ${{ github.repository }} && yarn install && yarn vuepress:build`

### 定制配置的编译

```ts
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
          BUILD_SCRIPT: && yarn install && yarn vuepress:build
          BUILD_DIR: docs/.vuepress/dist/
```

根据你显示创建的config.ts来编译, 而不是由translator-vx.py来生成其.

## Parameters

|  Parameter |  Description | Type | Required
| :------------ | :------------ |:------------ |:------------ |
| `ACCESS_TOKEN` | Personal access token or directly `GITHUB_TOKEN` of repository| `secrets`  |  **Yes** |
| `TARGET_BRANCH` | The branch you want to deploy. e.g.`gh-pages`.Default: **gh-pages** | `env` | **No** |
| `BUILD_SCRIPT` | The script to build the vuepress project. e.g. `yarn install && yarn vuepress:build` | `env` | **Yes** |
| `BUILD_DIR` | The output of the build-script above. e.g. `docs/.vuepress/dist/` | `env` | **Yes** |

## the sidebar style

> v1: 

```ts
sidebar: {
  "/": [
    ["/", "README"],
    {
      title: "01-easy",
      children: [
        {
          title: "python_flask",
          children: [["/01-easy/python_flask/", "README"]],
        },
        {
          title: "python_print_hello",
          children: [["/01-easy/python_print_hello/", "README"]],
        },
      ],
    },
    {
      title: "concept",
      children: [
        ["/concept/container.md", "container.md"],
        ["/concept/docker-compose.md", "docker-compose.md"],
        ["/concept/image.md", "image.md"],
        ["/concept/other.md", "other.md"],
        ["/concept/the_dockerfile.md", "the_dockerfile.md"],
      ],
    },
  ],
},
```
for article: `["LINK", "NAME"]`

for diretory: `{ title: "NAME", children: [ articles.. ] }`

> v2:

```ts
sidebar: {
  "/": [
    { text: "README", link: "/" },
    {
      text: "01-easy",
      children: [
        {
          text: "python_flask",
          children: [{ text: "README", link: "/01-easy/python_flask/" }],
        },
        {
          text: "python_print_hello",
          children: [
            { text: "README", link: "/01-easy/python_print_hello/" },
          ],
        },
      ],
    },
    {
      text: "concept",
      children: [
        { text: "container.md", link: "/concept/container.md" },
        { text: "docker-compose.md", link: "/concept/docker-compose.md" },
        { text: "image.md", link: "/concept/image.md" },
        { text: "other.md", link: "/concept/other.md" },
        { text: "the_dockerfile.md", link: "/concept/the_dockerfile.md" },
      ],
    },
  ],
},
```

for article: `{ text: "NAME", link: "LINK"}`

for directory: as same as v1