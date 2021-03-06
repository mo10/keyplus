# Copyright 2018 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)
from hid_keycodes import *
lang = 'Arabic'
country = 'Bahrain, Egypt, Jordan, Kuwait, Lebanon, Oman, Qatar, Saudi Arabia, Syrai, U.A.E, Yemen'
scancode_map = {
    KC_0: ('0', ')', '', '٠', ')', ''),
    KC_1: ('1', '!', '', '١', '!', ''),
    KC_2: ('2', '@', '', '٢', '@', ''),
    KC_3: ('3', '#', '', '٣', '#', ''),
    KC_4: ('4', '$', '', '٤', '$', ''),
    KC_5: ('5', '٪', '', '٥', '٪', ''),
    KC_6: ('6', '^', '', '٦', '^', ''),
    KC_7: ('7', '&', '', '٧', '&', ''),
    KC_8: ('8', '٭', '', '٨', '٭', ''),
    KC_9: ('9', '(', '', '٩', '(', ''),
    KC_A: ('a', 'A', '', 'ش', 'ش', ''),
    KC_B: ('b', 'B', '', 'ﻻ', 'ﻵ', ''),
    KC_C: ('c', 'C', '', 'ؤ', 'ؤ', ''),
    KC_D: ('d', 'D', '', 'ي', 'ي', ''),
    KC_E: ('e', 'E', '', 'ث', 'ث', ''),
    KC_F: ('f', 'F', '', 'ب', 'ب', ''),
    KC_G: ('g', 'G', '', 'ل', 'ل', ''),
    KC_H: ('h', 'H', '', 'ا', 'أ', ''),
    KC_I: ('i', 'I', '', 'ه', '÷', ''),
    KC_J: ('j', 'J', '', 'ت', 'ـ', ''),
    KC_K: ('k', 'K', '', 'ن', '،', ''),
    KC_L: ('l', 'L', '', 'م', '/', ''),
    KC_M: ('m', 'M', '', 'ة', 'ة', ''),
    KC_M: ('m', 'M', '', '〫', '', ''),
    KC_N: ('n', 'N', '', 'ى', 'آ', ''),
    KC_O: ('o', 'O', '', 'خ', '×', ''),
    KC_P: ('p', 'P', '', 'ح', '؛', ''),
    KC_Q: ('q', 'Q', '', 'ض', 'ض', ''),
    KC_R: ('r', 'R', '', 'ق', 'ق', ''),
    KC_S: ('s', 'S', '', 'س', 'س', ''),
    KC_T: ('t', 'T', '', 'ف', 'ف', ''),
    KC_U: ('u', 'U', '', 'ع', 'ع', ''),
    KC_V: ('v', 'V', '', 'ر', 'ر', ''),
    KC_W: ('w', 'W', '', 'ص', 'ص', ''),
    KC_X: ('x', 'X', '', 'ء', 'ء', ''),
    KC_Y: ('y', 'Y', '', 'غ', 'غ', ''),
    KC_Z: ('z', 'Z', '', 'ئ', 'ئ', ''),
    KC_APOSTROPHE: ("'", '"', '', 'ط', '"', ''),
    KC_BACKSPACE: ('\x08', '\x08', '', '\x08', '\x08', ''),
    KC_BACK_SLASH: ('\\', '|', '', '\\', '|', ''),
    KC_COMMA: (',', '<', '', 'و', ',', ''),
    KC_COMMA: (',', '<', '', '〭', '', ''),
    KC_ENTER: ('\r', '', '', '', '', ''),
    KC_EQUAL: ('=', '+', '', '=', '+', ''),
    KC_FORWARD_SLASH: ('/', '?', '', 'ظ', '؟', ''),
    KC_FORWARD_SLASH: ('/', '?', '', '〮', '', ''),
    KC_GRAVE: ('`', '~', '', 'ذ', 'ّ', ''),
    KC_LEFT_BRACKET: ('[', '{', '', 'ج', '>', ''),
    KC_MINUS: ('-', '_', '', '-', '_', ''),
    KC_PERIOD: ('.', '>', '', 'ز', '.', ''),
    KC_PERIOD: ('.', '>', '', '〬', '', ''),
    KC_RIGHT_BRACKET: (']', '}', '', 'د', '<', ''),
    KC_SEMICOLON: (';', ':', '', 'ك', ':', ''),
    KC_SPACEBAR: (' ', ' ', '', ' ', ' ', ''),
    KC_TAB: ('\t', '', '', '\t', '', ''),
}