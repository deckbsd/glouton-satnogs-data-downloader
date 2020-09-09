import os
import glob
import binascii


class PainaniDecoder:
    def __init__(self):
        pass

    def DecodeImages(self, full_path, file_pattern):
        files = glob.glob(os.path.join(full_path, file_pattern))
        mode = 'rb'
        images = {}
        chunks = []
        for file in files:
            with open(file, mode) as f:
                payload = bytearray(f.read())
                magic = bytearray([0x03, 0xf0, 0xcc, 0xcc])
                magic_id = payload[14:18]
                offset = 37
                if magic_id == magic:
                    image_id = int.from_bytes(payload[25:28], 'big')
                    if image_id not in images.keys():
                        images[image_id] = {}
                    chunk_id = int.from_bytes(payload[28:30], 'big')
                    chunk_size = payload[36]
                    chunk = payload[offset:offset + chunk_size]
                    if len(chunk) == chunk_size:
                        images[image_id][chunk_id] = chunk

        for image_key, chunk in sorted(images.items()):
            image_name = os.path.join(
                full_path, "image_" + str(image_key) + ".j2c")
            print("writing image:", image_name)
            img_sz = 0
            chunks = 0
            f = open(image_name, 'w+b')
            for ch_key, ch_value in sorted(chunk.items()):
                chunks += 1
                binary_data = []
                binary_data = bytearray(ch_value)
                f.write(binary_data)
                img_sz += len(binary_data)
            print("Image", image_key, "size:",
                  chunks, "chunks,", img_sz, "bytes")
            f.close()
