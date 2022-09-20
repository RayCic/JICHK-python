#!/usr/bin/env python
#
# Copyright (c) 2022, Raimonds Cicans
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from string_replacer import *


class CrazyConverter:
    HIRAGANA = 0
    KATAKANA = 1

    # Hiragana dictionary
    HIRAGANA_DICTIONARY = {
        # First row
        0: {
            "A": "あ",
            "I": "い",
            "U": "う",
            "E": "え",
            "O": "お",

            "А": "あ",
            "И": "い",
            "У": "う",
            "Э": "え",
            "О": "お",
        },
        # Second row
        1: {
            "KA": "か",
            "KI": "き",
            "KU": "く",
            "KE": "け",
            "KO": "こ",

            "КА": "か",
            "КИ": "き",
            "КУ": "く",
            "КЭ": "け",
            "КО": "こ",
        },
        # Third row
        2: {
            "SA": "さ",
            "SHI": "し",
            "SU": "す",
            "SE": "せ",
            "SO": "そ",

            "СА": "さ",
            "СИ": "し",
            "СУ": "す",
            "СЭ": "せ",
            "СО": "そ",
        },
        # Fourth row
        3: {
            "TA": "た",
            "CHI": "ち",
            "TSU": "つ",
            "TE": "て",
            "TO": "と",

            "ТА": "た",
            "ТИ": "ち",
            "ЦУ": "つ",
            "ТЭ": "て",
            "ТО": "と",
        },
        # Fifth row
        4: {
            "NA": "な",
            "NI": "に",
            "NU": "ぬ",
            "NE": "ね",
            "NO": "の",

            "НА": "な",
            "НИ": "に",
            "НУ": "ぬ",
            "НЭ": "ね",
            "НО": "の",
        },
        # Sixth row
        5: {
            "HA": "は",
            "HI": "ひ",
            "FU": "ふ",
            "HE": "へ",
            "HO": "ほ",

            "ХА": "は",
            "ХИ": "ひ",
            "ФУ": "ふ",
            "ХЭ": "へ",
            "ХО": "ほ",
        },
        # Seventh row
        6: {
            "MA": "ま",
            "MI": "み",
            "MU": "む",
            "ME": "め",
            "MO": "も",

            "МА": "ま",
            "МИ": "み",
            "МУ": "む",
            "МЭ": "め",
            "МО": "も",
        },
        # Eighth row
        7: {
            "RA": "ら",
            "RI": "り",
            "RU": "る",
            "RE": "れ",
            "RO": "ろ",

            "РА": "ら",
            "РИ": "り",
            "РУ": "る",
            "РЭ": "れ",
            "РО": "ろ",
        },
        # Ninth row
        8: {
            "WA": "わ",
            "WO": "を",

            "ВА": "わ",
            "ВО": "を",
        },
        # Tenth row
        9: {
            "N": "ん",

            "Н": "ん",
        },
    }

    # Katakana dictionary
    KATAKANA_DICTIONARY = {
        # First row
        0: {
            "A": "ア",
            "I": "イ",
            "U": "ウ",
            "E": "エ",
            "O": "オ",

            "А": "ア",
            "И": "イ",
            "У": "ウ",
            "Э": "エ",
            "О": "オ",
        },
        # Second row
        1: {
            "KA": "カ",
            "KI": "キ",
            "KU": "ク",
            "KE": "ケ",
            "KO": "コ",

            "КА": "カ",
            "КИ": "キ",
            "КУ": "ク",
            "КЭ": "ケ",
            "КО": "コ",
        },
        # Third row
        2: {
            "SA": "サ",
            "SHI": "シ",
            "SU": "ス",
            "SE": "セ",
            "SO": "ソ",

            "СА": "サ",
            "СИ": "シ",
            "СУ": "ス",
            "СЭ": "セ",
            "СО": "ソ",
        },
        # Fourth row
        3: {
            "TA": "タ",
            "CHI": "チ",
            "TSU": "ツ",
            "TE": "テ",
            "TO": "ト",

            "ТА": "タ",
            "ТИ": "チ",
            "ЦУ": "ツ",
            "ТЭ": "テ",
            "ТО": "ト",
        },
        # Fifth row
        4: {
            "NA": "ナ",
            "NI": "ニ",
            "NU": "ヌ",
            "NE": "ネ",
            "NO": "ノ",

            "НА": "ナ",
            "НИ": "ニ",
            "НУ": "ヌ",
            "НЭ": "ネ",
            "НО": "ノ",
        },
        # Sixth row
        5: {
            "HA": "ハ",
            "HI": "ヒ",
            "FU": "フ",
            "HE": "ヘ",
            "HO": "ホ",

            "ХА": "ハ",
            "ХИ": "ヒ",
            "ФУ": "フ",
            "ХЭ": "ヘ",
            "ХО": "ホ",
        },
        # Seventh row
        6: {
            "MA": "マ",
            "MI": "ミ",
            "MU": "ム",
            "ME": "メ",
            "MO": "モ",

            "МА": "マ",
            "МИ": "ミ",
            "МУ": "ム",
            "МЭ": "メ",
            "МО": "モ",
        },
        # Eighth row
        7: {
            "RA": "ラ",
            "RI": "リ",
            "RU": "ル",
            "RE": "レ",
            "RO": "ロ",

            "РА": "ラ",
            "РИ": "リ",
            "РУ": "ル",
            "РЭ": "レ",
            "РО": "ロ",
        },
        # Ninth row
        8: {
            "WA": "ワ",
            "WO": "ヲ",

            "ВА": "ワ",
            "ВО": "ヲ",
        },
        # Tenth row
        9: {
            "N": "ン",

            "Н": "ン",
        },
    }

    @classmethod
    def convert_text(cls, settings, text):
        alphabet = settings["alphabet"]
        rows = settings["rows"]

        if alphabet == cls.HIRAGANA:
            dictionary = cls.HIRAGANA_DICTIONARY
        elif alphabet == cls.KATAKANA:
            dictionary = cls.KATAKANA_DICTIONARY
        else:
            raise ValueError("Bad 'alphabet' value", alphabet)

        # Generate dictionary subset from preferences
        data = {}
        for i in rows:
            if rows[i]:
                data.update(dictionary[i])

        if data:
            replacer = StringReplacer(data)
            return replacer(text)
        else:
            return text
