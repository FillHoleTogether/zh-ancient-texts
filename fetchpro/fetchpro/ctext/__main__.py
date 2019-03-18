# -*- coding: utf-8 -*-

# Copyright (c) Huoty, All rights reserved
# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2019-03-11 20:50:07

if __name__ == "__main__":
    from ..core.log import setup_logging
    from ..core.config import load_config
    from . import CTextCrawler
    load_config()
    setup_logging()
    CTextCrawler().start()
