from sys import argv
import time
import re
name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
with open("./docs/_posts/" + name + ".markdown", "w+") as log:
    content = """---
layout:     post
title:      "Something Wrong"
subtitle:   "Autocheck Report"
date:       {:s}
author:     "BXYMartin"
header-img: "img/post-bg-2015.jpg"
tags:
---

**Time: {:s}**

> “Something wrong with the server!”


## Details

Last check is unsuccessful due to unknown reasons.

""".format(time, time)
    log.writelines(content)
