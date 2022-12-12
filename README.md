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
          BUILD_SCRIPT: yarn install && yarn vuepress:build
          BUILD_DIR: docs/.vuepress/dist/
          INFO_REPOSITORY: ${{ github.repository }}
```

The action will auto deploy the vuepress project when you push your code. 


## Parameters

|  Parameter |  Description | Type | Required
| :------------ | :------------ |:------------ |:------------ |
| `ACCESS_TOKEN` | Personal access token or directly GITHUB_TOKEN of repository| `secrets`  |  **Yes** |
| `TARGET_BRANCH` | The branch you want to deploy. e.g.`gh-pages`.Default: **gh-pages** | `env` | **No** |
| `BUILD_SCRIPT` | The script to build the vuepress project. e.g. `yarn install && yarn vuepress:build` | `env` | **Yes** |
| `BUILD_DIR` | The output of the build-script above. e.g. `docs/.vuepress/dist/` | `env` | **Yes** |
|`INFO_REPOSITORY`| Pass it to `translator.py` which is used to write the content of `sidebar` | `env`| **Yes**|