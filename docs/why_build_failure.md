# analyst of build error

## how to judge whether you build error
```bash
## 1. generate the config.ts
cd .. && git clone git@github.com:sword4869/vuepress-deploy.git
# here we come back to this project
cd - && python ../vuepress-deploy/translator-v2.py xxx

2. build
# usaually here are bulid failure hint if errors occur.
yarn vuepress:build

3. show the blog
yarn vuepress:dev
```

## the common errors
### the url of image in directory
```bash
project
├── docs
│   ├── README.md
│   └── .vuepress
│       └── config.js
├── images
├── node_modules
├── package.json
└── yarn.lock
```
```markdown
![](../images/83ad32c958dacc26e343fa0988ac1868f25889fb9f830f60f9946bf11d77dca4.png)
```

check the num of `..` to ensure the correct of hierachical structure.

### vuepress-vite version in yarn.lock

Caution: there should be a `yarn.lock` in project. Otherwise, your version is default `vuepress-vite@2.0.0-beta.50`.(and even you alter ci.yaml to 'yarn instal && yarn add -D vuepress@next', it is no use. because the error occurs when `yarn install` which means `yarn add -D vuepress@next` won't be executed.)

Resolution: in local host, execute `yarn add -D vuepress@next` which will correct the vuepress-vite to newest version. You will see the correct part in the `yarn.lock` file and then git push to remote host.

```
vuepress-vite@2.0.0-beta.50-pre.1:
  version "2.0.0-beta.60"
  resolved "https://registry.npmmirror.com/vuepress-vite/-/vuepress-vite-2.0.0-beta.60.tgz#844359283f18bbd638a059e3477388b8d2b73a1e"
  integrity sha512-ljHvo419nbfYl/cQecVbYL4bwJjUOX0+z76v/4yX6ODeGIpdHIs7ARZ4t52mr0EEfwP6aZbZa+qFZTTQutxAuQ==
  dependencies:
    "@vuepress/bundler-vite" "2.0.0-beta.60"
    "@vuepress/cli" "2.0.0-beta.60"
    "@vuepress/core" "2.0.0-beta.60"
    "@vuepress/theme-default" "2.0.0-beta.60"

vuepress@^2.0.0-beta.60:
  version "2.0.0-beta.50-pre.1"
  resolved "https://registry.npmmirror.com/vuepress/-/vuepress-2.0.0-beta.50-pre.1.tgz#26eec90444bb37590f29d10dd5923e75c476189f"
  integrity sha512-4Finc3GDscIqgRFAZFwa4SUm8tIFSVQIxnPIpQPW3kaM37rKylvUDkLrs2lMvoDPTAAE+Kf+v34tAFX+ZMGKUg==
  dependencies:
    vuepress-vite "2.0.0-beta.50-pre.1"
```