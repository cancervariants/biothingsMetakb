"""A module for MetaKB MOA dumper"""
import os

import biothings, config  # noqa: E401
biothings.config_for_app(config)
from config import DATA_ARCHIVE_ROOT  # noqa: E402

from biothings.utils.common import uncompressall  # noqa: E402

import biothings.hub.dataload.dumper  # noqa: E402


class MetakbMOADumper(biothings.hub.dataload.dumper.LastModifiedHTTPDumper):
    """Dumper for MOA"""

    SRC_NAME = "metakb_moa"
    SRC_ROOT_FOLDER = os.path.join(DATA_ARCHIVE_ROOT, SRC_NAME)
    SCHEDULE = None
    UNCOMPRESS = True
    SRC_URLS = ['https://vicc-metakb.s3.us-east-2.amazonaws.com/cdm/moa_cdm.json.zip']
    __metadata__ = {"src_meta": {}}

    def post_dump(self, *args, **kwargs):
        """If UNCOMPRESS = True, uncompress the file"""
        if self.__class__.UNCOMPRESS:
            self.logger.info("Uncompress all archive files in '%s'" %
                             self.new_data_folder)
            uncompressall(self.new_data_folder)
