
import logging
import io
import pytesseract
from PIL import Image, ImageChops

import numpy as np
import cv2


logger = logging.getLogger(__name__)


class OCREngine:
    def __init__(self, bill_source=None):
        self.bill_source = bill_source

    def analyze_image(self, img_bytes):
        data = []

        img = Image.open(io.BytesIO(img_bytes))

        # nparr = np.fromstring(img_bytes, np.uint8)
        # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        pre_processed_image = self.pre_process_image(img)

        if self.bill_source == 'physical':
            data = self.analyze_physical_source_type_bills(pre_processed_image)
        elif self.bill_source == 'digital':
            data = self.analyze_digital_source_type_bills(pre_processed_image)
        else:
            return []

        formatted_output = self.format_ocr_output(data)
        return formatted_output

    def pre_process_image(self, img_data):
        """
        refer this link - https://stackoverflow.com/questions/
        9480013/image-processing-to-improve-tesseract-ocr-accuracy/10034214#10034214
        """
        bg = Image.new(img_data.mode, img_data.size, img_data.getpixel((0, 0)))
        diff = ImageChops.difference(img_data, bg)
        diff = ImageChops.add(diff, diff, 2.0, -100)
        bbox = diff.getbbox()
        if bbox:
            img_data = img_data.crop(bbox)
        img_data.show()
        return img_data

    def analyze_physical_source_type_bills(self, img_bytes):

        bill_attributes = {
            'name': "",
            'date': "",
            'grand_total': "",
        }

        name = ""
        date = ""
        grand_total = ""

        # will be of type string
        raw_ocr_output = pytesseract.image_to_data(img_bytes)
        all_words = []
        each_row_data = ''
        # iterating over complete string
        for item in raw_ocr_output:
            if item == '\n':
                each_item_list = each_row_data.split("\t")
                all_words.append(each_item_list[-1])
                each_row_data = ''
            else:
                each_row_data += item

        all_words = all_words[1:] # removing column name

        # Applying following logic for extracting attributes like name, date and grand total.
        # 1. Name:
        #    -> First word in invoice is name
        # 2. Date:
        #    -> Usually prefixed with 'Date' keyword
        #    -> or Identify the pattern __/__/____ or __-__-____
        # 3. Bill grand total:
        #    -> Usually prefixed by following keywords - Total, Amount, Total Amount, Grand Total, Total Due, Amount Due

        print(all_words)

        found_title = False
        found_date = False
        found_total_amount = False
        for index, item in enumerate(all_words):
            if item.strip() not in ['', ' '] and not found_title:
                tmp_i = index
                while(all_words[tmp_i] != '' and tmp_i<len(all_words)):
                    name = name + " " + all_words[tmp_i]
                    tmp_i += 1
                found_title = True
            elif 'date' in item.lower() and not found_date:
                # either date value is present in the same item
                # or it is present in next item
                date_val_list = item.split(":")
                if len(date_val_list) > 1 and date_val_list[1] == '':
                    date = all_words[index + 1]
                    found_date = True
                elif len(date_val_list) > 1:
                    date = date_val_list[1]
                    found_date = True
                elif all_words[index + 1] in [':', '-'] and ('/' in all_words[index + 2] or '-' in all_words[index + 2]):
                        date = all_words[index + 2]
                        found_date = True
                else:
                    date = all_words[index+1]
                    found_date = True
            elif 'grand' in item.lower() and not found_total_amount and 'total' in all_words[index + 1].lower():
                # Ex - Grand Total: 440
                grand_total = all_words[index+2]
                found_total_amount = True
            elif 'total' in item.lower() and not found_total_amount and 'amount' in all_words[index + 1].lower():
                # Ex - Total Amount: 440
                grand_total = all_words[index+2]
                found_total_amount = True
            elif 'amount' in item.lower() and not found_total_amount and 'due' in all_words[index + 1].lower():
                # Ex - Amount Due: 440
                grand_total = all_words[index+2]
                found_total_amount = True
            elif ('total' in item.lower() or 'amount' in item.lower()) and not found_total_amount:
                # Ex - Total: 440.0
                try:
                    grand_total = float(all_words[index+1])
                    found_total_amount = True
                except Exception:
                    # value not a float
                    pass
                # Ex - Total: 440
                try:
                    grand_total = int(all_words[index+1])
                    found_total_amount = True
                except Exception:
                    # value not a int
                    pass

            if not found_date:
                # search for date pattern: xx/xx/xxxx
                for index, item in enumerate(all_words):
                    if '/' in item:
                        date_tmp_list = item.split("/")
                        if len(date_tmp_list)>1:
                            date = item

        bill_attributes['name'] = name.strip()
        bill_attributes['date'] = date
        bill_attributes['grand_total'] = grand_total

        return bill_attributes

    def analyze_digital_source_type_bills(self, img_bytes):
        raw_ocr_output = pytesseract.image_to_data(img_bytes)
        return raw_ocr_output

    def format_ocr_output(self, raw_ocr_string_output):
        # with open('tmp_2.txt', 'w') as text_file:
        #     text_file.write(raw_ocr_string_output)
        return raw_ocr_string_output
