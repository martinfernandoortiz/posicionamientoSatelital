#
#


import hatanaka
from pathlib import Path

# decompression
rinex_data = hatanaka.decompress('tgta2740.23d.Z')
# or
rinex_data = hatanaka.decompress(Path('tgta2740.23d.Z').read_bytes())
# or, creates '1lsu0010.21o' directly on disk
hatanaka.decompress_on_disk('tgta2740.23d.Z')

# compression
#Path('1lsu0010.21d.gz').write_bytes(hatanaka.compress(rinex_data))
# or
#Path('1lsu0010.21d.gz').write_bytes(hatanaka.compress('1lsu0010.21o'))
# or, creates '1lsu0010.21d.gz' directly on disk
#hatanaka.compress_on_disk('1lsu0010.21o')
