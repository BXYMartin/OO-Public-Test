from sys import argv
import time
import re
script, first, second, third = argv


name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open("./docs/_posts/" + name + ".markdown", "w+") as log:
    content = """---
layout:     post
title:      "Check Finished"
subtitle:   "{:s} Report"
date:       {:s}
author:     "BXYMartin"
header-img: "img/post-bg-2015.jpg"
tags:
---

**Time: {:s}**

> “Check {:s}!”


## Details

Successful participants:

```
{:s}
```

Models are:

```
{:s}
```

""".format(third, time, time, third, first, second)
    log.writelines(content)
